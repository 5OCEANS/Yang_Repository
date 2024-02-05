m, n = map(int, input().split())

for num in range(m, n+1):
    if num == 1:
        continue
    for i in range(2, int(num**0.5)+1): #제곱근 구하기 
        #어떤 수의 약수 중 하나가 그 수의 제곱근을 넘어가면 구할 필요가 없어서 
        if num % i ==0: #나누어 떨어지면 소수가 아니다 
            break
    else:
        print(num)