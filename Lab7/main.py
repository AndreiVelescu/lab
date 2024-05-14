import re

def introducere_date():
    nume = input("Introduceți numele angajatului: ")
    prenume = input("Introduceți prenumele angajatului: ")
    numar_copii = input("Introduceți numărul de copii minori aflați în întreținerea angajatului: ")

    # Verificare folosind expresii regulate
    if re.match(r'^[a-zA-Z\-]+$', nume) and re.match(r'^[a-zA-Z\-]+$', prenume) and re.match(r'^\d{1,2}$', numar_copii):
        with open("data.txt", "a") as file:
            file.write(f"{nume}\t{prenume}\t{numar_copii}\n")
        print("Datele au fost înregistrate cu succes!")
    else:
        print("Datele introduse nu respectă formatul specificat. Vă rugăm să încercați din nou.")


def vizualizare_date():
    try:
        with open("data.txt", "r") as file:
            angajati = file.readlines()
            total_copii = 0
            print("Lista angajaților și numărul lor de copii:")
            for angajat in angajati:
                angajat = angajat.strip().split("\t")
                nume, prenume, numar_copii = angajat
                numar_copii = int(numar_copii)
                total_copii += numar_copii
                print(f"{nume} {prenume}: {numar_copii} copii")
            print(f"Număr total de copii al angajaților companiei: {total_copii}")
    except FileNotFoundError:
        print("Nu există date salvate încă.")


def menu():
    print("Informații cu referire la angajații Bumba-Lumba")
    while True:
        print("\nMeniu:")
        print("1. Introducere date")
        print("2. Vizualizare date")
        print("3. Ieșire")
        optiune = input("Alegeți o opțiune: ")

        if optiune == '1':
            introducere_date()
        elif optiune == '2':
            vizualizare_date()
        elif optiune == '3':
            print("Meniul este închis")
            break
        else:
            print("Opțiune invalidă. Vă rugăm să introduceți 1, 2 sau 3.")

if __name__ == '__main__':
    menu()
