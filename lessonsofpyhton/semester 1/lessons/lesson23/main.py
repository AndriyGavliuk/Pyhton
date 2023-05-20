# file = open("lesson23/seek.txt")
# file.seek(2)
# print(file.read(1))
# file.close()

# file = open("lesson23/seek.txt")
# try:
#    print(file.read(3))
# finally:
#    print("The end")
#    file.close()

# try:
#    file = open("lesson23/seek.txt")
# except AttributeError:
#   print("An error has occurred")


# print("Some next code")


# try:
#    file = open("lesson23/seek.txt")
# except Exception as e:
#    print("An error has occurred:", str(e))


# print("Some next code")


with open("lesson23/seek.txt") as file:
    file.seek(2)
    print(file.read(1))
