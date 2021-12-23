import datetime

def ivesti_gimimo_data():
    while True:
        metai = input("Įveskite darbuotojo gimimo metus (sveikas skaičius, formatas - YYYY): ")
        menuo = input("Įveskite mėnesį (skaičius tarp 1 ir 12): ")
        diena = input("Įveskite dieną (sveikas skaičius): ")
        try:
            return datetime.datetime(int(metai), int(menuo), int(diena))
        except ValueError as e:
            print(e)

def ivesti_atlyginima():
    while True:
        atlyginimas = input("Įveskite atlyginimą (skaičius): ")
        try:
            return float(atlyginimas)
        except ValueError as e:
            print(e)

def ivesti_darbuotojo_duomenis():
    vardas = input("Įveskite darbuotojo vardą: ")
    pavarde = input("Įveskite darbuotojo pavardę: ")
    gimimo_data = ivesti_gimimo_data()
    pareigos = input("Įveskite pareigas: ")
    atlyginimas = ivesti_atlyginima()
    return vardas, pavarde, gimimo_data, pareigos, atlyginimas

def ivesti_darbuotojo_id():
    while True:
        darbuotojo_id = input("Įveskite darbuotojo ID: ")
        try:
            return int(darbuotojo_id)
        except ValueError as e:
            print(e)