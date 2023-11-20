import json

import aiohttp

import app.web.app
from app.drone.search_path import astar
import asyncio
from asyncio import Task
from aiohttp import web

class DroneObject:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.status = "Stoped"
        self.moving_to = [0, 0]
        self.is_moving = False

    async def move_to(self, x, y):

        grid = [
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
            [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 0, 1, 0]
        ]

        self.moving_to = [x, y]
        path = astar(grid,[self.x, self.y], self.moving_to)
        if path:
            self.is_moving = True
            print(f'До цели {len(path)} секунд полёта! Отправляюсь.')
            for i in range(len(path)):
                self.x = path[i][0]
                self.y = path[i][1]
                print(f'Сейчас я в точке {[self.x, self.y]} !!!')

                await self.send_data_to_center(self.x, self.y)

                await asyncio.sleep(2)

            print(f'Я прибыл в точку {self.moving_to}')

            await self.send_data_to_center(self.x, self.y)
            self.is_moving = False
            return f'Я прибыл в точку {self.moving_to}'
        else:
            print(f"Не могу добраться до точки {[x,y]}")
            return f"Не могу добраться до точки {[x,y]}"


    def where_am_i(self):
        return [self.x, self.y]


    async def send_data_to_center(self, x, y):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url="http://192.168.68.74:8080/station.listen",
                                        json={
                                            "x": x,
                                            "y": y
                                        }
                                        ) as resp:
                    response = await resp.text()
                    data = json.loads(response)['data']
                    print(data)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    web.run_app(app)

