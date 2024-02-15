t = int(input())

for i in range (t):
    k = int(input())
    n = int(input())
    people=[i for i in range(1, n+1)]

    for x in range (k):
        new=[]
        for y in range(n):
            new.append(sum(people[:y+1])) #y가 0일때: 첫번째 호실까지 주민 포함, y가 1일때 두번째 호실까지 주민 포함, y가 2이면 세번째 호실까지 주민 포함
        people = new.copy()
    print(people[-1])