v = int(input())
t = int(input())
d = 109

if(v < 0):
    ans = (v*t) + d
else:
    ans = (v * t) - d

print(ans)

