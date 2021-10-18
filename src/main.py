from fastapi import APIRouter, Depends
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI

from . import backend

TITLE = "Sublist3r API Service"
VERSION = "1.0.0"

app = FastAPI(title=TITLE)
app.include_router(backend.router)


@app.get("/")
def health_check():
	global VERSION
	return {"version": VERSION}


def custom_openapi():
	global VERSION, TITLE
	if app.openapi_schema:
		return app.openapi_schema
	openapi_schema = get_openapi(
		title=TITLE,
		version=VERSION,
		description="Descriont goes here",
		routes=app.routes,
	)
	openapi_schema["info"]["x-logo"] = {
		"url": ""
	}
	app.openapi_schema = openapi_schema
	return app.openapi_schema

app.openapi = custom_openapi
