import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def train_model():
    # Beispiel-Daten
    X = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])
    y = np.array([0.5, 0.6, 0.7])

    # Modell erstellen
    model = Sequential([
        Dense(10, input_shape=(3,), activation='relu'),
        Dense(1, activation='linear'),
    ])

    # Modell kompilieren und trainieren
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=10)

    # Modell speichern
    model.save("model.h5")

if __name__ == "__main__":
    train_model()
