from src.logger import logging 
from src.exception import CustomException 
import sys  
from src.components.data_ingestions import DataIngestion 
from src.components.data_ingestions import DataIngestionConfig 

if __name__=="__main__": 
    logging.info("the execution has started") 

    try:
        data_ingestion = DataIngestion() 
        train_data_path,test_data_path = data_ingestion.initiate_data_ingestion() 
    except Exception as e: 
         logging.info("Custom Exception") 
         raise CustomException(e,sys)