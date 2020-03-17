n = int(input())
i = 0
while 2 ** i <= n:
    if 2 ** i == n: even = True
    else: even = False
    i = i + 1
if(even): print('YES')
else:print('NO')    