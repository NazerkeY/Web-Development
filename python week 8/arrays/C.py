cnt = 0
x = int(input())
arr = list(map(int, input().split()))
for i in range(0, x):
    if(arr[i] > 0):
        cnt += 1
print(cnt)
