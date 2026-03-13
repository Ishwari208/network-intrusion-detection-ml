import joblib

model = joblib.load("model/ids_pipeline.pkl")

print(type(model))
print(model)
