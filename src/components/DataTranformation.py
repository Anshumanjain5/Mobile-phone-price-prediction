from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from dataclasses import dataclass
import sys
import os

# Add project directory to the system path
sys.path.append(r"C:\Users\anshuman\Desktop\Mobile Price Prediction\src")

from logger.logger import logging
from logger.exception import CustomError
from utilities.SaveObject import save_object
from DataIngestion import DataIngestion

@dataclass
class DataTransformationConfig:
    """
    Configuration class for data transformation.
    Stores the path for the preprocessor object.
    """
    preprocessor: str = os.path.join(os.getcwd(), "artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        """
        Initializes the DataTransformation class.
        Ingests the training and testing data.
        """
        logging.info("Initializing Data Transformation...")
        self.train, self.test = DataIngestion().ingest_data()

    def get_preprocessor(self):
        """
        Creates and returns a data preprocessing pipeline.
        Currently includes only scaling.
        """
        logging.info("Loading preprocessor...")
        preprocessor = Pipeline(steps=[
            ("scaler", StandardScaler())
        ])
        logging.info("Preprocessor loaded successfully.")
        return preprocessor

    def transform_data(self):
        """
        Transforms the data by applying the preprocessing pipeline.
        Saves the preprocessor and returns the transformed datasets.
        """
        try:
            target_column = "price_range"
            logging.info("Starting data transformation process...")

            # Initialize and prepare the preprocessor
            preprocessor = self.get_preprocessor()
            logging.info(f"Dropping target column '{target_column}' from datasets...")
            self.train_ = self.train.drop(target_column, axis=1)
            self.test_ = self.test.drop(target_column, axis=1)

            logging.info("Fitting the preprocessor on training data...")
            preprocessor.fit(self.train_)
            logging.info("Preprocessor fitted successfully.")

            # Save the preprocessor object
            logging.info("Saving the preprocessor object...")
            save_object(preprocessor, DataTransformationConfig.preprocessor)

            # Transform train and test datasets
            logging.info("Transforming training dataset...")
            self.train_arr = preprocessor.transform(self.train_)

            logging.info("Transforming testing dataset...")
            self.test_arr = preprocessor.transform(self.test_)

            # Combine transformed data with the target column
            logging.info("Combining transformed data with target column...")
            self.train_set = np.c_[self.train_arr, self.train[target_column]]
            self.test_set = np.c_[self.test_arr, self.test[target_column]]

            logging.info("Data transformation process completed successfully.")
            return self.train_set, self.test_set

        except Exception as e:
            error_msg = CustomError(e, sys)
            logging.error(f"An error occurred during data transformation: {error_msg}")
            raise error_msg


if __name__ == '__main__':
    try:
        logging.info("Starting the data transformation script...")
        transformer = DataTransformation()
        train_set, test_set = transformer.transform_data()
        logging.info("Data transformation script completed successfully.")
    except Exception as e:
        logging.error(f"Script terminated due to an error: {e}")
