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


def dfs(node: str, goal: str, servers: dict[str, list[str]]) -> int:
    node_to_paths = {}

    def _dfs(node: str, parents: set):
        # base case
        if node == goal:
            # print("found goal")
            return 1

        # detect cycle
        if node in parents:
            return -1

        # get memoized paths
        if node_to_paths.get(node, None) is not None:
            return node_to_paths.get(node)

        child_nodes = servers.get(node, [])
        paths = 0
        for child_node in child_nodes:
            parents.add(node)
            child_paths = _dfs(child_node, parents)
            parents.remove(node)
            if child_paths != -1:
                paths += child_paths

        node_to_paths[node] = paths
        return paths

    return _dfs(node, set())


def count_paths(servers: dict[str, list[str]]) -> int:
    print("counting paths")

    return (
        dfs("svr", "dac", servers)
        * dfs("dac", "fft", servers)
        * dfs("fft", "out", servers)
    ) + (
        dfs("svr", "fft", servers)
        * dfs("fft", "dac", servers)
        * dfs("dac", "out", servers)
    )


servers = read_servers(input_file)
paths = count_paths(servers)

print("paths: ", paths)
