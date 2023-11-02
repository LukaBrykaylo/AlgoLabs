from collections import deque


def number_of_islands(island_map):
    if not island_map:
        return 0
    
    num_islands = 0

    for i in range(len(island_map)):
        for j in range(len(island_map[0])):
            if island_map[i][j] == 1:
                num_islands += 1
                bfs(i, j, island_map)

    return num_islands


def bfs(i, j, island_map):
    queue = deque()
    queue.append((i, j))
    island_map[i][j] = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]

    while queue:
        x, y = queue.popleft()

        for dirx, diry in directions:
            upd_x, upd_y = x + dirx, y + diry
            if 0 <= upd_x < len(island_map) and 0 <= upd_y < len(island_map[0]) and island_map[upd_x][upd_y] == 1:
                queue.append((upd_x, upd_y))
                island_map[upd_x][upd_y] = 0
