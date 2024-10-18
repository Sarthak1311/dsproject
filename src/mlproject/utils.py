import os 
import sys
from src.mlproject.Exception import CustomException
from src.mlproject.Logger import logging
import pandas as pd

from dotenv import load_dotenv
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import pymysql

import numpy as np
import pickle


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
    
def save_object(file_path,obj):
    dir_name = os.path.dirname(file_path)
    os.makedirs(dir_name,exist_ok=True)

    with open(file_path,'wb') as file_obj:
        pickle.dump(obj,file_obj)



def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
