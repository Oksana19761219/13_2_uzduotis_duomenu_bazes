from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from duomenu_baze import Darbuotojai
from pagalbines_funkcijos import ivesti_darbuotojo_id, ivesti_gimimo_data, ivesti_atlyginima

engine = create_engine('sqlite:///darbuotojai.db')
Session = sessionmaker(bind=engine)


def prideti_irasa(vardas, pavarde, gimimo_data, pareigos, atlyginimas):
    session = Session()
    irasas = Darbuotojai(vardas, pavarde, gimimo_data, pareigos, atlyginimas)
    session.add(irasas)
    session.commit()

def perziureti_darbuotoju_duomenis():
    session = Session()
    darbuotoju_duomenys = session.query(Darbuotojai).all()
    return darbuotoju_duomenys

def ar_validus_darbuotojo_id(darbuotojo_id):
    session = Session()
    darbuotoju_duomenys = session.query(Darbuotojai).all()
    id_sarasas = [darbuotojas.id for darbuotojas in darbuotoju_duomenys]
    return darbuotojo_id in(id_sarasas)

def pasirinkti_iraso_id():
    darbuotoju_duomenys = perziureti_darbuotoju_duomenis()
    for darbuotojas in darbuotoju_duomenys:
        print("ID ", darbuotojas.id, darbuotojas)
    darbuotojo_id = ivesti_darbuotojo_id()
    if ar_validus_darbuotojo_id(darbuotojo_id):
        return darbuotojo_id
    else:
        print("Tokio darbuotojo nėra")

def istrinti_darbuotojo_duomenis(darbuotojo_id):
    session = Session()
    darbuotojo_duomenys = session.query(Darbuotojai).filter_by(id = darbuotojo_id).one()
    session.delete(darbuotojo_duomenys)
    session.commit()


def atnaujinti_darbuotojo_duomenis(darbuotojo_id):
    session = Session()
    keiciama_reiksme = "1"
    while keiciama_reiksme in ["1", "2", "3", "4", "5"]:
        darbuotojo_duomenys = session.query(Darbuotojai).filter_by(id = darbuotojo_id).one()
        print(darbuotojo_duomenys)
        keiciama_reiksme = input("""Pasirinkite keičiamus duomenis:
        1 - vardas
        2 - pavardė
        3 - gimimo data
        4 - pareigos
        5 - atlyginimas
        kitas mygtukas - nieko keisti nenoriu
        """)
        if keiciama_reiksme == "1":
            darbuotojo_duomenys.vardas = input("Įveskite vardą: ")
        elif keiciama_reiksme == "2":
            darbuotojo_duomenys.pavarde = input("Įveskite pavardę: ")
        elif keiciama_reiksme == "3":
            darbuotojo_duomenys.gimimo_data = ivesti_gimimo_data()
        elif keiciama_reiksme == "4":
            darbuotojo_duomenys.pareigos  = input("Įveskite pareigas: ")
        elif keiciama_reiksme == "5":
            darbuotojo_duomenys.atlyginimas = ivesti_atlyginima()
    session.commit()




