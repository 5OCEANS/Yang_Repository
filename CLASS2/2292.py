n = int(input())

nums, cnt = 1, 1 #num -> 벌집 개수 , cnt -> 반복문이 반복되는 횟수
while n > nums:
    nums += 6 * cnt
    cnt += 1
#nums에 6의 배수인 6*cnt를 더하고  cnt는 1씩 증가 
    #층이 하나씩 증가할 때마다 해당 층의 마지막 숫자 범위 업데이트 

print(cnt)