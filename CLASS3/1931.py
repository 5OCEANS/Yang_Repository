n=int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x : (x[1], x[0]))
#종료시간을 기준으로 회의를 오름차순으로 정렬하고 종료시간이 같다면 시작 시간을 오름차순으로 정렬

time=0 #현재시간 초기화
answer=0 #진행할 수 있는 회의 개수

#모든 회의를 확인하면서 진행할 수 있는 회의의 개수를 초기화한다.
for meeting in meetings:
    if time <= meeting[0]: #현재시간이 회의 시작시간보다 같거나 같으면
        time = meeting[1] #현재시간을 해당 회의 종료 시간으로 갱신
        answer += 1 #진행할 수 있는 회의의 개수 1 2증가 

print(answer)