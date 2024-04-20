from fastapi import FastAPI
from tensorflow.keras.models import load_model
import numpy as np
from pydantic import BaseModel
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load your trained model
model = load_model("my_lstm_model.h5")

# Initialize FastAPI app
app = FastAPI()


# Define a Pydantic model for input data
class RequestData(BaseModel):
    prices: list  # This will receive a list of last 'look_back' days' prices


# Define a Pydantic model for output data
class PredictedPrice(BaseModel):
    predicted_prices: list


# Endpoint to predict the next 30 days prices
@app.post("/predict", response_model=PredictedPrice)
async def predict(data: RequestData):
    # Scale the input prices as the model expects scaled data
    scaler = MinMaxScaler(feature_range=(0, 1))
    prices_scaled = scaler.fit_transform(np.array(data.prices).reshape(-1, 1))

    # Prepare the input in the form expected by the model
    prices_scaled = prices_scaled.reshape(1, -1, 1)

    # Initialize list for predictions
    predicted_prices = []

    # Predict next 30 days prices
    for _ in range(30):
        predicted_price = model.predict(prices_scaled)[0]
        predicted_prices.append(predicted_price)
        # Update the input for next prediction
        prices_scaled = np.append(prices_scaled[:, 1:, :], [[predicted_price]], axis=1)

    # Inverse transform to get original prices scale
    predicted_prices = scaler.inverse_transform(predicted_prices)

    return {"predicted_prices": predicted_prices.flatten().tolist()}
