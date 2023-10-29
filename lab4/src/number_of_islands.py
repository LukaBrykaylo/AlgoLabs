def number_of_islands(island_map):
    if not island_map:
        return 0
    number = 0
    for i in range(len(island_map)):
        for j in range(len(island_map[0])):
            if (island_map[i][j] == 1):
                number += 1
                dfs(i, j, island_map)
    return number


def dfs(i, j, island_map):
    if i < 0 or j < 0 or i >= len(island_map) or j >= len(island_map[0]) or island_map[i][j] == 0:
        return 0
    island_map[i][j] = 0

    dfs(i+1, j, island_map)
    dfs(i - 1, j, island_map)   
    dfs(i, j + 1, island_map)
    dfs(i, j - 1, island_map)
    dfs(i+1, j+1, island_map)
    dfs(i+1, j-1, island_map)
    dfs(i-1, j+1, island_map)
    dfs(i-1, j-1, island_map)
