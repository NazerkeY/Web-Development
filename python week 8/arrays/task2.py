def func(a,b, c, d):
    min = 10000000
    if a < min:
        min = a
    if b < a:
        min = b
    if c < a or c < b:
        min = c
    if d < a or d < b or d < c:
        min = d
    return min

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(func(a,b,c,d))
