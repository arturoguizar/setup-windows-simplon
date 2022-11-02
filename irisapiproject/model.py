# 1. Library imports
import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from pydantic import BaseModel
import joblib


# 2. Class which describes a single flower measurements
class IrisSpecies(BaseModel):
    sepal_length: float 
    sepal_width: float 
    petal_length: float 
    petal_width: float


# 3. Class for training the model and making predictions
class IrisModel:
    # 6. Class constructor, loads the dataset and loads the model
    #    if exists. If not, calls the _train_model method and 
    #    saves the model
    def __init__(self):
        self.df = load_iris()
        self.model_fname_ = 'iris_model.joblib'
        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model = self._train_model()
            joblib.dump(self.model, self.model_fname_)
        

    # 4. Perform model training using the RandomForest classifier
    def _train_model(self):
        X = self.df.drop('species', axis=1)
        y = self.df['species']
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=1, stratify=y)
        rfc = RandomForestClassifier()
        model = rfc.fit(X_train,y_train)
        return model


    # 5. Make a prediction based on the user-entered data
    #    Returns the predicted species with its respective probability
    def predict_species(self, sepal_length, sepal_width, petal_length, petal_width):
        data_in = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = self.model.predict(data_in)
        probability = self.model.predict_proba(data_in).max()
        return prediction[0], probability
