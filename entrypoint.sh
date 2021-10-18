#!/bin/bash

RUN_PORT=${PORT:-8087}

/opt/venv/bin/gunicorn src.main:app --worker-tmp-dir /dev/shm --workers 5 -k uvicorn.workers.UvicornWorker --worker-connections=1000 --timeout 2400 --bind "0.0.0.0:${RUN_PORT}"
