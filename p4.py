import heapq

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def parse_graph_input():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    
    for _ in range(num_edges):
        u, v, cost = input("Enter an edge (format: u v cost): ").split()
        cost = float(cost)
        
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        
        graph[u].append((v, cost))
    
    return graph

def ao_star_search(start_state, goal_state, graph):
    frontier = []
    heapq.heappush(frontier, Node(start_state, None, None, 0, heuristic(start_state, goal_state)))
    explored = {}

    while frontier:
        current_node = heapq.heappop(frontier)
        current_state = current_node.state

        if current_state == goal_state:
            path = []
            while current_node.parent is not None:
                path.append((current_node.action, current_node.state))
                current_node = current_node.parent
            path.reverse()
            return path

        if current_state not in explored or current_node.cost < explored[current_state]:
            explored[current_state] = current_node.cost
            for neighbor, step_cost in graph.get(current_state, []):
                new_cost = current_node.cost + step_cost
                new_node = Node(neighbor, current_node, f"Move to {neighbor}", new_cost, heuristic(neighbor, goal_state))
                heapq.heappush(frontier, new_node)
    
    return None

def heuristic(state, goal_state):
    heuristic_values = {'A': 5, 'B': 3, 'C': 2, 'D': 1, 'E': 2, 'G': 0}
    return heuristic_values.get(state, float('inf'))

if __name__ == "__main__":
    print("Define the graph:")
    graph = parse_graph_input()
    
    start_state = input("Enter the start state: ")
    goal_state = input("Enter the goal state: ")

    path = ao_star_search(start_state, goal_state, graph)

    if path:
        print("Path found:")
        for action, state in path:
            print(f"Action: {action}, State: {state}")
    else:
        print("No path found.")