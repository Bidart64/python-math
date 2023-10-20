import matplotlib.pyplot as plt

def collatz(n):
  if (n == 1):
    return 1
  elif (n % 2 == 0):
    return collatz(n / 2)
  else:
    return collatz(3 * n + 1)
  
def main(n):
  i = 1
  collatz_values = []
  while (i < n):
    collatz_values.append(collatz(i))
    i += 1
  plt.plot(range(1, n), collatz_values)
  plt.xlabel('i')
  plt.ylabel('collatz(n)')
  plt.show()
  exit()
  
main(1000)
