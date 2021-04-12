import inspect
import pathlib

from fastapi import FastAPI

filename = inspect.getframeinfo(inspect.currentframe()).filename
BASE_DIR =  pathlib.Path(filename).resolve().parent

app = FastAPI()

@app.get("/") # HTTP GET
def read_root():
    return {"hello": "world", "parent": str(BASE_DIR)}

# @app.post('/') # HTTP POST
# def write_root():
#     return {"hello": "world", "parent": str(BASE_DIR)}