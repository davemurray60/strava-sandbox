from aiohttp import web
import asyncio
import requests
import sys
import webbrowser


DOMAIN = 'https://www.strava.com'
BASE_URL = '/api/v3'
CLIENT_ID = 22199

def exchange_code_for_token(code, secret):
    response = requests.post('{0}{1}/oauth/token'.format(DOMAIN, BASE_URL),
        params={
            'client_id': CLIENT_ID,
            'client_secret': secret,
            'code': code
        }
    )
    json = response.json()
    return json['access_token']


async def get_code():
    code_future = asyncio.Future()

    async def authorized(request):
        code = request.query['code']
        code_future.set_result(code)
        return web.Response(text=code)

    # start server
    loop = asyncio.get_event_loop()
    app = web.Application()
    app.router.add_get('/', authorized)
    handler = app.make_handler()
    server_future = loop.create_server(handler, '0.0.0.0', 8080)
    server = loop.create_task(server_future)

    # initiate oauth flow
    redirect_uri = 'http://localhost:8080'
    auth_url = '{0}/oauth/authorize?client_id={1}&redirect_uri={2}&response_type=code'.format(DOMAIN, CLIENT_ID, redirect_uri)
    webbrowser.open(auth_url)

    # wait for code
    code = await code_future

    # shutdown server
    await app.shutdown()
    await handler.shutdown(60.0)
    await app.cleanup()

    return code


async def get_token(secret):
    code = await get_code()
    return exchange_code_for_token(code, secret)


if __name__ == '__main__':
    secret = sys.argv[1]

    loop = asyncio.get_event_loop()
    token_future = asyncio.ensure_future(get_token(secret))
    loop.run_until_complete(token_future)
    print(token_future.result())
    loop.close()
