from fastapi import FastAPI

app = FastAPI()


@app.get("/say-hi")
def say_hi():
    return {"message": "hello from Titan Nodus!"}
