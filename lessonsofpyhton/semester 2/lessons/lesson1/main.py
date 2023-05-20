# file = open("my_name.txt", "w")
# file.write("My name is Andriy")
# file.close()

# file = open("my_name.txt", "a")
# file.write("\n\nI am 16.")
# file.close()


# file = open("my_name.txt", "r")
# info = file.read()
# print(info)
# file.close()


file = open("semester 2/lessons/grades.csv", "r")
result = []


for line in file:
    arr = line.split(",")
    print(arr)
    result.append(arr)

sum_of_grades = sum(map())
file.close
