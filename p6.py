import sys

def nearest_neighbor_tsp(distances):
    num_cities = len(distances)
    tour = [0]  
    visited = set([0])  
    current_city = 0
    total_distance = 0

    while len(visited) < num_cities:
        nearest_city = None
        min_distance = sys.maxsize

        for next_city in range(num_cities):
            if next_city not in visited and distances[current_city][next_city] < min_distance:
                nearest_city = next_city
                min_distance = distances[current_city][next_city]

        tour.append(nearest_city)
        visited.add(nearest_city)
        total_distance += min_distance
        current_city = nearest_city

    tour.append(0)
    total_distance += distances[current_city][0]

    return tour, total_distance

if __name__ == "__main__":
    distances = [[0, 4, 8, 9, 12], 
                 [4, 0, 6, 8, 9], 
                 [8, 6, 0, 10, 11], 
                 [9, 8, 10, 0, 7], 
                 [12, 9, 11, 7, 0]]

    tour, total_distance = nearest_neighbor_tsp(distances)
    print("Nearest Neighbor TSP Tour:", tour)