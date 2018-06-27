# RIDE MY WAY API

[![Build Status](https://api.travis-ci.org/marthamareal/ride-my-way-API.svg?branch=feature)](https://travis-ci.org/marthamareal/ride-my-way-API.svg?branch=feature)
[![Coverage Status](https://coveralls.io/repos/github/marthamareal/ride-my-way-API/badge.svg?branch=feature)](https://coveralls.io/github/marthamareal/ride-my-way-API?branch=feature)
[![Maintainability](https://api.codeclimate.com/v1/badges/881bb003dd26c80d3fc4/maintainability)](https://codeclimate.com/github/marthamareal/ride-my-way-API/maintainability)

It is built using python and flask

## Installation

create a virtual environment with (virtualenv yourEnv).

Activate the virtual environment. (source yourEnv/bin/activate)

install python (pip install python)

Install Flask (pip install flask)

Install requirements (pip freeze > requirements.txt)

# Endpoints in the API

|REQUEST TYPE| URL | DESCRIPTION |
|------------|-----|-------------|
|POST| /api/v1/rides/create |Create ride offer|
|GET| /api/v1/rides |Get all ride offers|
|GET| /api/v1/rides/<int:ride_id> |Get specific ride|
|POST| /api/v1/rides/create |Request to join ride|
|GET| /api/v1/ride_requests/requests |Get all ride requests|
|POST| /api/v1/requests/ride_requests/approve |Approve ride request|
|GET| /api/v1/notifications |Get all notifications|
|DELETE| /api/v1/rides/delete/<int:ride_id>|Delete ride offer|
|DELETE| /api/v1/rides/ride_requests/delete/<int:request_id> |Delete ride request|
|DELETE| /api/v1/notifications/delete/<int:notification_id> |Delete notification|

## Deployment

install flassger (pip install flasgger) for documenting the api

Application is deployed using Heroku.

checkout on [View App](https://ride-my-way-v1-api.herokuapp.com)
