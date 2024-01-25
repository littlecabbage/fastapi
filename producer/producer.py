from fastapi import APIRouter
import pandas as pd


producer = APIRouter()


path = "/Users/mac/fastapi/fake_data.csv"
data_iter = pd.read_csv(path, index_col=0, parse_dates=True, chunksize=1)


# 生产者路由
@producer.get("/")
def producer_home():
    return {"message": "Welcome to the producer page!"}


@producer.get("/get_records/")
def get_data():
    return next(data_iter).to_json(orient="split")
