# https://note.nkmk.me/en/python-list-initialize/

# Initialize a list:
l = [0] * 10
print(l)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(list(range(3)))
# [0, 1, 2]

# Notes on initializing a 2D list (list of lists)


# initialize a list multiple times: n * list
# explains: https://stackoverflow.com/questions/18946728/changing-an-element-in-one-list-changes-multiple-lists
l_2d_ng = [[0] * 4] * 3
print(l_2d_ng)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# If you update one list, all the lists will be changed.
l_2d_ng[0][0] = 5
print(l_2d_ng)
# [[5, 0, 0, 0], [5, 0, 0, 0], [5, 0, 0, 0]]

l_2d_ng[0].append(100)
print(l_2d_ng)
# [[5, 0, 0, 0, 100], [5, 0, 0, 0, 100], [5, 0, 0, 0, 100]]
# This is because the inner lists are all the same object.

print(id(l_2d_ng[0]) == id(l_2d_ng[1]) == id(l_2d_ng[2]))
# True


# To initialize independent inner lists : comprehensions: [expression for variable_name in iterable]

l_2d_ok = [[0] * 4 for i in range(3)]
print(l_2d_ok)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Each inner list is treated as a different object.
l_2d_ok[0][0] = 100
print(l_2d_ok)
# [[100, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

print(id(l_2d_ok[0]) == id(l_2d_ok[1]) == id(l_2d_ok[2]))
# False


# List comprehensions with if [expression for variable_name in iterable if condition]
odds = [i for i in range(10) if i % 2 == 1]
print(odds)
# [1, 3, 5, 7, 9]

# initilaze a list of int and list of list:
q = deque([0]) # list of int
newq = deque()
newq.append([0]) # list of list

# 2D matrix: list[list[int]]:
grid = [[0,0,0],[1,1,0],[1,1,0]]
rows, columns = len(grid), len(grid[0])
# if the cell is (x,y), then 8 directions:(x, y+1), (x, y-1), (x+1, y), (x-1, y), (x+1, y+1), (x+1, y-1),(x-1, y+1), (x-1, y-1)
directions = [(0, 1), (0, -1), (1, 1), (-1, 1), (1, 0), (-1, 0), (1, 1), ()]