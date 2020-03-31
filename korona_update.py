import json

while(1):
    print("0. Dodaj \n 1. Edytuj \n")
    mode = int(input("\n"))

    print("0. Daty \n 1. Nr dnia \n 2. Zdiagnozowani \n 3. Hospitalizacja \n 4. Kwarantanna \n 5. Zgony \n 6. Wyzdrowiali \n 7. Wiek \n 8. Plec \n")


    json_array_titles = {"daty", "nr_dnia", "zdiagnozowani", "hospitalizacja", "kwarantanna", "zgony", "wyzdrowiali", "wiek_zmarlych", "plec_zmarlych"}
    json_fields_titles = {"data", "nr", "ilosc", "ilosc", "ilosc", "ilosc", "ilosc", "wiek", "plec"}

    with open('korona-data.json', 'w') as json_file:
        data = json.load(json_file)
        if mode:
            mode = int(input("\n"))
            value_to_add = input("Wartosc do dodania: ")
            if is not mode:
                value_to_add = int(value_to_add)
            data[json_array_titles[mode]].append({json_fields_titles[mode]: value_to_add})
        else:
            mode = int(input("\n"))
            value_to_add = input("Wartosc uaktualniona: ")
            if is not mode:
                value_to_add = int(value_to_add)
            data[json_array_titles[mode]][-1][json_fields_titles[mode]] = value_to_add
        json.dump(data, json_file)
    
    mode = int(input("\n0. Add next value \n 1. Exit \n"))

    if mode:
        break
