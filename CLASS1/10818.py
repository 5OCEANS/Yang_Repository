n=int(input())
nums=list(map(int,input().split()))
#print(min(nums), max(nums))

max=nums[0]
min=nums[0]
for i in nums[1:]: #첫번째 숫자는 max랑min에 할당해서 1부터 시작한다
    if i  > max:
        max = i
    elif i < min:
        min = i
print(min,max)