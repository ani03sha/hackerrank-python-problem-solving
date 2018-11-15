# Given an array of integers, find the sum of its elements.


import os


def simple_array_sum(a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simple_array_sum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
