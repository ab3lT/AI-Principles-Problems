from collections import deque

def has_cycle(graph):
    """
    Detects a cycle in a directed graph using Depth First Search (DFS).

    Parameters:
    graph (dict): A dictionary representing the adjacency list of the graph.

    Returns:
    bool: True if there is a cycle in the graph, False otherwise.

    Approach:
    - Use DFS to traverse the graph.
    - Maintain a visited set to track visited nodes.
    - Use a recursion stack to detect back edges, which indicate a cycle.
    """
    def dfs(node, visited, rec_stack):
        # Mark the current node as visited
        visited[node] = True
        rec_stack[node] = True
        
        # Visit all neighbors
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:  # If the neighbor is not visited, recurse
                if dfs(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:  # If the neighbor is in the recursion stack, a cycle is detected
                return True

        # Remove the node from the recursion stack before returning
        rec_stack[node] = False
        return False

    visited = {node: False for node in graph}
    rec_stack = {node: False for node in graph}

    for node in graph:
        if not visited[node]:  # If the node is not yet visited, start DFS
            if dfs(node, visited, rec_stack):
                return True
    return False


def has_cycle_kahns(graph):
    """
    Detects a cycle in a directed graph using Kahn's Algorithm (Topological Sort).

    Parameters:
    graph (dict): A dictionary representing the adjacency list of the graph.

    Returns:
    bool: True if there is a cycle in the graph, False otherwise.

    Approach:
    - Calculate the in-degree (number of incoming edges) of each node.
    - Use a queue to process nodes with in-degree 0.
    - Remove processed nodes and update the in-degree of their neighbors.
    - If any nodes remain unprocessed (non-zero in-degree), a cycle exists.
    """
    # Step 1: Calculate in-degrees of all nodes
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Step 2: Collect nodes with in-degree 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])

    # Step 3: Process the queue
    count = 0  # Count of processed nodes
    while queue:
        current = queue.popleft()
        count += 1
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check if all nodes are processed
    if count != len(graph):
        return True  # There is a cycle
    return False  # No cycle


def main():
    """
    Main function to demonstrate cycle detection in directed graphs
    using DFS and Kahn's Algorithm.
    """
    # Example graph with a cycle
    graph_with_cycle = {
        0: [1],
        1: [2],
        2: [3],
        3: [0]
    }

    # Example graph without a cycle
    graph_without_cycle = {
        0: [1],
        1: [2],
        2: [3],
        3: []
    }

    print("Using DFS Algorithm:")
    print(f"Graph with cycle: {has_cycle(graph_with_cycle)}")  # Output: True
    print(f"Graph without cycle: {has_cycle(graph_without_cycle)}")  # Output: False

    print("\nUsing Kahn's Algorithm:")
    print(f"Graph with cycle: {has_cycle_kahns(graph_with_cycle)}")  # Output: True
    print(f"Graph without cycle: {has_cycle_kahns(graph_without_cycle)}")  # Output: False


if __name__ == "__main__":
    main()
