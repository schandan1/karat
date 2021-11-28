parentChildPairs = [(1, 3), (2, 3), (3, 6), (5, 6),
                   (5, 7), (4, 5), (4, 8), (8, 10)]

#part 1
"""
Write a function that takes this data as input and returns two collections: 
one containing all individuals with zero known parents, and one containing all 
individuals with exactly one known parent.

"""
from collections import defaultdict

def part1(pairs):
    d = defaultdict(int)
    for p, c in pairs:
        d[c] += 1
        d[p] += 0

    print(d)
    empty = []
    one = []
    for k,v in d.items():
        if v == 0:
            empty.append(k)
        if v == 1:
            one.append(k)
    return empty, one
# empty, one = part1(parentChildPairs)
# print(empty, one)


"""
Pt.2 Write a function that takes the graph, as well as two of the individuals in our dataset, 
as its inputs and returns true if and only if they share at least one ancestor.
"""


def part2(pairs, n1, n2):
    p1 = set()
    p2 = set()

    def find_parents(c1, parents):
        for p, c in pairs:
            if c == c1:
                parents.add(p)
                find_parents(p, parents)
    find_parents(n1, p1)
    find_parents(n2, p2)
    return len(p1.intersection(p2)) > 0

# print(part2(parentChildPairs, 3, 8))
# print(part2(parentChildPairs, 5, 8))
# print(part2(parentChildPairs, 6, 8))
# print(part2(parentChildPairs, 1, 3))

"""
Write a function that, for a given individual in our dataset, returns their earliest known ancestor -- 
the one at the farthest distance from the input individual.  
If there is more than one ancestor tied for "earliest", return any one of them. 
If the input individual has no parents, the function should return null (or -1). Sample input and output:

"""


def part3(pairs, n1):
    p1 = defaultdict(list)

    def find_parents(c1, depth):
        for p, c in pairs:
            if c == c1:
                p1[depth+1].append(p)
                find_parents(p, depth+1)

    find_parents(n1, 0)

    return p1[max(p1.keys())] if len(p1) > 0 else -1

parent_child_pairs = [ (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 10), (11, 2) ]

print(part3(parent_child_pairs, 8))
print(part3(parent_child_pairs, 7))
print(part3(parent_child_pairs, 6))
print(part3(parent_child_pairs, 1))