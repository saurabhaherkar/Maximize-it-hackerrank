from itertools import product

n, m = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
a = list(product(*arr))
z = list(map(lambda x : sum(i**2 for i in x)%m, a))
print(max(z))