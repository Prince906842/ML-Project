from src.logger import logging 
from src.exception import CustomException 
import sys 

if __name__=="__main__": 
    logging.info("the execution has started") 

    try:
        pass
    except Exception as e: 
         logging.info("Custom Exception") 
         raise CustomException(e,sys)