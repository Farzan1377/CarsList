# How to get it running

1. Open the command line and cd to this directory.

2. Create a virtual environment.
	
	On Unix:
	```
	python3 -m venv venv
	. venv/bin/activate
	```
	On Windows:
	```
	py -3 -m venv venv
	venv\Scripts\activate
	```

3. Install dependencies:
	```
	pip install Flask
	pip install MySQL
	pip install MySQL-connector
	```

4. Set environment variables and run. 
	
	On Unix:
	```
	export FLASK_APP=app
	export FLASK_ENV=development
	flask run
	```
  	On Windows:
	```
	set FLASK_APP=app
	set FLASK_ENV=development
	flask run
	```
	    
5. Open your internet browser and go to 'http://localhost:5000/shop/buy'.

Note: 
This application will not initialize the MySQL database. 
The MySQL database must be initialized with data beforehand.
Also note that the username and password are hardcoded in `app/db.py`

# How to get front-end of the application running
1. Cd into the frontend directory.
2. Run 'npm start'. The website should go live at http://localhost:3000/
Note: The front-end is not calling the backend APIs yet. The styling and API calls will be done in the following days.
