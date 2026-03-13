import joblib
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Load trained IDS model
model = joblib.load("model/ids_pipeline.pkl")

def predict(features):
    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)
    probability = model.predict_proba(features)

    return prediction[0], probability.max()