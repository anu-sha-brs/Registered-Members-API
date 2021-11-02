# Registered Members Api

The API provides functionality to get statistics about registered persons from datasource api "https://reqres.in/" and gets statistics of names from lookup api "https://api.genderize.io". The application uses Python Flask micro-framework to build rest api with Swagger frontend. 

## Requirements
* Python 3 stable version
* Docker and Docker-compose [Installation](https://docs.docker.com/engine/install/)

## Quick Start
* Clone the repository
* Build docker services docker-compose build
* Launch the container docker-compose up
* Go to Swagger http://localhost:5000/swagger/ 
* To shutdown: docker-compose down

## Unit Tests
To perform unit tests run the below command. The outcome of the tests looks as below.
* nosetests --verbosity=2
> Test getting all registered members ... ok
Test getting a single member ... ok
Test getting a non existent member ... ok
Test getting statistical information of all registered members ... ok

----------------------------------------------------------------------
Ran 4 tests in 11.503s

OK

## Run without docker container
* Start the flask server by running 
> python app.py
* Requests can be sent to get statistical information of registered members as follows:
> curl -X GET "http://localhost:5000/statistical-information" -H  "accept: application/json"
