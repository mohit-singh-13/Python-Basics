file = open('youtube.txt', 'w')

try:
    file.write("Mohit Singh")
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write("Jyoti Singh")