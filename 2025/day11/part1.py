# input_file = "./inputs/test.txt"
input_file = "./inputs/day11.txt"


def read_servers(fp: str):
    # adjacency list
    servers = {}
    with open(fp) as f:
        for line in f:
            line = line.strip()
            node, out = line.split(": ")
            out = out.split(" ")
            servers[node] = out
    return servers


def count_paths(servers: dict[str, list[str]]) -> int:
    print("counting paths")

    # map node to number of paths to out
    node_to_paths = {}
    goal = "out"

    def dfs(node: str, parents: set[str]):
        # base case
        if node == goal:
            return 1

        # detect cycle
        if node in parents:
            return -1

        # get memoized paths
        if node_to_paths.get(node, None):
            return node_to_paths.get(node)

        child_nodes = servers[node]
        paths = 0
        for child_node in child_nodes:
            parents.add(node)
            child_paths = dfs(child_node, parents)
            parents.remove(node)
            if child_paths != -1:
                paths += child_paths

        node_to_paths[node] = paths
        return paths

    return dfs("you", set())


servers = read_servers(input_file)
paths = count_paths(servers)

print("paths: ", paths)
