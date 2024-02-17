import sys
input = sys.stdin.readline

k,n=map(int, input().split())

lan = []
for _ in range(k):
    lan.append(int(input()))

start=1
end=max(lan)
result=0 #결과값 저장 변수 초기화 

while start <= end:
    cnt=0
    mid=(start+end)//2

#지금 길이로 만들 수 있는 랜선 개수 계산
    for i in lan:
        cnt +=(i//mid)

#필요한 랜선 개수보다 지금 만들 수 잇는 랜선 개수가 ㅁ낳거나 같은경우 
    if cnt >= n:
        result = mid #결과값저장 
        start=mid +1 
#필요한ㄹ 랜선 개수보다 지금 만들 수있는 랜선 개수가 부족해 
    else:
        end = mid -1 #끝점을 현재 중간값 이전값으로 

print(result)