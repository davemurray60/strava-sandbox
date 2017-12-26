# Install

This creates a directory we will hence refer to as your "virtual environment" where all of your dependencies will be downloaded to rather than installing them to your root libraries

	virtualenv -p python3 env

This activates your environment so that when you run python only the files in your virtual environment are used

	. env/bin/activate


This installs all of your dependencies into your virtual environment

	pip install -r requirements.txt


# Authenticate

Acquire the client client_secret

	cat client_secret.txt

Acquire your user token

	python get_token.py [CLIENT_SECRET]

# Fetch

GET your last 200 activities

	python get_activities.py [YOUR_TOKEN]

# Reference

Strava API

	http://strava.github.io/api/
