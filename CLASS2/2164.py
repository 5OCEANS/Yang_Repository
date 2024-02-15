from collections import deque
import sys

input = sys.stdin.readline
n = int(input()) #큐에 들어갈 범위 n입력받기
queue = deque()
queue = deque(range(1,n+1)) #1부터 n까지로 채워진 큐 생성
while len(queue)!=1: #큐에 1개만 남을때까지 반복
    queue.popleft() #큐에 맨 앞 요소 빼기
    queue.append(queue.popleft()) #큐에서 빼낸 요소 다시 큐 뒤에 넣기 
print(queue.popleft()) #마지막 남은 요소 출력