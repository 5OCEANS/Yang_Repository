a, b = map(int, input().split())

#최대공약수 a를 b로 나눈것의 나머지 = r, a와 b의 최대공약수 = b와 r의 최대공약수 (0으로 나눠지지 않을때까지 반복)
def gcd(a,b):
    while b>0:
        a,b = b, a % b
    return a #나머지 r''이 0이 되면 나누는 수 r'이 a와 b의 최대공약수이다. 

#최소공배수 두수 a * b = l * g -> l = a*b // g
def lcm(a,b):
    return a * b // gcd(a, b)

print(gcd(a,b))
print(lcm(a,b))