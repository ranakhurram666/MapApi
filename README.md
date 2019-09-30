# MEDWING - Google Map

This application shows Google Map and markers on saved locations in it.
Application is developed using
- ##### React, Redux and Jest [Front-End]
- ##### Python, Flask, MySql [Back-End]

State management in front-end is achieved through Redux. Front-End unit test are written in Jest.
# Features
Following are the feature and their test cases.

- User can add, update, fetch and delete markers from front-end application.
- Once User saves or updates a marker, data will be saved in database and reflect changes on front-end as well immediately.

## Front-End Installation

- Clone the repo or download code from [React application - Google Map Markers](https://github.com/ranakhurram666/GoogleMaps)
- Run `npm install` in the root folder
- Make sure that Flask server is running
- Run `npm run dev`
- To run tests, run `npm tests -- -u`

## Back-End Installation

- Install Python 2.7
- Install pip for Python 2.7 by running `apt-get install python-pip`
- Clone or download code from [Python Flask API - Google Map Markers](https://github.com/ranakhurram666/MapApi)
- Run `pip install -r requirements.txt` in code's root folder
- Create MySql database and define your DB_NAME, DB_USER, DB_PASSWORD and DB_HOST in `constants.py	`
- Now Run `python run.py`
- Application is running on http://0.0.0.0:5000