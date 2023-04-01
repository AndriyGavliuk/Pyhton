numbers = [6, 2, 1, 8, 10]
max = 0
min = 0
for i in numbers:
    if i > max:
        max = i

    if i < max:
        min = i
print(min)
print(max)


number = numbers.pop(2) and numbers.pop(-1)

print(number)
