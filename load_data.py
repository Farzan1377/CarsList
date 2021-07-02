import pandas as pd
import sqlalchemy
import pymysql

"""userData.csv and vehiclesWithUserAdded.csv need to be copied into the root cs348/ directory for this load script 
to work"""

USER = '<Enter MySQL username>'
PASSWORD = '<Enter MySQL password>'

CREATE_USER_TABLE = "CREATE TABLE users (" \
                    "user_id VARCHAR(255) NOT NULL, " \
                    "name VARCHAR(255), " \
                    "username VARCHAR(255), " \
                    "password VARCHAR(255), " \
                    "location VARCHAR(255), " \
                    "email VARCHAR(255), " \
                    "phone VARCHAR(255), " \
                    "picture VARCHAR(255), " \
                    "PRIMARY KEY (user_id));"

CREATE_VEHICLE_TABLE = "CREATE TABLE vehicles (" \
                       "vehicle_id VARCHAR(255) NOT NULL, " \
                       "user_id VARCHAR(255) NOT NULL, " \
                       "manufacturer VARCHAR(255), " \
                       "model VARCHAR(255), " \
                       "year INT, " \
                       "type VARCHAR(255), " \
                       "vehicle_condition VARCHAR(255), " \
                       "odometer INT, " \
                       "paint_color VARCHAR(255), " \
                       "image_url VARCHAR(255), " \
                       "description TEXT, " \
                       "PRIMARY KEY (vehicle_id), " \
                       "FOREIGN KEY (user_id) REFERENCES users(user_id)" \
                       ");"

CREATE_POST_TABLE = "CREATE TABLE posts (" \
                    "post_id INT NOT NULL, " \
                    "user_id VARCHAR(255) NOT NULL, " \
                    "vehicle_id VARCHAR(255) NOT NULL, " \
                    "price INT, " \
                    "date_created VARCHAR(255), " \
                    "date_expires VARCHAR(255), " \
                    "PRIMARY KEY (post_id), " \
                    "FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id), " \
                    "FOREIGN KEY (user_id) REFERENCES users(user_id)" \
                    ");"

print("Connecting to MySQL...")
engine = sqlalchemy.create_engine('mysql+pymysql://' + USER + ':' + PASSWORD + '@localhost')

print("Creating database...")
engine.execute("DROP DATABASE IF EXISTS CS348")
engine.execute("CREATE DATABASE CS348")
engine.execute("USE CS348")

print("Creating tables...")
engine.execute(CREATE_USER_TABLE)
engine.execute(CREATE_VEHICLE_TABLE)
engine.execute(CREATE_POST_TABLE)

print("Loading users...")
users_df = pd.read_csv('userData.csv',
                       usecols=['name.first', 'name.last', 'location.street.number', 'location.street.name',
                                'location.city', 'location.state', 'location.country', 'email', 'login.uuid',
                                'login.username', 'login.password', 'phone', 'picture.medium'])
users_df.dropna(inplace=True)
users_df['name'] = users_df['name.first'] + ' ' + users_df['name.last']
del users_df['name.first']
del users_df['name.last']
users_df['location'] = users_df['location.street.number'].astype(str) + ' ' + users_df['location.street.name']
users_df['location'] = users_df[['location', 'location.city', 'location.state', 'location.country']].agg(', '.join,
                                                                                                         axis=1)
del users_df['location.street.number']
del users_df['location.street.name']
del users_df['location.city']
del users_df['location.state']
del users_df['location.country']
users_df.rename(columns={'login.uuid': 'user_id', 'login.username': 'username', 'login.password': 'password',
                         'picture.medium': 'picture'},
                inplace=True)
users_df.to_sql(name='users', con=engine, schema='cs348', if_exists='append', index=False)

print("Loading vehicles...")
vehicles_df = pd.read_csv('vehiclesWithUserAdded.csv',
                          usecols=['id', 'login.uuid', 'year', 'manufacturer', 'model', 'condition', 'odometer', 'type',
                                   'paint_color', 'image_url', 'description'])
vehicles_df.dropna(inplace=True)
vehicles_df.rename(columns={'id': 'vehicle_id', 'login.uuid': 'user_id', 'condition': 'vehicle_condition'},
                   inplace=True)
vehicles_df.to_sql(name='vehicles', con=engine, schema='cs348', if_exists='append', index=False)

print("Load complete!")
