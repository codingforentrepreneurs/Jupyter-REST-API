#!/bin/bash

/usr/local/bin/uvicorn src.server:app --port $PORT --host 0.0.0.0