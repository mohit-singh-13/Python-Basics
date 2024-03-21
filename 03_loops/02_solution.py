n = input("Enter n : ")
sum_even = 0

for i in range(1, int(n)+1):
    if i % 2 == 0:
        sum_even += i

print("Sum even is : ", sum_even)