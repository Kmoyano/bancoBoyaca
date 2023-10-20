import os

import uvicorn
from fastapi import FastAPI, APIRouter, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

STATIC_PATH = os.path.abspath(os.path.join(os.getcwd(), "view/static"))
print(STATIC_PATH)

class Control:
    def __init__(self):
        self.app = FastAPI()
        self.router = APIRouter()


    def routers(self):
        pass

    # Don't modify this code only routers
    def web_config(self):
        self.app.mount(
            "/static",
            StaticFiles(directory=STATIC_PATH),
            name="static"
        )
        self.routers()
        self.app.include_router(self.router)

    def run(self):
        self.web_config()
        uvicorn.run(self.app, host="127.0.0.1", port=5000)