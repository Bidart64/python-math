import matplotlib.pyplot as plt

import numpy as np


fig = plt.figure(figsize=(10, 10), dpi=100)

fig.set_facecolor('black')
ax = plt.axes()
plt.axis('off')

# ax.set_axis_bgcolor('black')


#mp.dps = 50
print("Input p:")
p = int(input())
i = 0
m = p
c = 0
axis1 = []
axis2 = []

def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


axis1.append(primes(p)*np.cos(primes(p)))
axis2.append(primes(p)*np.sin(primes(p)))

plt.plot(axis2, axis1, 'yo', markerfacecolor="None")
plt.show()

