"""
https://www.acmicpc.net/problem/1920
case 1 -> case 3: parametric search
"""

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

def search(target, nums=nums):
    l, r = 0, len(nums)
    while l < r:
        mid = (l+r)//2
        if nums[mid] == target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid
        elif nums[mid] < target:
            l = mid+1
    return 0 < l and nums[l-1] == target

K = int(input())
finds = map(int, input().split())
for to_find in finds:
    print(1 if search(to_find) else 0)

