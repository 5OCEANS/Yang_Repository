while True:
    nums = list(map(int,input().split()))
    max_num=max(nums)
    if sum(nums)==0:
        break
    nums.remove(max_num)
    if max_num**2==nums[0]**2+nums[1]**2:
        print('right')
    else:
        print('wrong')