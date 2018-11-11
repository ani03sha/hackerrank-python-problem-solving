# An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an
# array, A, of size N, each memory location has some unique index, i (where 0 <= i < N), that can be referenced as A[i].

n, a = int(input()), list(map(int, input().split()))
for i in range(n-1, -1, -1):
    print(a[i], end=' ')
