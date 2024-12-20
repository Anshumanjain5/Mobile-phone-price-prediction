from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import sys
import os
from DataTranformation import DataTransformation
from dataclasses import dataclass

# Adding project directory to the sys path for import resolution
sys.path.append(r"C:\Users\anshuman\Desktop\Mobile Price Prediction\src")

from logger.logger import logging
from logger.exception import CustomError
from utilities.SaveObject import save_object
from utilities.ModelTrainer import model_trainer

@dataclass
class ModelTrainerConfig:
    """
    Configuration class for Model Trainer, including the path where the trained model will be saved.
    """
    model_path: str = os.path.join(os.getcwd(), "artifacts", "model.pkl")

class ModelTrainer:
    """
    This class is responsible for training models, evaluating their performance, 
    and saving the best-performing model.
    """
    def __init__(self):
        self.config = ModelTrainerConfig().model_path
    
    def train_model(self, X_train, X_test, y_train, y_test):
        """
        This method trains multiple models, evaluates their performance, 
        and saves the best model.
        
        Args:
            train (array-like): Training data (features and target).
            test (array-like): Test data (features and target).

        Returns:
            float: The best score (mean cross-validation score) of the best-performing model.
        """
        # Splitting the training and testing data into features (X) and target (y)
        # Defining a dictionary of models to train
        models = {
            "Linear Regression": LinearRegression(),
            "Logistic Regression": LogisticRegression(),
            "KNeighborsRegressor": KNeighborsRegressor(),
            "SVC": SVC(),
            "DecisionTreeClassifier": DecisionTreeClassifier(),
            "XGBRegressor": XGBRegressor(),
            "CatBoostRegressor": CatBoostRegressor(),
            "RandomForestRegressor": RandomForestRegressor(),
        }

        # Training the models and selecting the best model based on cross-validation score
        best_model, best_score, name = model_trainer(models, X_train, y_train, X_test, y_test)
        
        # Logging the best model and its score
        logging.info(f"Best Model: {best_model}, Best Score: {best_score}")

        # Saving the best model to the specified path
        save_object(best_model, self.config)
        logging.info(f"Model saved successfully at {self.config}")

        y_prediction = best_model.predict(X_test)

        r2_square = r2_score(y_test, y_prediction)
        
        return best_score,r2_square,name

if __name__ == "__main__":
    # Load the data
    data_transformation = DataTransformation()
    x_train_set,x_test_set,y_train_set,y_test_set = data_transformation.transform_data()
    
    # Create an instance of ModelTrainer
    evaluate_models = ModelTrainer()
    
    # Train the model and evaluate its performance
    best_score,r2_square,name = evaluate_models.train_model(x_train_set,x_test_set,y_train_set,y_test_set)
    print(f"Model:{name}\nBest score: {best_score}")
    logging.info(f"Best Model Score: {best_score}")
