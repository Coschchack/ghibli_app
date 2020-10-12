# Python Back-end Assignment: Movie List

## Assignment description
Studio Ghibli is a Japanese movie company. They offer a ​REST API ​where one can query information about movies and people (characters).

The task is to write a Python application which serves a page on localhost:8000/movies/. This page should contain a plain list of all movies from the Ghibli API. For each movie the people that appear in it should be listed.

Do not use the ​people ​field on the ​/films​ endpoint, since it’s broken. There is a list field called films ​on the ​/people ​endpoint which you can use to get the relationship between movies and the people appearing in them.

You don’t have to worry about the styling of that page.

Since accessing the API is a time-intensive operation, it should not happen on every page load. But on the other hand, movie fans are a very anxious crowd when it comes to new releases, so make sure that the information on the page is not older than 1 minute when the page is loaded.

The code should be submitted in a clean and refactored state. Please format the code according to the PEP8 conventions.

Don’t forget to test your code. Your tests don’t have to be complete, but you should describe how you would extend them if you had the time.
 
If you have to skip some important work due to time limitations, feel free to add a short description of what you would improve and how if you had the time for it.


## Starting/stopping the application
All commands need to be executed from root folder of the repository (main ghibli_app folder).

### Start
1. Build the needed image(s):
`docker-compose -f docker/docker-compose.yml build`
2. Start the services needed by the application and the application itself:
`docker-compose -f docker/docker-compose.yml up -d`
3. Open a browser and access the application by `http://localhost:8000/movies/`

### Stop
1. To stop and remove: `docker-compose -f docker/docker-compose.yml down`

### Run tests
1. Build the needed image(s):
`docker-compose -f docker/docker-compose.yml build`
2. Start the tests e.g. on the web service:
`docker-compose -f docker/docker-compose.yml run --rm web pytest -v -l tests/`


## To Do
- Tests:
    - implement `pytest-django` instead of raw pytest as it provides nice features
    - extend tests to other layers:
        - some tests with Django test_client
        - Selenium tests (if needed)
- Refactor:
    - page/data caching for 60 seconds instead of celery and DB
    - storing peoples differently than in a string
    - maybe make the URLs not primitive strings i.e. create a Url class
- Dockers:
    - after starting the application in Docker, we need to wait 60 sec for the database to be filled with Ghibli data. 
    It's due to the Celery periodic task. Improve this to fill the database when the Django server starts.
    - make them more customizable e.g. allow to change Django settings like DEBUG, ALLOWED_HOSTS etc.
    - separate database from the web service
    - reduce the number of needed docker containers for the app
- Linter - pylint or flake8