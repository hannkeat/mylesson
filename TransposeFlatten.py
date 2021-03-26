import numpy as np

n, m = map(int, input().split())
array = np.array([input().strip().split() for _ in range(n)], int)

print(np.transpose(array))
print(array.flatten())


"""
sample input

3 2
1 2
3 4
5 6

expected output
[[1 3 5]
 [2 4 6]]
[1 2 3 4 5 6]

"""