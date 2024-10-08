import os 
import sys
from src.mlproject.Exception import CustomException
from src.mlproject.Logger import logging
import pandas as pd

from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("database")

def read_sql_data():

    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        logging.info("connection stablish: %s", mydb)
        query = "select * from student"
        df = pd.read_sql_query(query,mydb)
        return df


    except Exception as e:
        logging.info(f"ERROR occured{e}")
        raise CustomException(e,sys)

