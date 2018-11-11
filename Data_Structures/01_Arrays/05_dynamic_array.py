# Create a list, seqList, of N empty sequences, where each sequence is indexed from 0 to N-1. The elements within
# each of the N sequences also use 0-indexing.
#
# Create an integer, lastAnswer, and initialize it to 0. The  types of queries that can be performed on your list of
# sequences (seqList) are described below:
#
# Query: 1 x y
# Find the sequence, seq, at index ((x XOR lastAnswer) % N) in seqList. Append integer y to sequence seq.
#
# Query: 2 x y Find the sequence, seq, at index ((x XOR lastAnswer) % N) in seqList. Find the value of element y%size
#  in seq ( where size is the size of seq) and assign it to lastAnswer.
# Print the new value of lastAnswer on a new line Task


n, q = map(int, input().split())
d = [[] for i in range(n)]
lastAnswer = 0
for _ in range(q):
    a = list(map(int, input().split()))
    index = (a[1] ^ lastAnswer) % n
    if a[0] == 1:
        d[index].append(a[2])
    elif a[0] == 2:
        lastAnswer = d[index][a[2] % len(d[index])]
        print(lastAnswer)
