# Text justification

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        result, current_line, num_letters = [], [], 0
        for word in words:
            if num_letters + len(word) + len(current_line) > maxWidth:
                # need to justify
                # spaces to distribute between words
                size = max(1, len(current_line) - 1)
                # how many spaces?
                for i in range(maxWidth - num_letters):
                    index = i % size
                    current_line[index] += "-"
                # add to result
                result.append("-".join(current_line))
                current_line, num_letters = [], 0
            current_line.append(word)
            num_letters += len(word)

        result.append("-".join(current_line) + "-" * (maxWidth - num_letters - len(current_line) + 1))

        return result


    # d = defaultdict(int)
    # for cpdomain in cpdomains:
    #     cnt, domain = cpdomain.split(' ')
    #     d[domain] += int(cnt)
    #     while '.' in domain:
    #         part, domain = domain.split('.', 1)
    #         d[domain] += int(cnt)
    # return [f"{value} {key}" for key, value in d.items()]

# n1 = len(nums1)
# n2 = len(nums2)
# dp = [[0 for _ in range(n1 + 1)] for _ in range(n2 + 1)]
#
# res = -1
# for i in range(1, n2+1):
#     for j in range(1, n1+1):
#         if nums2[i-1] == nums1[j-1]:
#             dp[i][j] = 1 + dp[i-1][j-1]
#             res = max(res, dp[i][j])

def findHistory(user1, user2):
    result  = []

    if user1 == user2:
        return user1

    for i in range(len(user1)):
        index1 = i
        curResult = []
        if user1[i] in user2:
            index2 = user2.index(user1[i])
            while index1 < len(user1) and index2 < len(user2) and user1[index1] == user2[index2]:
                curResult.append(user1[index1])
                index1 += 1
                index2 += 1
                if len(curResult) > len(result):
                    result = curResult
    return result


s = s.replace(" ", "")
current_op = "+"
stack = []
num = 0

for i in range(len(s)):
    if s[i].isdigit():
        num = 10 * num + ord(s[i]) - ord('0')
    if not s[i].isdigit() or i == len(s) - 1:
        if current_op == "+":
            stack.append(num)
        elif current_op == "-":
            stack.append(-num)
        elif current_op == "*":
            stack.append(stack.pop() * num)
        elif current_op == "/":
            stack.append(int(stack.pop() / num))

        num = 0
        current_op = s[i]

return sum(stack)

# sign = 1
# res = 0
# num = 0
# stack = []
#
# for ch in s:
#     if ch.isdigit():
#         num = num * 10 + int(ch)
#     elif ch in {'+', '-'}:
#         res += sign * num
#         sign = 1 if ch == "+" else -1
#         num = 0
#     elif ch == '(':
#         stack.append(res)
#         stack.append(sign)
#         sign = 1
#         res = 0
#     elif ch == ")":
#         res += sign * num
#         res = res * stack.pop()
#         res += stack.pop()
#         num = 0
#
# res += sign * num
# return res

# word search

class Solution:
    def exist(self, board, word: str) -> bool:
        if not board and not word:
            return True
        if not board or not word:
            return False
        rows = len(board)
        cols = len(board[0])

        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def dfs(i, j, index):
            if index == len(word) - 1:
                return True

            found = False
            temp = board[i][j]
            board[i][j] = "#"  # to avoid visited array
            for x, y in directions:
                n_i = i + x
                n_j = j + y
                if 0 <= n_i < len(board) and 0 <= n_j < len(board[0]) and board[n_i][n_j] == word[index + 1]:
                    if dfs(n_i, n_j, index + 1):
                        found = True
                        break

            board[i][j] = temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        print(board)
                        return True

        return False

#snake game
def findPassableLanes(straight_board):
    rows = []
    cols = []

    for i in range(len(straight_board)):
        row_flag = True
        for j in range(len(straight_board[i])):
            if straight_board[i][j] == '+':
                row_flag = False
                break

        if row_flag:
            rows.append(i)

    for j in range(len(straight_board[0])):
        col_flag = True
        for i in range(len(straight_board)):
            if straight_board[i][j] == '+':
                col_flag = False
                break

        if col_flag:
            cols.append(j)

    return (rows, cols)

from collections import deque
def findExit(board, start): # BFS, don't update the board in place to reuse it.
    m, n = len(board), len(board[0])
    vis, (i, j) = [[0] * n for _ in range(m)], start
    vis[i][j], q = 1,  deque([start])
    while q:
        i, j = q.popleft()
        for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
            if m > x >= 0 <= y < n and not vis[x][y] and not board[x][y]:
                if x in (0, m - 1) or y in (0, n - 1):
                    return x, y
                vis[x][y] = 1
                q.append((x, y))

