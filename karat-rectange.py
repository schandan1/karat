grid = [ [0, 0, 0, 0, 1],
         [0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0] ]

def part1(grid):
    found = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] == 1:
                print(i, j)
                start_row, start_col = i, j
                i += 1
                while i < len(grid) and grid[i][j] == 1:
                    i += 1
                i -= 1
                end_row = i
                j += 1
                while j < len(grid[0]) and grid[i][j] == 1:
                    j += 1
                j -= 1
                end_col = j
                found = True
            if found:
                break
    return [start_row, start_col, end_row, end_col]

#print(part1(grid))


def part2(grid):
    res = []
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if (i, j) in visited:
                    continue
                start_row, start_col = i, j
                i += 1
                while i < len(grid) and grid[i][j] == 1:
                    i += 1
                i -= 1
                end_row = i
                j += 1
                while j < len(grid[0]) and grid[i][j] == 1:
                    j += 1
                j -= 1
                end_col = j
                for k in range(start_row, end_row+1):
                    for l in range(start_col, end_col+1):
                        visited.add((k,l))
                res.append([start_row, start_col, end_row, end_col])

    return res

grid2 = [ [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 1, 1, 0],
         [0, 1, 0, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 1, 0, 0],
         [0, 0, 0, 1, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0] ]
print(part2(grid2))
