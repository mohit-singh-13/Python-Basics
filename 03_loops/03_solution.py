n = input("Enter n : ")

for i in range(1, 11):
    if i == 5:
        continue

    print(n, " * ", i, " = ", int(n)*i)