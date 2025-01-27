

'''

Welcome to week 2!

In order for these assignments to work you will need to install three libraries:

- python-dotenv
- sql alchemy
- pandas

You can install these by opening a terminal on your Linux VM and running:

sudo apt-get install python3-dotenv
sudo apt-get install python3-sqlalchemy
sudo apt-get install python3-pandas

You will be prompted to install these (please enter 'Y') when prompted.  

Once those have been installed and you have created/filled-out your .env file then this program should run!

Please make sure it runs successfully before moving on to assignment_2.py!

'''

# This imports Operating system (os) functions
import os


#sqlalchemy is a VERY common Database Object-relational mapper (ORM) for Python
# # We are using the create_engine function to connect to a PostgreSQL database! 
from sqlalchemy import create_engine

# dotenv is the Python-instantiation of a popular ".env" library in JavaScript
# we are using the load_dotenv function to pull in the environment variables defined in the .env file!
from dotenv import load_dotenv
load_dotenv()

# Pandas is  a really useful data manipulation library
import pandas as pd


'''

See!  Before we even get to the code we are already importing 
functions from commonly used libraries which we will be using!

'''

# connect to database

'''
This creates an "engine" variable which is a live connection to the PostgreSQL database with the parameters
outlined in the .env file in this directory!  We will be reviewing "securing" these .env files at some point but 
please note one of the most common ways to do this you have already seen - by not committing it to GitHub!

This is why you were required to pull the .env file out of Discord!
'''
engine = create_engine(f"postgresql://{os.getenv('db_user')}:{os.getenv('db_pass')}@{os.getenv('db_host')}:5432/{os.getenv('db_db')}")

'''

If you see the following print statement in your terminal window after running this script
you have successfully connected to the database and are all set with assignment one!

'''

students = pd.read_sql('select * from cpt_program.week_two_keys',engine)


print('Database connected successfully')