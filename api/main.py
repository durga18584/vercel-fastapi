import uvicorn
from fastapi import FastAPI
import time
app = FastAPI()

@app.get("/test")
def test():
    timer_duration = 20
    time.sleep(timer_duration)
    return {"hello world": "bye"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)