from typing import Optional

from aiohttp.web import (
    Application as AiohttpApplication,
    Request as AiohttpRequest,
    View as AiohttpView,
)

from app.drone.drone import DroneObject
from app.map.models import Map
from app.store import Store, setup_store
from app.store.database.database import Database
from app.web.logger import setup_logging
from app.web.routes import setup_routes


class Application(AiohttpApplication):
    store: Optional[Store] = None
    database: Optional[Database] = None


class Request(AiohttpRequest):
    map: Optional[Map] = None

    @property
    def app(self) -> Application:
        return super().app()


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request

    @property
    def database(self):
        return self.request.app.database

    @property
    def store(self) -> Store:
        return self.request.app.store

    @property
    def data(self) -> dict:
        return self.request.get("data", {})


app = Application()
drone = DroneObject()

def setup_app() -> Application:
    setup_logging(app)
    setup_routes(app)
    setup_store(app)
    return app
