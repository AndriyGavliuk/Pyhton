with open("Homework21.txt", "a") as f:
    while True:
        name = input("Введіть ім'я користувача (або 'q' для виходу): ")
        if name == "q":
            break
        f.write(name + "\n")
