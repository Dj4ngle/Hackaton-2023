import typing

import aiohttp
from sqlalchemy import select, text

from app.map.models import Map, MapModel
from app.base.base_accessor import BaseAccessor

from app.web.app import drone




class MapAccessor(BaseAccessor):
    async def get_all_map(self) -> list[Map]:
        async with self.app.database.session() as session:

            res = await session.execute(text("Select id, x, y, type from map;"))
            return res.fetchall()

    async def get_cell(self):
        if drone.is_moving:
            return None
        async with self.app.database.session() as session:
            res = await session.execute(select(MapModel)
                                        .where(MapModel.x == drone.x, MapModel.y == drone.y))
            return res.scalars().first()


    async def move_to(self, x:int, y:int):
        if drone.x == x and drone.y == y:
            return f"Я уже и так в точке {[x,y]}!"
        status = await drone.move_to(x, y)
        return status

    async def where_am_i(self):
        return drone.where_am_i()

