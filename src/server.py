import inspect
import pathlib

from fastapi import FastAPI, Request
from .trigger import trigger_run
filename = inspect.getframeinfo(inspect.currentframe()).filename
BASE_DIR =  pathlib.Path(filename).resolve().parent

app = FastAPI()

@app.get("/") # HTTP GET
def read_root():
    return {"hello": "world", "parent": str(BASE_DIR)}

# @app.post('/') # HTTP POST
# def write_root():
#     return {"hello": "world", "parent": str(BASE_DIR)}


# /trigger/nbs/test.ipynb
# /trigger/nbs/scrape.ipynb
@app.get("/trigger/{filepath:path}")
def trigger_notebook(filepath, request:Request):
    # /Users/cfe/Dev/jupyter-api/src / nbs/scrape.ipynb
    params = dict(request.query_params)
    params["BASE_DIR"] = str(BASE_DIR)
    params["DATA_DIR"] = str(BASE_DIR / "data")
    input_path = BASE_DIR / pathlib.Path(filepath) #
    rs, output_path = None, None
    try:
        rs, output_path = trigger_run(input_path, params=params)
    except:
        pass
    return {"output_path": output_path}
