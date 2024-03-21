items = ["apple", "banana", "orange", "apple", "mango"]

# for i in items:
#     if (items.count(i) > 1):
#         print(i)
#         break

unique_items = set()

for i in items:
    if i in unique_items:
        print("Duplicate", i)
        break
    else:
        unique_items.add(i)