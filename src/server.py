import inspect
import json
import pathlib

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
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


@app.get("/output/{filepath:path}")
def output_notebook(filepath, request:Request):
    input_path = BASE_DIR / pathlib.Path(filepath) #
    fname = input_path.stem
    suffix = input_path.suffix
    output_dir = input_path.parent / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)   
    output_path = output_dir /  f"{fname}-output{suffix}"
    if not output_path.exists():
        return {}
    data = json.loads(output_path.read_text())
    return data


@app.get("/events/{filepath:path}")
def output_events(filepath, request:Request):
    input_path = BASE_DIR / pathlib.Path(filepath) #
    fname = input_path.stem
    suffix = input_path.suffix
    output_dir = input_path.parent / "outputs"
    stdout_path = output_dir / f"{fname}-stdout"
    if not stdout_path.exists():
        return []
    return StreamingResponse(open(stdout_path, 'rb'))
