def is_valid(grid):
    n = len(grid)
    row_set = [set() for _ in range(n)]
    col_set = [set() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            num = grid[i][j]
            if num < 1 or num > n or num in row_set[i] or num in col_set[j]:
                return False
            else:
                row_set[i].add(num)
                col_set[j].add(num)
    return True

def validateNonogram(matrix, row, col):
    rowFlag = False
    colFlag = False

    for i in range(len(matrix)):
        list = []
        count = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'B':
                count += 1
            elif count > 0:
                list.append(count)
                count = 0

        if count > 0:
            list.append(count)

        if row[i] != list:
            return False

    rowFlag = True

    for i in range(len(matrix[0])):
        list = []
        count = 0
        for j in range(len(matrix)):
            if matrix[j][i] == 'B':
                count += 1
            elif count > 0:
                list.append(count)
                count = 0

        if count > 0:
            list.append(count)

        if col[i] != list:
            return False

    colFlag = True

    return rowFlag and colFlag