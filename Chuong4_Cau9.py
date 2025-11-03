import math
n = int(input("Nhập n (số dấu căn): "))
s = 0
for i in range(n):
    s = math.sqrt(2 + s)
print(f"S({n}) = {s}")