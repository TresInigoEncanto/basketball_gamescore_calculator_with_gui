# number_entered = [float(input(f"Enter value {index + 1}: ")) for index in range (0, 10)]

# seen = set()
# duplicates = set()

# for num in number_entered:
#     if num in seen:
#         duplicates.add(num)
#     else:
#         seen.add(num)

# print("Duplicate numbers:", *duplicates )

number_entered = [float(input(f"Enter value {index + 1}: ")) for index in range (0, 10)]

seen = set()
duplicates = set()

for number in number_entered:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)

print("Duplicate numbers:", * duplicates )