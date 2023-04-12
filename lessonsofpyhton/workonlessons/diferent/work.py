# s = str(15)
# print(type(s))

# s = "ABCDEFGHI"
# first_element = s(0)
# last_element = s(-1)
# print (first_element)
# print(last_element)


# a = "Ivanov Ivan"

# first_elemet_of_surname = a[0]
# first_elemet_of_name = a[-4]
# if first_elemet_of_name == first_elemet_of_surname:
#   print("Перша літера імя співда


# l = 'hellO, worlD!'
# print(l.title())
# stop_words = ["Купити", "Продати", "реклама"]
# user_string = input()
# for stop_word in stop_words:
#   if user_string.find(stop_word) != -1:
#      print("It is spam message!!!")
#      break
#  else:
#      print("It is not spam")

# mystring = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada, est vitae suscipit vestibulum"
# n = int(input(""))


# if n > len(mystring):
#    print("wrong")
# else:
#    newstring = mystring[n:]
#    print(newstring)
# s = "I am learning string in Pyhron. Some new methods got now"
# sentences = s.split(". ")
# print(sentences)
# text = input("Ввести довільне речення з клавіатури і порахувати кількість слів.").split()
# print(len(text))
# delimiter = '-' * 80
# goods = [['Апельсин', 6, 150], ['Лимон', 8, 90], ['Картопля', 123, 445]]
# total_sum = 0
# number = 0

# print(delimiter)
# print("|{:^5}|{:<40}|{:>15}| {:>14}|".format('#', 'Товар', "Кількість", "Вартість"))
# print(delimiter)

# for good in goods:
#   name = good[0]
#  amount = good[1]
# number += 1
# total_sum += money
# print("|{:^5}|{:<40}|{:>15}|{:>15}|".format(number, name, amount, money))

# print(delimiter)
# print("|{:<62}|{:>15}|".format(' Total:', total_sum))
# print(delimiter)
# user = {
#   "name": "Bill",
#  "surname": "Bosh",
# "age": 22
# }
# if "age" in user:
#   print(user)
# clients = [
#    ['White House', 'Іванов', 3],
#    ['Shelter', 'Іванова', 5],
#    ['Верховина', 'Іванова', 5],
#   ['Буковель', 'Іванова', 5]
# ]

# hotels = dict()

# for voucher in clients:
#   voucher_hotel = voucher[0]
#  voucher_clients = voucher[2]

# if hotels.get(voucher_hotel, 0) == 0:
#   hotels[voucher_hotel] = voucher_clients
# else:
#   hotel_clients = hotels[voucher_hotel]
#  hotels[voucher_hotel] = hotel_clients + voucher_clients

# for hotel, clients in hotels.items():
#   print(f"У готелі {hotel} наразі проживає {clients} клієнтів")

# def print_sun():
#   a = 7
#   b = 9
#   print(a+b)


# print_sun()

# def print_max(a, b):
#  if a > b:
#      print(f"Max - {a}")
#  elif a == b:
#     print("equal")
# else:
#      print(f"max - {b}")


# print_max


def name():
    print(f"Hello {name}")
    name = input("Enter your name: ")


name()
