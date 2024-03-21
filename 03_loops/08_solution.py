my_num = 11

flag = True

for i in range(2, my_num):
    if my_num % i == 0:
        print("NOT a Prime Number")
        flag = False
        break

if flag:
    print("Prime Number")