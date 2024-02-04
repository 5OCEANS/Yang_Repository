N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(N): #arr에서 첫번째 인덱스 
    for j in range(i+1, N): #i 다음 부터 마지막 인덱스까지 
        for k in range(j+1, N): #j다음부터 마지막 인덱스까지 
            if arr[i] + arr[j] + arr[k] > M: # 각각 다른 3개의 숫자 더하기 
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k])

print(result)