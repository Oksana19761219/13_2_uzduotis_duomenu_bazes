from duomenu_bazes_veiksmai import prideti_irasa, perziureti_darbuotoju_duomenis, istrinti_darbuotojo_duomenis, pasirinkti_iraso_id, atnaujinti_darbuotojo_duomenis
from pagalbines_funkcijos import ivesti_darbuotojo_duomenis

veiksmas = "1"
while veiksmas in ["1", "2", "3", "4"]:
    veiksmas = input("""Pasiriknike norimą veiksmą:
    1 - pridėti įrašą
    2 - ištrinti įrašą
    3 - peržiūrėti duomenis
    4 - pakeisti darbuotojo duomenis
    kitas mygtukas - programos pabaiga
    """)

    if veiksmas == "1":
        vardas, pavarde, gimimo_data, pareigos, atlyginimas = ivesti_darbuotojo_duomenis()
        prideti_irasa(vardas, pavarde, gimimo_data, pareigos, atlyginimas)

    elif veiksmas == "2":
        darbuotojo_id = pasirinkti_iraso_id()
        if darbuotojo_id:
            istrinti_darbuotojo_duomenis(darbuotojo_id)


    elif veiksmas == "3":
        darbuotoju_duomenys = perziureti_darbuotoju_duomenis()
        for darbuotojas in darbuotoju_duomenys:
            print("ID ", darbuotojas.id, darbuotojas)

    elif veiksmas == "4":
        darbuotojo_id = pasirinkti_iraso_id()
        if darbuotojo_id:
            atnaujinti_darbuotojo_duomenis(darbuotojo_id)

    else:
        print("viso gero")

