# currencies = {'USD':  36.9, 'EUR': 38.18, 'GBP': 43.87}
# currencies["PLN"] = 8.18
# currencies["USD"] = 39
# currencies["EUR"] = 41
# currencies["GBP"] = 44
# currencies["RDK"] = 49
# currencies["POK"] = 42

# currency = input("Enter currency you would like to exchange")
# amount = float(input("How much you wanr exchange"))

# print(currencies.values())
# if currency not in currencies.keys():
#   print("He dont support such currency")
# else:
#    result = round(amount * currencies[currency], 2)
#    print("Here is your {} UAH".format(result))


transport = {
    'AA1111AA': 'Іванов Іван',
    'IVANOV': 'Іванов Іван',
    'AA0007AA': 'Семенов Андрій',
    'AA007AA': 'Іванов Іван',
    'AВ1111AВ': 'Вінниця Водоканал',
    'AІ1010КК': 'Семенов Андрій',

}
transport["II6767AO"] = "Петренко Петро"
transport["CA8888CE"] = "Іванов Олексій"

car_plate = input("Enter the plate to find car")
car_owner = transport.get(car_plate, ("Not Found"))
print("car owner of plate {} is {}".format(car_plate, car_owner))

car_owners = dict()
for owner in transport.values():
    if car_owners.get(owner, 0) == 0:
        car_owners[owner] = 1
    else:
        auto_count = car_owners[owner]
        auto_count += 1
        car_owners[owner] = auto_count
        for owner, auto_count in car_owners.items():
            if auto_count > 1:
                print(f"Owner{owner} has {auto_count} cars")
