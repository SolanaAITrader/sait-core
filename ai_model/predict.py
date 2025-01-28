import numpy as np
from tensorflow.keras.models import load_model

class Predictor:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def predict(self, input_data):
        prediction = self.model.predict(input_data)
        return prediction[0][0]

# Beispiel: Verwendung des Modells
if __name__ == "__main__":
    predictor = Predictor("model.h5")
    input_data = np.array([[0.5, 0.3, 0.2]])  # Beispiel-Daten
    print("Predicted Price:", predictor.predict(input_data))
