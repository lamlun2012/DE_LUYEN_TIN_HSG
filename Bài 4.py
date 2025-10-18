def ma_so(x):
    while x >= 10:
        x = sum(int(ch) for ch in str(x))
    return x

with open("BAI4.INP", "r") as f:
    data = list(map(int, f.read().split()))

n = data[0]         
nums = data[1:]     

ma = [ma_so(x) for x in nums]

from collections import Counter
dem = Counter(ma)
max_freq = max(dem.values())

ma_nhieu_nhat = min([k for k, v in dem.items() if v == max_freq])

cung_ma = [str(nums[i]) for i in range(n) if ma[i] == ma_nhieu_nhat]

with open("BAI4.OUT", "w") as f:
    f.write("Ma so: " + " ".join(map(str, ma)) + "\n")
    f.write("Cac so cung ma nhieu nhat: " + "; ".join(cung_ma))
