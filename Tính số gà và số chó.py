with open("GA_CHO.INP", "r") as f:
    m, n = map(int, f.read().split())  

g = 2 * m - n // 2
c = m - g

if n % 2 != 0 or g < 0 or c < 0:
    result = "KHONG"
else:
    result = f"Ga = {g}; Cho = {c}"

with open("GA_CHO.OUT", "w") as f:
    f.write(result)
