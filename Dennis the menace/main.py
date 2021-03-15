from itertools import combinations 

arr = list(map(int,input().split(' ')))
N = int(input())

allCom = list(combinations(arr, N))

total = 0
for com in allCom:
    if total < sum(com):
        total = sum(com)
    
print(total)