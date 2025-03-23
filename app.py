from src.logger import logging 
from src.exception import CustomException 
from src.components.data_ingestions import DataIngestion 
from src.components.data_ingestions import DataIngestionConfig  
from src.components.data_transformations import DataTransformationconfig,DataTransformation  

import sys


if __name__=="__main__": 
    logging.info("the execution has started") 

    try:
        data_ingestion = DataIngestion() 
        train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()  

        data_transformation = DataTransformation() 
        data_transformation.initiate_data_transfromation(train_data_path,test_data_path) 

    except Exception as e: 
         logging.info("Custom Exception") 
         raise CustomException(e,sys)