#-*- coding: utf-8 -*-
import heapq

print("# 최소값 출력")
def kth_smallest(nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  kth_min = None
  for _ in range(k):
    kth_min = heapq.heappop(heap)
  return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3))

print("# Heap Sort test")
# Heap 정렬
nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1

print("# Heap pop test")
# Heap pop test
for num in nums:
    print(num)
    nums.pop()
