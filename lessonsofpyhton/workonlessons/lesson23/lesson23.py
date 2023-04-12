file = open("lesson23/text.txt", "w")
file.write("Banana\n")
file.write("Orange\n")
file.close()


file = open("lesson23/text.txt")
a = open("lesson23/stext.txt", "w")


while True:
    symbol = file.read(1)
    if len(symbol) == 0:
        print("The end")
        break
    else:
        a.write(f"{symbol}\n")

a.close()
file.close()
