# Deployable development environment
This is an exercise to create a containerized system of a flask service and postgresql using docker.
## Table of contents:
* Repo content
* Setup
* Test Calls

## Repo Content:
* **docker-compose.yml**: Compose to orchistrate the creation of the containers. 
* **app**: contains the flask app related files:
  * **Dockerfile**: flask container specific instructions.
  * **app.py**: The flask python code.
  * **wsgi.py**: To run the app through gunicorn
  * **requirements.txt**: Python requirements to run the service.
  * **config.py**: Dict to map env-variables to keys.
* **db**: contains the db related files:
  * **Dockerfile**: specific instructions to build the postgres container.
  * **rates.sql**: SQL dump file to build the db from.
  * **db.env**: Environment file, maps DB env variables to values. Used both by both app and db containers. Shouldn't be part of the repo, added here for simplicity.

## Setup:
1. Clone this repo locally.
2. Make sure you have docker and docker compose cli installed. (through apt-get, brew). 
3. cd to repo and run `docker-compose up -d` to download the images and build the containers.
**Notes**:
* The DB should be built automatically from the dump as it is copied to the initd locatl in the posgres container. 
* Make sure that the `5432` port is free for local and is not being used by another running postgres service on the host machine. 
* The service takes a bit of time to start since I added a heatlh check for postgres to run the db creation and avoid log error from the flask service (making calls to the DB before it being ready). 

## Test Calls:
The containerized service should be running on `http://127.0.0.1:80`, 5000 gunicorn port is mapped to port 80 locally. 
to test the service run these in the terminal:
* `$ curl "http://127.0.0.1:80/"` 👇🏼  
```
{
  "message": "Hello world!"
}
```


* `$ curl "http://127.0.0.1:80/rates?date_from=2021-01-01&date_to=2021-01-31&orig_code=CNGGZ&dest_code=EETLL"`
``` 
{
  "rates": [
    {
      "count": 3, 
      "day": "2021-01-31", 
      "price": 1154.3333333333333
    }, 
    {
      "count": 3, 
      "day": "2021-01-30", 
      "price": 1154.3333333333333
    },...
 ```

