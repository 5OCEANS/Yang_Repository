#올라가는 거리=A 미끄러지는 거리=B 높이=V
#하루동안 올라갈 수 있는 거리=A-B
#올라가야할 거리 = V-B

#A, B, V = map(int, input().split())

#if (V-B) % (A-B) == 0 : #딱떨어지게 다 올라감
#    print((V-B)//(A-B))
#else:
#    print((V-B)//(A-B)+1) #밤에 미끄러진 거리가 있어서 1일 추가

import math

A, B, V = map(int,input().split())
day = (V-B) / (A-B)
print(math.ceil(day)) #ceil함수로 올림한다. 