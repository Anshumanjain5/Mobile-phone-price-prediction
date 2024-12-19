from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import os
import sys
sys.path.append(r"C:\Users\anshuman\Desktop\Mobile Price Prediction\src")
from logger.logger import logging
from logger.exception import CustomError
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_path:str = os.path.join(os.getcwd(),"data","data.csv")

class  DataIngestion:
    def __init__(self):
        self.train_path = DataIngestionConfig().train_path
    
    def ingest_data(self):
        try:
            self.data = pd.read_csv(self.train_path)
            train,test = train_test_split(self.data,test_size=0.2)
            logging.info(f"Train data size: {len(train)}, Test data size: {len(test)}")
            train_set,test_set = pd.DataFrame(train,columns=self.data.columns), pd.DataFrame(test,columns=self.data.columns)
            return (train_set,test_set)
        except Exception as e:
            error = CustomError(e,sys)
            logging.error(error)
            raise error

    