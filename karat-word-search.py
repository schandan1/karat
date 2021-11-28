"""
After catching your classroom students cheating before, you realize your students are getting craftier and hiding words in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches, return any one.

grid1 = [
	['c', 'c', 'x', 't', 'i', 'b'],
	['c', 'c', 'a', 't', 'n', 'i'],
	['a', 'c', 'n', 'n', 't', 't'],
	['t', 'c', 's', 'i', 'p', 't'],
	['a', 'o', 'o', 'o', 'a', 'a'],
	['o', 'a', 'a', 'a', 'o', 'o'],
	['k', 'a', 'i', 'c', 'k', 'i'],
]
word1 = "catnip"
word2 = "cccc"
word3 = "s"
word4 = "bit"
word5 = "aoi"
word6 = "ki"
word7 = "aaa"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"

find_word_location(grid1, word1) => [ (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4) ]
find_word_location(grid1, word2) =>
       [(0, 1), (1, 1), (2, 1), (3, 1)]
    OR [(0, 0), (1, 0), (1, 1), (2, 1)]
    OR [(0, 0), (0, 1), (1, 1), (2, 1)]
    OR [(1, 0), (1, 1), (2, 1), (3, 1)]
find_word_location(grid1, word3) => [(3, 2)]
find_word_location(grid1, word4) => [(0, 5), (1, 5), (2, 5)]
find_word_location(grid1, word5) => [(4, 5), (5, 5), (6, 5)]
find_word_location(grid1, word6) => [(6, 4), (6, 5)]
find_word_location(grid1, word7) => [(5, 1), (5, 2), (5, 3)]
find_word_location(grid1, word8) => [(4, 1), (4, 2), (4, 3)]
find_word_location(grid2, word9) => [(0, 0)]

r = number of rows
c = number of columns
w = length of the word

"""

grid1 = [
    ['c', 'c', 'x', 't', 'i', 'b'],
    ['c', 'c', 'a', 't', 'n', 'i'],
    ['a', 'c', 'n', 'n', 't', 't'],
    ['t', 'c', 's', 'i', 'p', 't'],
    ['a', 'o', 'o', 'o', 'a', 'a'],
    ['o', 'a', 'a', 'a', 'o', 'o'],
    ['k', 'a', 'i', 'c', 'k', 'i']
]

word1 = "catnip"
word2 = "cccc"
word3 = "s"
word4 = "bit"
word5 = "aoi"
word6 = "ki"
word7 = "aaa"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"


def search_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])

    directions = [(0, 1), (1, 0)]  # right, below

    res = []
    visited = set()

    def dfs(i, j, index, path):
        # print(i,j,index, path, grid[i][j], word[index])
        if index == len(word) - 1:
            res.append(path + [[i, j]])
            return

        for x, y in directions:
            n_i = i + x
            n_j = j + y

            if 0 <= n_i < rows and 0 <= n_j < cols and grid[n_i][n_j] == word[index + 1]:
                # print(" in dfs of ", grid[i][j], " next is ", grid[n_i][n_j], word[index+1] )
                dfs(n_i, n_j, index + 1, path + [[i, j]])

        return path

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                p = dfs(i, j, 0, [])


    return res


print(search_word(grid2, word9))
word1 = "catnip"
word2 = "cccc"
word3 = "s"
word4 = "bit"
word5 = "aoi"
word6 = "ki"
word7 = "aaa"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"
# print(earch_word(grid1, word1))
#
# print(earch_word(grid1, word2))
#
# print(earch_word(grid1, word3))
# print(earch_word(grid1, word4))
# print(earch_word(grid1, word1))
# print(earch_word(grid1, word1))
# find_word_location(grid1, word1) => [ (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4) ]
# find_word_location(grid1, word2) =>
#        [(0, 1), (1, 1), (2, 1), (3, 1)]
#     OR [(0, 0), (1, 0), (1, 1), (2, 1)]
#     OR [(0, 0), (0, 1), (1, 1), (2, 1)]
#     OR [(1, 0), (1, 1), (2, 1), (3, 1)]
# find_word_location(grid1, word3) => [(3, 2)]
# find_word_location(grid1, word4) => [(0, 5), (1, 5), (2, 5)]
# find_word_location(grid1, word5) => [(4, 5), (5, 5), (6, 5)]
# find_word_location(grid1, word6) => [(6, 4), (6, 5)]
# find_word_location(grid1, word7) => [(5, 1), (5, 2), (5, 3)]
# find_word_location(grid1, word8) => [(4, 1), (4, 2), (4, 3)]
# find_word_location(grid2, word9) => [(0, 0)]