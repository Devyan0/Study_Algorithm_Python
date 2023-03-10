"""
https://www.acmicpc.net/problem/10815
pin point, while-else
"""
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards.sort()

M = int(input())
finds = map(int, input().split())
for find in finds:
    l, r = 0, len(cards)-1          # 닫힌 범위로 초기화
    while l <= r:                   # 종료 조건 확인
        mid = (l+r) // 2
        check = cards[mid]
        if find == check:
            print(1, end=' ')
            break                   # 찾으면 끝
        elif find < check:
            r = mid - 1             # 업데이트 확인
        elif check < find:
            l = mid + 1

    else:
        print(0, end=' ')           # 못 찾은 경우

