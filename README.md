### Step 1: Set Up Your Environment

First, ensure you have the necessary libraries installed. You'll need FastAPI and Uvicorn, a lightning-fast ASGI server to run your FastAPI app. You can install them using pip:

```bash
pip install fastapi uvicorn
```

### Step 2: Run Your Server

To run your FastAPI application, use Uvicorn. You can start your server with the following command:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

Sample input:
```bash
{
  "prices": [9264.32, 9258.11, 9313.86, 9357.47, 9390.85, 9432.93, 9450.70, 9468.45, 9429.32, 9400.86, 9371.13, 9350.29, 9301.91, 9351.77, 9377.01, 9360.88, 9325.96, 9304.97, 9283.83, 9277.97, 9300.92, 9335.87, 9358.59, 9367.19, 9380.92, 9402.48, 9417.71, 9431.85, 9452.37, 9473.57, 9487.64, 9502.38, 9522.73, 9511.85, 9490.32, 9472.39, 9461.06, 9442.29, 9428.15, 9410.24, 9392.03, 9371.93, 9350.45, 9328.64, 9306.83, 9284.72, 9261.95, 9240.85, 9220.34, 9200.11, 9180.05, 9160.48, 9141.05, 9122.22, 9104.19, 9086.94, 9069.78, 9053.42, 9037.64, 9022.57]
}
```

Sample Request:
````bash
curl -X POST "http://localhost:8000/predict" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"prices\":[9264.32, 9258.11, 9313.86, 9357.47, 9390.85, 9432.93, 9450.70, 9468.45, 9429.32, 9400.86, 9371.13, 9350.29, 9301.91, 9351.77, 9377.01, 9360.88, 9325.96, 9304.97, 9283.83, 9277.97, 9300.92, 9335.87, 9358.59, 9367.19, 9380.92, 9402.48, 9417.71, 9431.85, 9452.37, 9473.57, 9487.64, 9502.38, 9522.73, 9511.85, 9490.32, 9472.39, 9461.06, 9442.29, 9428.15, 9410.24, 9392.03, 9371.93, 9350.45, 9328.64, 9306.83, 9284.72, 9261.95, 9240.85, 9220.34, 9200.11, 9180.05, 9160.48, 9141.05, 9122.22, 9104.19, 9086.94, 9069.78, 9053.42, 9037.64, 9022.57]}"
```

This command tells Uvicorn to run the app object in the `app.py` file, listen on all interfaces (`--host 0.0.0.0`), use port 8000, and reload the server automatically when code changes are detected (`--reload`).

### Step 3: Test Your API

Once your server is running, you can test your API endpoint using tools like cURL, Postman, or directly from a browser (for GET requests). To test the `/predict` endpoint, you need to send a POST request with JSON data that includes the last `look_back` days' prices.

### Step 4: Secure and Deploy

Before deploying to production, ensure your API is secure and robust. Consider adding error handling, validation, logging, and possibly authentication to protect your API.

This setup gives you a basic FastAPI server that can predict the next 30 days of Bitcoin prices based on the last `look_back` days of input prices using your LSTM model. Adjustments may be needed based on your specific model setup and deployment environment.