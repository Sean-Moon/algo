#-*- coding: utf-8 -*-
#최단거리 구하기
line_num = int(input())
print(line_num)

nums = [int(x) for x in input().split()]
print(nums)

shortest_length = 1000000
for i in range(0, len(nums)-1): 
    if(shortest_length > nums[i+1] - nums[i]):
        shortest_length = nums[i+1] - nums[i]

print(shortest_length)