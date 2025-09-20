from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/add")
def add(x , y):
    return float(x) + float(y)

@app.get("/sub")
def sub(x, y):
    return float(x) - float(y)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
