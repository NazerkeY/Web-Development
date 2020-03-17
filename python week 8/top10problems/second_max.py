n = int(input())
current = []
list = []
current = input().split()
list = sorted(set(current)).copy()
print(list[-2])