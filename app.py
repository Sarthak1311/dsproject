import os 
import sys
from src.mlproject.Exception import CustomException
from src.mlproject.Logger import logging
from src.mlproject.components.Data_injestion import DataIngestion
from src.mlproject.components.Data_injestion import DataIngestoinConfig
from src.mlproject.components.Data_transformation import DataTransformation,DataTransformationConfig
import pandas as pd


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        data_ingestion =DataIngestion()
        train_data_path ,test_data_path = data_ingestion.initiate_data_ingestion()
        # data_transformation_config = DataTransformationConfig()
        data_transforamtion = DataTransformation()
        data_transforamtion.initiate_data_transormation(train_data_path,test_data_path)




    except Exception as e:
        logging. info("Custom Exception")
        raise CustomException (e, sys)