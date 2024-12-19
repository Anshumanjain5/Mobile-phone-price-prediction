from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import os
import sys
from dataclasses import dataclass

# Adding the project directory to the system path
sys.path.append(r"C:\Users\anshuman\Desktop\Mobile Price Prediction\src")

from logger.logger import logging
from logger.exception import CustomError

@dataclass
class DataIngestionConfig:
    """
    Configuration class for data ingestion.
    Stores the path to the dataset.
    """
    train_path: str = os.path.join(os.getcwd(), "data", "data.csv")


class DataIngestion:
    def __init__(self):
        """
        Initializes the DataIngestion class with the dataset path.
        """
        logging.info("Initializing Data Ingestion...")
        self.train_path = DataIngestionConfig().train_path

    def ingest_data(self):
        """
        Reads the dataset, splits it into training and testing sets,
        and returns the resulting DataFrames.
        """
        try:
            logging.info(f"Reading dataset from: {self.train_path}")
            self.data = pd.read_csv(self.train_path)

            logging.info("Splitting data into training and testing sets...")
            train, test = train_test_split(self.data, test_size=0.2, random_state=42)
            logging.info(f"Train data size: {len(train)}, Test data size: {len(test)}")

            # Ensure train and test sets retain the original column structure
            train_set = pd.DataFrame(train, columns=self.data.columns)
            test_set = pd.DataFrame(test, columns=self.data.columns)

            logging.info("Data ingestion completed successfully.")
            return train_set, test_set

        except Exception as e:
            error = CustomError(e, sys)
            logging.error(f"An error occurred during data ingestion: {error}")
            raise error
