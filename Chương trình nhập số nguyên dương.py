with open("Nhập số nguyên dương.INP", "r") as f:
    n = int(f.read().strip())

P = sum(int(ch) for ch in str(n))

S = 0
for i in range(2, n + 2):
    S += ((-1) ** i) / i
S = round(S, 4)

tong = 0
k = 0
while tong + k * (k + 1) <= n * n:
    k += 1
    tong += k * (k + 1)
k -= 1  

with open("Nhập số nguyên dương.OUT", "w") as f:
    f.write(f"P = {P}; S = {S}; k = {k}")
