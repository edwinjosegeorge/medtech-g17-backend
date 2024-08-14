from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

from controllers import forcast_drug
app = FastAPI()


# Define the input model
class ForecastDrugRequest(BaseModel):
    drug_name: str
    forecast_until_date: date


@app.post("/forecast", response_model=dict)
def get_drug_names(request: ForecastDrugRequest):
    return forcast_drug(
        drug_name=request.drug_name,
        end_date=request.forecast_until_date
    )
## curl -X POST "http://127.0.0.1:8000/forecast" -H "Content-Type: application/json" -d '{"drug_name": "Aspirin", "forecast_date": "2024-08-20"}'
