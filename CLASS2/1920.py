n = int(input())
n_list = list(map(int, input().split())) #n개의 정수를 리스트로 받음, 정렬
n_list.sort()

m=int(input())
targets = list(map(int, input().split()))

#이진탐색 정의
def binary(target):
    left = 0
    right = n-1

    while left <= right: #왼쪽 인덱스가 오른쪽 인덱스보다 작거나 같을때까지 반복
        mid = (left+right)//2 #중간인덱스 계산
        if n_list[mid] == target: #중간값이 타겟과 같으면 
            return True
        
        if target < n_list[mid]: #타겟이 중간값보다 작으면 오른쪽을 중간값 -1로 설정
            right = mid-1
        elif target > n_list[mid]: #타겟이 중간값보다 크면 왼쪽을 중간값 +1로 설정
            left = mid +1

for i in range(m): #모든 타겟에 대해 반복
    if binary(targets[i]):
        print(1)
    else:
        print(0)