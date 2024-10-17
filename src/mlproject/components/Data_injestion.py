import os 
import sys
from src.mlproject.Exception import CustomException
from src.mlproject.Logger import logging
from src.mlproject.utils import read_sql_data
import pandas  as pd
from sklearn.model_selection import train_test_split


from dataclasses import dataclass

@dataclass
class DataIngestoinConfig():
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","raw.csv")


class DataIngestion():

    def __init__(self):
        self.data_ingestion_config = DataIngestoinConfig()
    

    def initiate_data_ingestion(self):
        logging.info("Initiating data injestion phase")
        try:
            df =pd.read_csv(os.path.join('notebook/data','raw.csv'))
            logging.info("started reading the sql data")
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)

            train_set,test_set =train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data Ingestion in completed")
             
            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )

            
        except Exception as e :
            logging.info(f"ERROR occured{e}")
            raise CustomException(e,sys)