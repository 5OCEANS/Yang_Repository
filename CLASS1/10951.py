#try-except구문 수가 입력되지 않을때 반복문을 끝낼 수 있도록
while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a+b)