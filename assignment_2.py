
# Import os for using environment variables set from load_dotenv() below
import os

# Import sqlalchemy for DB connection
from sqlalchemy import create_engine

# Import dotenv for environment variables
from dotenv import load_dotenv
load_dotenv()

# Pandas
'''

This is a VERY powerful and very widely used library for organizing, managing,
and crunching data in Python!  We will be devoting an entire module to this!

'''
import pandas as pd

# Import requests for API call
import requests


'''

Whoops!  We're missing the function definition for this function call!

Can you please complete this function definition so the code beneath it will run when called below?

'''

# Complete Assignment two by finishing the function definition here!



    try:
        # connect to database
        engine = create_engine(f"postgresql://{os.getenv('db_user')}:{os.getenv('db_pass')}@{os.getenv('db_host')}:5432/{os.getenv('db_db')}")


        # collect 
        student_record = pd.read_sql("select cpt_username, cast(passkey as text) as passkey from cpt_program.week_two_keys",engine)

        if len(student_record) > 0:
            cpt_username = student_record.iloc[0]['cpt_username']
            passkey = student_record.iloc[0]['passkey']

            body = {
                'cpt_username': cpt_username,
                'class_code': 'CPT-127',
                'passkey': passkey
            }

            headers = {
                'Content-type':'application/json'
            }

            res = requests.post('http://192.168.2.51:5000/week_two',json=body,headers=headers)

            if res.status_code == 200:
                return "Congratulations, you're all done!"
            else:
                return f"Submission did not complete with code: {res.status_code}"
        else:
            return "No record found for your user!"

    except Exception as e:
        return f"Error on request: {e}"

    

message = complete_assignment_two()


print(message)