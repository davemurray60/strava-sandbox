import requests
import sys

DOMAIN = 'https://www.strava.com'
BASE_URL = '/api/v3'

def get_activities(token):
    response = requests.get('{0}{1}/athlete/activities'.format(DOMAIN, BASE_URL),
        headers={
            'Authorization': 'Bearer {0}'.format(token),
        },
        params={
            'per_page': 200
        }
    )
    return response.json()


if __name__ == '__main__':
    token = sys.argv[1]
    activities = get_activities(token)
    print('id,type,name,start_date,distance,time')
    for activity in activities:
        _id = activity['id']
        _type = activity['type']
        name = activity['name']
        start_date = activity['start_date']
        distance = activity['distance']
        time = activity['moving_time']
        print(_id, _type, name, start_date, distance, time)
