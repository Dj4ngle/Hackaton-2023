import heapq

class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = 0  # Расстояние от начальной точки
        self.h = 0  # Эвристическое расстояние до конечной точки
        self.f = 0  # Общая стоимость (g + h)

    def __lt__(self, other):
        return self.f < other.f

def astar(grid, start, end):
    open_list = []
    closed_list = set()

    start_node = Node(start[0], start[1])
    end_node = Node(end[0], end[1])

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.x == end_node.x and current_node.y == end_node.y:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]

        closed_list.add((current_node.x, current_node.y))

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                new_x, new_y = current_node.x + dx, current_node.y + dy
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0:
                    if (new_x, new_y) not in closed_list:
                        new_node = Node(new_x, new_y, current_node)
                        new_node.g = current_node.g + 1
                        new_node.h = abs(new_x - end_node.x) + abs(new_y - end_node.y)
                        new_node.f = new_node.g + new_node.h

                        for node in open_list:
                            if node.x == new_x and node.y == new_y and node.f < new_node.f:
                                break
                        else:
                            heapq.heappush(open_list, new_node)

    return None

# Пример использования:
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = astar(grid, start, end)
if path:
    print("Путь найден:", path)
else:
    print("Путь не найден")
