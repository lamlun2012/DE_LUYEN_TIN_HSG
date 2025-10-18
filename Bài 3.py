with open("BAI3.INP", "r", encoding="utf-8") as f:
    S = f.read().strip()

digits = "".join(ch for ch in S if ch.isdigit())
if digits == "":
    a = "0"
else:
    a = digits

b = "KHONG"
for i in range(len(a) - 1, -1, -1):
    if a[i] in ['0', '5']:
        b = a[:i + 1]  
        break

import re
nums = re.findall(r'\d+', S)
T = sum(int(x) for x in nums)

with open("BAI3.OUT", "w", encoding="utf-8") as f:
    f.write(f"a = {a}; b = {b}; T = {T}")
