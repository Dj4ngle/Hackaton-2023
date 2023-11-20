import typing
from app.map.views import MapGetView, CellGetView, GetDronePositionVeiw, MoveDroneVeiw

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application"):

    app.router.add_view("/map.get_all", MapGetView)
    app.router.add_view("/map.get_cell", CellGetView)
    app.router.add_view("/drone.get_position", GetDronePositionVeiw)
    app.router.add_view("/drone.move", MoveDroneVeiw)
