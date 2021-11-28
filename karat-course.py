import collections

student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]

student_course_pairs_2 = [
  ["42", "Software Design"],
  ["0", "Advanced Mechanics"],
  ["9", "Art History"],
]

def find_pairs(pairs):
    d = collections.defaultdict(set)
    for s, c in pairs:
        d[s].add(c)

    students = list(d.keys())
    print(students)
    res = collections.defaultdict(set)
    for i in range(len(students)):
        for j in range(i+1, len(students)):
            res[(students[i], students[j])] = d[students[i]].intersection(d[students[j]])
    print(res)


# find_pairs(student_course_pairs_2)


all_courses = [
    ["Logic","COBOL"],
    ["Data Structures","Algorithms"],
    ["Creative Writing","Data Structures"],
    ["Algorithms","COBOL"],
    ["Intro to Computer Science","Data Structures"],
    ["Logic","Compilers"],
    ["Data Structures","Logic"],
    ["Creative Writing","System Administration"],
    ["Databases","System Administration"],
    ["Creative Writing","Databases"]
]

some_courses = [
    ["Creative Writing","System Administration"],
    ["Databases","System Administration"],
    ["Creative Writing","Databases"]
]


def find_mid_paths(courses):
    indegree = collections.defaultdict(int)
    graph = collections.defaultdict(list)

    for a, b in courses:
        indegree[b] += 1
        indegree[a] += 0
        graph[a].append(b)

    res = []
    output = set()

    def dfs(src, path):
        if not graph[src]:
            res.append(path)
            output.add(path[((len(path)+1)//2)-1])

        for nei in graph[src]:
            dfs(nei, path + [nei])

    starting = [k for k in indegree if indegree[k] == 0]
    for node in starting:
        dfs(node, [node])
    return output, res

print(find_mid_paths(all_courses))
