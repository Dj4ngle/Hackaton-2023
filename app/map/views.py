from app.drone.drone import DroneObject
from app.map.schemes import MapListSchema, MapSchema
from app.web.app import View
from app.web.utils import json_response


class MapGetView(View):
    async def get(self):
        maps = await self.store.maps.get_all_map()
        return json_response(data=MapListSchema().dump({"maps": maps}))

class CellGetView(View):
    async def get(self):

        cell = await self.store.maps.get_cell()
        if cell == None:
             return json_response(data="Дрон в полёте!!!")
        return json_response(data=MapSchema().dump(cell))

class GetDronePositionVeiw(View):
    async def get(self):
        position = await self.store.maps.where_am_i()
        return json_response(data=position)

class MoveDroneVeiw(View):
    async def post(self):
        request_data = await self.request.json()

        x = request_data["x"]
        y = request_data["y"]
        message = await self.store.maps.move_to(x, y)
        return json_response(data=message)