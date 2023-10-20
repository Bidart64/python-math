import matplotlib.pyplot as plt

print("Input maximum:")
maximum = int(input())


def multiple_3_and_5(n):
    values = []
    i = 1
    while (i < n):
        if (n % 3 == 0):
            values.append(n)
        elif (n % 5 == 0):
            values.append(n)
        i += 1
        return sum(values)


def main(m):
    j = 1
    values = []
    while (j < m):
        values.append(multiple_3_and_5(j))
        j += 1
    fig, ax = plt.subplots()
    ax.stem(range(1, m), values)
    plt.xlabel('i')
    plt.ylabel('multiple_3_and_5(i)')
    plt.show()
    exit()


print(main(maximum))
