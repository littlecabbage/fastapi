from fastapi import FastAPI
from producer.producer import producer
from consumer.consumer import consumer

app = FastAPI()


app.include_router(producer, prefix="/producer", tags=["producer"])
app.include_router(consumer, prefix="/consumer", tags=["consumer"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000)
