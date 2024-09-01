from fastapi import FastAPI

from pydantic import BaseModel

from model import convert, predict


app = FastAPI()


class StockIn(BaseModel):
    ticker: str


class StockOut(StockIn):
    forecast: dict

@app.post("/predict", response_model=StockOut, status_code=200)
def get_prediction(payload: StockIn):
    ticker = payload.ticker

    prediction_list = predict(ticker)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"ticker": ticker, "forecast": convert(prediction_list)}
    return response_object

### test endpoint for window: curl --header "Content-Type: application/json" --request POST --data "{\"ticker\":\"MSFT\"}" http://localhost:8008/predict
### test endpoint for linux/mac: curl --header "Content-Type: application/json" --request POST --data '{"ticker":"MSFT"}' http://localhost:8008/predict
### test endpoint for heroku app: curl --header "Content-Type: application/json" --request POST --data "{\"ticker\":\"MSFT\"}" https://<YOUR_HEROKU_APP_NAME>.herokuapp.com/predict
### test endpoint for heroku app: curl --header "Content-Type: application/json" --request POST --data "{\"ticker\":\"MSFT\"}" https://aqueous-wildwood-97407.herokuapp.com/predict