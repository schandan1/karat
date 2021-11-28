import collections

input = [
["cook", "eat"],
["study", "eat"],
["sleep", "study"]]

#output (steps of a workflow):
# {{"sleep", "cook"},
# {"study"},
# {"eat"}}

graph = collections.defaultdict(list)
child_to_par = collections.defaultdict(list)
outdegree = collections.defaultdict(int)

for child, parent in input:
    graph[parent].append(child)
    outdegree[parent] += 1
    outdegree[child] += 0
    child_to_par[child].append(parent)


print(outdegree)
print(child_to_par)

q = collections.deque()
for item in outdegree:
    if outdegree[item] == 0:
        q.append(item)
        outdegree[item] -= 1
print(q)
print(outdegree)

res = []
while q:
    temp = []
    for _ in range(len(q)):
        node = q.popleft()
        temp.append(node)
        for parent in child_to_par[node]:
            outdegree[parent] -= 1
            if outdegree[parent] == 0:
                q.append(parent)
    res.append(temp)

print(res)





