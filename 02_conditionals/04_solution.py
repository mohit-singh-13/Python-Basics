# fruit ripeness checker

fruit = input("Enter fruit : ")
color = input("Enter color : ")

if fruit == "Banana":
    if color == "Green":
        print("Unriped")
    elif color == "Yellow":
        print("Riped")
    elif color == "Brown":
        print("Over Riped")