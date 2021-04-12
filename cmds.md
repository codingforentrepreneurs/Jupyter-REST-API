
### Running FastAPI server via uvicorn
```
uvicorn src.server:app --reload
```

### Running Papermill via cli

*basic*
```
papermill in.ipynb out.ipynb
```

*with params*
```
papermill in.ipynb out.ipynb -p hello "world" abc 123
```