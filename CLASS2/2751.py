n=int(input())
numbers=[]

for i in range(n):
    numbers.append(int(input()))

#numbers.sort()
#for num in numbers:
#    print(num)
#위 세줄 합쳐서 
for i in sorted(numbers):
    print(i)