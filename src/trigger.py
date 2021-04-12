import pathlib
import papermill as pm

def trigger_run(notebook_filepath, params={}, id=None, output_path=None):
    '''
    Trigger the notebook filepath
    '''
    input_path = pathlib.Path(notebook_filepath)
    if not input_path.exists():
        return []
    if output_path is None:
        fname = input_path.stem
        suffix = input_path.suffix
        output_dir = input_path.parent / "outputs"
        output_dir.mkdir(parents=True, exist_ok=True)   
        output_path = output_dir /  f"{fname}-output{suffix}"
    rs = pm.execute_notebook(
        input_path,
        output_path,
        parameters={"id": id, **params}
    )
    return rs, output_path