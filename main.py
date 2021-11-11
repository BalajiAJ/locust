from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    x = 0
    for i in range(1,90000000):
        x = x+1
        x = x-1
    return {"message": "Hello World"}