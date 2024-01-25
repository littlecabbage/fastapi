from fastapi import APIRouter
import requests
import json 
import pandas as pd 

consumer = APIRouter()

@consumer.get("/")
def root():
    return {"message": "Hello World"}

@consumer.get("/from_producer/")
def get_from_producer():
    url = "http://localhost:8000/producer/get_records"
    # get json from url
    response = requests.get(url)
    json_res = response.json()
    res = json.loads(json_res)
    print(pd.to_datetime(res['index'], unit='ms'))
    return res['index']