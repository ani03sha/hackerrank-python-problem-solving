# Given a 6X6 2D Array, arr:
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
#
# We define an hourglass in A to be a subset
# of values with indices falling in this pattern in 's graphical representation:
#
# a b c
#   d
# e f g
#
# There are 16 hourglasses in , and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum
# for every hourglass in arr, then print the maximum hourglass sum.
#
# For example, given the 2D array:
#
# -9 -9 -9  1 1 1
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0
#
# We calculate the following  hourglass values:
#
# -63, -34, -9, 12,
# -10, 0, 28, 23,
# -27, -11, -2, 10,
# 9, 17, 25, 18
# Our highest hourglass value is  from the hourglass:
#
# 0 4 3
#   1
# 8 6 6
#
# Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in
# the array.


import sys

a = [[j for j in map(int, input().strip().split())] for i in range(6)]
m = -sys.maxsize - 1
for i in range(4):
    for j in range(4):
        s = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]
        if m < s:
            m = s
print(m)
 