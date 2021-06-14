# URL Shortener Service
**Tech Stack:** Python, Flask, Postgresql as well as Some HTML and CSS.  
**Deployment:** The application is deployed on heroku with the help of postgresql database provided by heroku.  
**Main File:** server.py --> Contains all the routes -> Index, Post for Shortening URL, Get for Resolving URL        
**Util:** 
1. Shortener.py -> Contains Logic for the Shortening the URL
2. Models.py -> Contains Model for the DB and transactions with the Postgres Database.
3. Db and Log.py -> Db.py instantiates the DB and log.py is a Custom Logger Class Used by all the services. The logs are store in logs/my.log.   

**Procfile:** Used to configure how the application will be started on heroku.   

**Link to the Deployed Version of the applicstion:**  
https://tinnieurl.herokuapp.com/

## Running the Application

### [Optional] - Create a virtual environment

`python -m venv tinnieUrl`

Activate the Env  
Windows : `./tinnieUrl/Scripts/activate`  
Mac : `source ./tinnieUrl/bin/activate`  
Linux : `source ./tinnieUrl/bin/activate`

### Main Steps (Virtual Env Optional)- Install all the Dependecies

`pip install -r requirement.txt`

### Run the Application

` python server.py`
