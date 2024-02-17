n = int(input())
cnt = 0 #종말번호를 업데이트 시킬 카운트값
result = 666 # 종말번호

while True: 
    if '666' in str(result): # 666이 있는지 확인
        cnt += 1 # 666이 포함되어있으면 카운터 변수 1 추가
    
    if cnt == n : #카운터변수가 입력받은 n이랑 같다 (원하는 개수의 숫자를 찾았다면 중단)
        break

    result +=1 #종말번호를 계속 1씩 증가

print(result) #입력한 n번째 종말번호 출력