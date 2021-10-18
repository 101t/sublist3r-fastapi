FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10


COPY ./app ./app/src
COPY requirements.txt /app/requirements.txt
COPY ./entrypoint.sh ./app/entrypoint.sh

WORKDIR /app

RUN chmod +x entrypoint.sh

RUN python3 -m venv /opt/venv && /opt/venv/bin/python -m pip install -r requirements.txt

CMD [ "./entrypoint.sh" ]
