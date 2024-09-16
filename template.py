import os 
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO)

project_name = "mlproject"

list_of_file = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/Data_injestion.py",
    f"src/{project_name}/components/Data_transformation.py",
    f"src/{project_name}/components/Model_trainer.py",
    f"src/{project_name}/components/Model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/Training_pipeline.py",
    f"src/{project_name}/pipelines/Prediction_pipeline.py",
    f"src/{project_name}/Exception.py",
    f"src/{project_name}/Logger.py",
    "app.py",
    'setup.py',
    'requirements.txt',
   'Dockerfile'


]


for filepath in list_of_file:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok= True)
        logging.info(f"creating directory{filedir} for file: {filename} ")

    if(not os.path.exists(filepath) or os.path.getsize(filepath)==0):
        with open (filepath,'w')  as file :
            pass
            logging.info(f"creating the file : {filename}")

    else:
        logging.info(f"the file already exists : {filename}")


