from fastapi import FastAPI

app = FastAPI()


@app.get("/say-hi")
def say_hi():
    return {"message": "hi from Titan Nodus!"}
