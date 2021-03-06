# Installation

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

Note: 
This application will not initialize the MySQL database. 
The MySQL database must be initialized with data beforehand.
Also note that the username and password are hardcoded in `app/db.py`

# How to get front-end of the application running
1. Cd into the frontend directory.
2. Run 'npm start'. The website should go live at http://localhost:3000/
Note: The front-end is not calling the backend APIs yet. The styling and API calls will be done in the following days.

# Initializing the Database

1. In the load_data.py file, add your mysql username and password to the corresponding fields.
2. Run the file by using the command python3 load_data.py.
	- This file will generate database called CS348 and also the user, post and vehicle tables. These tables will be populated with data as well.
	- Ensure that userData.csv and vehiclesWithUserAdded.csv are in the same directory.
3. Run the SQL commands contained in the file insert_posts.sql to initialize the posts table.


# Features implemented so far

There are a total of 9 features implemented so far. A user will be able to create, edit, delete and modify a vehicle; the backend code can be found in `app/vehicles.py`. A user will be able to create, edit, and delete a post as well; the related backend code can be found in `app/posts.py`. A user will be able to find the average price of vehicles made by a manufacturer and a user will also be able to filter through posts based on price and manufacturer as well; the backend code can be found in `app/search.py`. For ease of testing, an endpoint can be specifically be tested running the Python code in the `Python HTTP Requests for Testing` folder while the Flask server is running (Step 4 in the Installation). Alternatively, an HTTP request can be sent to http://localhost:5000/{specifc_endpoint_found_in_file} while the Flask server is running. In the future, the front-end will be integrated with the back-end.
