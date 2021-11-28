import collections

paths = [
["A", "B"],
["A", "C"],
["B", "K"],
["C", "K"],
["E", "L"],
["F", "G"],
["J", "M"],
["E", "F"],
["G", "H"],
["G", "I"],
["C", "G"]
]


def find_path(paths):
    d = collections.defaultdict(list)
    indegree = collections.defaultdict(int)

    for src, dst in paths:
        d[src].append(dst)
        indegree[dst] += 1
        indegree[src] += 0

    staring_nodes = [key for key in indegree if indegree[key]==0]

    res = collections.defaultdict(set)

    def dfs(node,  parent):
        if not d[node]:
            res[parent].add(node)

        for nei in d[node]:
            dfs(nei, parent)

    for node in staring_nodes:
        dfs(node, node)

    return res

print(find_path(paths))