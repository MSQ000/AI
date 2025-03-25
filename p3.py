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
        cost = int(cost)
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    return graph


def astar_search(start_state, goal_test, successors, heuristic):
    frontier = []
    heapq.heappush(frontier, Node(start_state, None, None, 0, heuristic(start_state)))
    explored = set()

    while frontier:
        current_node = heapq.heappop(frontier)
        current_state = current_node.state

        if goal_test(current_state):
            path = []
            while current_node.parent is not None:
                path.append((current_node.action, current_node.state))
                current_node = current_node.parent
            path.reverse()
            return path

        explored.add(current_state)

        for action, successor_state, step_cost in successors(current_state):
            if successor_state not in explored:
                new_cost = current_node.cost + step_cost
                new_node = Node(successor_state, current_node, action, new_cost, heuristic(successor_state))
                heapq.heappush(frontier, new_node)

    return None


if __name__ == "__main__":
    print("Define the graph:")
    graph = parse_graph_input()

    start_state = input("Enter the start state: ")
    goal_state = input("Enter the goal state: ")

    def goal_test(state):
        return state == goal_state

    def successors(state):
        successors_list = []
        for neighbor, cost in graph.get(state, []):
            action = f"Move to {neighbor}"
            successor_state = neighbor
            step_cost = cost
            successors_list.append((action, successor_state, step_cost))
        return successors_list

    def heuristic(state):
        heuristic_values = {key: abs(ord(key) - ord(goal_state)) for key in graph.keys()}
        return heuristic_values.get(state, float('inf'))

    path = astar_search(start_state, goal_test, successors, heuristic)

    if path:
        print("Path found:")
        for action, state in path:
            print(f"Action: {action}, State: {state}")
    else:
        print("No path found.")
