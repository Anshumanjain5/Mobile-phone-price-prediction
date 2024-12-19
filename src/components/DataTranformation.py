from sklearn.pipeline import Pipeline
import pandas as pd
from dataclasses import dataclass
import sys
import os
sys.path.append(r"C:\Users\anshuman\Desktop\Mobile Price Prediction\src")
from logger.logger import logging
from logger.exception import CustomError
from utilities.SaveObject import save_object
from sklearn.preprocessing import StandardScaler
from DataIngestion import DataIngestion
import numpy as np

@dataclass
class DataTransformationConfig:
    preprocessor = os.path.join(os.getcwd(),"artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.train,self.test = DataIngestion().ingest_data()
    
    def get_preprocessor(self):
        logging.info("Loading preprocessor...")
        preprocessor = Pipeline(steps=[
            ("scaler",StandardScaler())
        ])
        logging.info("Preprocessor loaded successfully.")
        return preprocessor
    
    def transform_data(self):
        try:
            target_column = "price_range"
            logging.info("Transforming data...")
            preprocessor = self.get_preprocessor()
            self.train_ = self.train.drop(target_column,axis=1)
            self.test_ = self.test.drop(target_column,axis=1)
            logging.info("Preparing the preprocessor")
            preprocessor.fit(self.train_)
            logging.info("Preprocessor prepared successfully.")
            save_object(preprocessor,DataTransformationConfig.preprocessor)
            self.train_arr = preprocessor.transform(self.train_)
            self.test_arr = preprocessor.transform(self.test_)
            self.train_set = np.c_[self.train_arr,self.train[target_column]]
            self.test_set = np.c_[self.test_arr,self.test[target_column]]
            logging.info("Data transformation completed successfully.")
            return self.train_set,self.test_set
        except Exception as e:
            error_msg = CustomError(e,sys)
            logging.error(error_msg)
            raise error_msg
    
if __name__ == '__main__':
    transformer = DataTransformation()
    transformer.transform_data()
    