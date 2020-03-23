## Intro
This is proof of concept project for api authorization for FlaskAPI project.

## Setup
Install virtualenv and activate it using commands:

`python -m virtalenv ./env`

For Linux: `source ./env/bin/activate`

For Windows: `.\env\Scripts\activate`

Install requirements using command:
`pip install -r requirements.txt`

## Running the web server
To run the web server, simply run the following command:

`python app.py`

## Running the tests
To run the tests, web server should be ran first and live.
To run the tests, execute the following commands:

`cd tests`

`python tests.py`

## The idea
Api keys should be sent in headers with key 'Authorization'. Implement decorator function which will check if valid API key is sent in the request headers. To authorize a route decorate it with `@api_key_required`. API keys can be stored and or generated different ways.

## Elaboration
For POC, dict containing API keys is located in conf file `/app/config/dev.py`. Dict keys are API keys, while the values are user's name and surname.

Decorator implementation is located at `/app/auth/wrappers.py` and checks if API key is in headers with key Authorization and if it is valid.

To authorize a route decorate it with `@api_key_required` but first import the decorator like this:

`from app.auth.wrappers import api_key_required`

If route is not decorated with `@api_key_required` API key check will not be executed. In `/app/books/routes` there are examples of both decorated and not decorated routes.

Take a look at `/tests/tests.py` to see how valid request in Python is generated.

## Conclusion
POC works. POC can be edited to store the API keys in database. Genrator of API keys can also be generated, and API keys can be connected with standard Auth for users in later phases.
