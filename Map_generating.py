import random

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создание экземпляра базовой модели
Base = declarative_base()

# Определение модели Map
class Map(Base):
    __tablename__ = 'map'  # Имя таблицы в базе данных
    id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
    type = Column(String)
    resource = Column(String)

# Создание соединения с базой данных
engine = create_engine("postgresql://kts_user:kts_pass@localhost/kts")


# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

grid = []
# Генерация и добавление рандомных записей
for i in range(10):
    grid.append([])
    for j in range(10):
        x = i
        y = j
        type = random.choice(["mount", "plain", "crater"])
        if type == "mount":
            grid[i].append(1)
            resource = random.choice(["stone", "gold", "copper"])
        elif type == "plain":
            grid[i].append(0)
            resource = random.choice(["clay", "stone", "copper"])
        else:
            grid[i].append(0)
            resource = random.choice(["silver", "stone", "gold"])

        new_map = Map(x=x, y=y, type=type, resource=resource)
        session.add(new_map)

# Завершение сессии
session.commit()
session.close()

print(grid)