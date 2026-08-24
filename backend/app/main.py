from fastapi import FastAPI

app = FastAPI(title="MindSpace API")


@app.get("/")
def root():
    return {"message": "Welcome to MindSpace"}