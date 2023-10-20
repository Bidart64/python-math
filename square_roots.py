import matplotlib.pyplot as plt
from mpmath import mp
mp.dps = 50
plt.figure(figsize=(10, 10))
print("Input a:")
a = int(input())
print("Input n:")
n = int(input())
f1 = a
g2 = 0
f2 = a
i = 1
axis1 = []
axis2 = []
while i < n:
    p = 1
    f1 = a
    while p < i:
        f2 = (((f1 / mp.sqrt(p)) ** 2)-1)
        f1 = mp.sqrt(f2*(i-p)+1)
        p = p+1
    axis1.append(float(f1))
    axis2.append(float(i))
    i = i + 1
print(f1)
plt.plot(axis2, axis1, 'k.')
plt.show()