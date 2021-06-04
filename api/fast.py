from datetime import datetime
import pytz
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from TaxiFareModel.data import *
import joblib
import csv
from Flashcard.dummy_csv import *

PATH_TO_LOCAL_MODEL = 'model.joblib'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"greeting": "Hello world"}


@app.get("/random")
def random():
    return random_keyword()


@app.get("/predict")
def predict(pickup_datetime, pickup_longitude, pickup_latitude,
            dropoff_longitude, dropoff_latitude, passenger_count):
    # localize the user datetime with NYC timezone
    # create a datetime object from the user provided datetime
    pickup_datetime = "2021-05-30 10:12:00"
    pickup_datetime = datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")

    eastern = pytz.timezone("US/Eastern")
    localized_pickup_datetime = eastern.localize(pickup_datetime, is_dst=None)

    utc_pickup_datetime = localized_pickup_datetime.astimezone(pytz.utc)
    formatted_pickup_datetime = utc_pickup_datetime.strftime(
        "%Y-%m-%d %H:%M:%S UTC")

    X_test_dic = {
        "key": ["2013-07-06 17:18:00.000000119"],
        "pickup_datetime": [formatted_pickup_datetime],
        "pickup_longitude": [pickup_longitude],
        "pickup_latitude": [pickup_latitude],
        "dropoff_longitude": [dropoff_longitude],
        "dropoff_latitude": [dropoff_latitude],
        "passenger_count": [passenger_count]
    }

    df_test = pd.DataFrame.from_dict(X_test_dic)
    pipeline = joblib.load(PATH_TO_LOCAL_MODEL)
    y_pred = pipeline.predict(df_test)
    predicted_fare = y_pred
    #df = get_data_from_gcp()
    #df = clean_data(df)

    response = {
      "prediction": predicted_fare[0]
    }

    return response
