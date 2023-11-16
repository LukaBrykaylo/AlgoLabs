from collections import deque


def gas_management(cities, gas, active_gas):
    adjacency_list = {}

    for connection in active_gas:
        if connection[0] not in adjacency_list:
            adjacency_list[connection[0]] = []
        adjacency_list[connection[0]].append(connection[1])

    final_results = []

    for storage in gas:
        unreached_cities = bfs(storage, adjacency_list, set(cities))
        if unreached_cities:
            final_results.append([storage, list(unreached_cities)])

    return final_results


def bfs(start, adjacency_list, all_cities):
    visited = set()
    queue = deque([start])
    unreached_cities = set(all_cities)

    while queue:
        current_city = queue.popleft()
        visited.add(current_city)
        unreached_cities.discard(current_city)

        if current_city in adjacency_list:
            for neighbor in adjacency_list[current_city]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    return unreached_cities
