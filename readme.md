# URL Shortener Service
**Tech Stack:** Python, Flask, Postgresql as well as Some HTML and CSS.  
**Deployment:** The application is deployed on heroku with the help of postgresql database provided by heroku.  
**Main File:** server.py - Contains all the routes for the api. Get for Index, Post for Shortening URL, Get for Resolving URL.    

**Util:** 
1. Shortener.py -> Contains Logic for Shortening the URL
2. Models.py -> Contains the Model for the DB and functions that transacte with the Postgres Database.
3. Db and Log.py -> Db.py instantiates the DB and log.py is a Custom Logger Class used by all the services. The logs are stored in logs/my.log.   

**Procfile:** Used to configure how the application will be started on heroku.   

**Link to the Deployed Version of the applicstion:**  
https://tinnieurl.herokuapp.com/

## Running the Application

### [Optional] - Create a virtual environment

`pip install virtualenv`
`virtualenv env`

Activate the Env  
Windows : `source env/scripts/activate`  
Mac : `source env/scripts/activate`  
Linux : `source env/scripts/activate`

### Main Steps (Virtual Env Optional)- Install all the Dependecies

`pip install -r requirement.txt`

### Run the Application

` python server.py`
