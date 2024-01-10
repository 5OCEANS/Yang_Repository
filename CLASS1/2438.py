n=int(input())
"""
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    if i is not n-1:
        print()
"""
for i in range(1, n+1):
    print("*" * i)