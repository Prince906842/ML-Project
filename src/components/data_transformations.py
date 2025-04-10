import sys 
from dataclasses import dataclass 
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder ,StandardScaler  
from sklearn.compose import ColumnTransformer 
from sklearn.impute import SimpleImputer 
from sklearn.pipeline import Pipeline 
from src.exception import CustomException  
from src.utils import save_object 
from src.logger import logging 
import os 

@dataclass  
class DataTransformationconfig: 
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")  


class DataTransformation: 
    def __init__(self):
         self.data_transformation_config = DataTransformationconfig() 

    def  get_data_transfromer_object(self): 
        """ 
        this fuction is responsible for data transformation
        """ 
        try: 
            numerical_columns = ["writing_score","reading_score"]
            categorical_columns = ["gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",]
            num_pipeline = Pipeline(steps=[
            ("imputer",SimpleImputer(strategy="median")), 
            ("scaler",StandardScaler())
            ]) 

            cat_pipeline = Pipeline(steps=[ 
                ("imputer",SimpleImputer(strategy="most_frequent")) ,
                 ("one_hot_encoder",OneHotEncoder()), 
                 ("scaler",StandardScaler(with_mean=False))
            ]) 

            logging.info(f"categorical_columns:{categorical_columns}") 
            logging.info(f"numerical_columns:{numerical_columns}") 

            preprocessor= ColumnTransformer([
                ("num_pipeline",num_pipeline ,numerical_columns ) ,
                ("cat_pipeline",cat_pipeline,categorical_columns)
            ]) 

            return preprocessor 
            
        except Exception as e : 
            raise CustomException(e,sys) 


    def initiate_data_transfromation(self,train_path,test_path):  
        try:
            train_df = pd.read_csv(train_path) 
            test_df = pd.read_csv(test_path ) 
             
            logging.info("Reading the train and test file") 

            preprocessing_obj = self.get_data_transfromer_object() 

            target_columns_name = "math_score"  
            numerical_columns = ["writing_score","reading_score"] 

            ## divide the train dataset to independent and dependent feature 
            input_features_train_df=train_df.drop(columns=[target_columns_name],axis=1) 
            target_features_train_df = train_df[target_columns_name] 

            ## divide the test dataset to independent and dependent feature 
            input_features_test_df=test_df.drop(columns=[target_columns_name],axis=1) 
            target_features_test_df = test_df[target_columns_name] 
 
            logging.info("Appying preprocessing on training and test dataframe") 

            input_features_train_arr = preprocessing_obj.fit_transform(input_features_train_df) 
            input_features_test_arr = preprocessing_obj.transform(input_features_test_df) 

            train_arr = np.c_[input_features_train_arr ,np.array(target_features_train_df)] 
            test_arr = np.c_[input_features_test_arr,np.array(target_features_test_df)]  

            logging.info(f"Saving preprocessing object")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return ( 
                train_arr,
                test_arr, 
                self.data_transformation_config.preprocessor_obj_file_path
            )
            
        except Exception as e: 
            raise CustomException(e,sys)
