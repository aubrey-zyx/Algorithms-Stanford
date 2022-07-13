"""
You are given an n by n grid of distinct numbers. A number is a local minimum if it is smaller than all of its neighbors.
(A neighbor of a number is one immediately above, below, to the left, or the right. Most numbers have four neighbors;
numbers on the side have three; the four corners have two.)
Use the divide-and-conquer algorithm design paradigm to compute a local minimum with only O(n) comparisons between pairs of numbers.
(Note: since there are n*n numbers in the input, you cannot afford to look at all of them.
Hint: Think about what types of recurrences would give you the desired upper bound.)
"""

"""
https://www.baeldung.com/cs/local-minimum-in-n-x-n-matrix
https://stackoverflow.com/questions/18525179/find-local-minimum-in-n-x-n-matrix-in-on-time
"""

import numpy as np

def find_local_minimum(M, r1, r2, c1, c2):
    mid_row = int((r1 + r2) // 2)
    mid_column = int((c1 + c2) // 2)
    min_cell = get_min_cell(M, mid_row, mid_column, r1, r2, c1, c2)
    min_neighbor = get_min_neighbor(min_cell, M, r1, r2, c1, c2)
    if min_neighbor == min_cell:
        return min_cell, M[min_cell[0], min_cell[1]]
    elif min_neighbor[0] < mid_row:
        if min_neighbor[1] < mid_column:
            return find_local_minimum(M, r1, mid_row, c1, mid_column)     # Top-left sub-matrix
        else:
            return find_local_minimum(M, r1, mid_row, mid_column+1, c2)     # Top-right sub-matrix
    else:
        if min_neighbor[1] < mid_column:
            return find_local_minimum(M, mid_row+1, r2, c1, mid_column)     # Bottom-left sub-matrix
        else:
            return find_local_minimum(M, mid_row+1, r2, mid_column+1, c2)     # Bottom-right sub-matrix

# Get the cell with the smallest value among all the values in the middle row and the middle column
def get_min_cell(M, mid_row, mid_column, r1, r2, c1, c2):
    min_cell = (mid_row, c1)
    min_value = M[mid_row, c1]
    for j in range(c1, c2):
        if M[mid_row, j] < min_value:
            min_cell = (mid_row, j)
            min_value = M[mid_row, j]
    for i in range(r1, r2):
        if M[i, mid_column] < min_value:
            min_cell = (i, mid_column)
            min_value = M[i, mid_column]
    return min_cell

# Get the smallest adjacent cell
def get_min_neighbor(cell, M, r1, r2, c1, c2):
    x = cell[0]
    y = cell[1]
    value = M[x][y]
    min_neighbor = cell
    if x > c1 and value > M[x-1][y]:
        value = M[x-1][y]
        min_neighbor = (x-1, y)
    if y > r1 and value > M[x][y-1]:
        value = M[x][y-1]
        min_neighbor = (x, y-1)
    if x < c2-1 and value > M[x+1][y]:
        value = M[x+1][y]
        min_neighbor = (x+1, y)
    if y < r2-1 and value > M[x][y+1]:
        value = M[x][y+1]
        min_neighbor = (x, y+1)
    return min_neighbor

M1 = [[30, 100, 20, 19, 18],
     [29, 101, 21, 104, 17],
     [28, 102, 22, 105, 16],
     [27, 103, 23, 106, 15],
     [26, 25, 24, 107, 14]]
M1 = np.array(M1)
print(M1)
print(find_local_minimum(M1, 0, len(M1), 0, len(M1[0])))

M2 = [[32, 31, 100, 17, 13, 12, 113],
      [33, 30, 101, 18, 14, 11, 10],
      [34, 29, 102, 19, 15, 120, 9],
      [35, 28, 103, 20, 16, 121, 116],
      [36, 27, 104, 21, 107, 112, 117],
      [37, 26, 105, 22, 108, 111, 118],
      [38, 25, 106, 23, 109, 110, 119]]
M2 = np.array(M2)
print(M2)
print(find_local_minimum(M2, 0, len(M2), 0, len(M2[0])))