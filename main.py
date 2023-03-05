from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World", "var": 123}

@app.get("/get-current-time")
async def get_current_time():
    return {"message": "Current time is 12pm"}