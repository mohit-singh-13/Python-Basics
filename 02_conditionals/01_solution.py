# age group categorization

age = input("Enter your age : ")
age = int(age)

if age < 13:
    print("Child")
elif age < 20:
    print("Teenagers")
elif age < 60:
    print("Adult")
else:
    print("Senior")