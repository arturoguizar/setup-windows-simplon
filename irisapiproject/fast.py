# 1. Library imports
import uvicorn
from fastapi import FastAPI
import pickle
from model import IrisModel, IrisSpecies



# 2. Create the app object
app = FastAPI()
model = IrisModel()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, stranger'}


# 4. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted flower species with the confidence
@app.get('/predict')
def predict_species(iris: IrisSpecies):
    data = iris.dict()
    prediction, probability = model.predict_species(
        data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']
    )
    return {
        'prediction': prediction,
        'probability': probability
    }
# http://127.0.0.1:8000/predict?sepal+length+%28cm%29=148&sepal+width+%28cm%29=148&petal+length+%28cm%29=148&petal+width+%28cm%29=148


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
