n = int(input())
arr = list(map(int, input().split()))
same = False
for i in range(0, n - 1):
    if (arr[i] > 0 and arr[i + 1] > 0) or (arr[i] > 0 and arr[i + 1] < 0):
        same = True
    else: same = False
if(same == True): print('YES')  
else: print('NO')  