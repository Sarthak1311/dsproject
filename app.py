import os 
import sys
from src.mlproject.Exception import CustomException
from src.mlproject.Logger import logging
from src.mlproject.components.Data_injestion import DataIngestion
from src.mlproject.components.Data_injestion import DataIngestoinConfig
import pandas as pd


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        data_ingestion =DataIngestion()
        data_ingestion.initiate_data_ingestion()


    except Exception as e:
        logging. info("Custom Exception")
        raise CustomException (e, sys)