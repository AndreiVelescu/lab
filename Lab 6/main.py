import re

#1 email
def email():
    try:
        email = input("Introduceți adresa de e-mail: ")
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            print("Adresa de e-mail este validă.")
        else:
            raise ValueError
    except ValueError:
            print("Adresa de e-mail nu este validă.")

 #2  cod postal
def cod_postal():
    try:
        cod_postal = input("Introduceți codul poștal: ")
        pattern = r'^[a-zA-Z0-9]{6}$'
        # exact 6 caractere, fie cifre, fie litere
        if re.match(pattern, cod_postal):
            print("Codul poștal este valid.")
        else:
            raise ValueError
    except ValueError:
            print("Codul postal nu este valid.")


# 3.nume de utilizator

def nume_utilizator():
    try:
        nume_utilizator = input("Introduceți numele de utilizator: ")
        pattern = r'^[a-zA-Z0-9]{5,15}$'
        # doar din litere și/sau cifre și să aibă între 5 și 15 caractere.
        if re.match(pattern, nume_utilizator):
            print("Numele este valid.")
        else:
            raise ValueError
    except ValueError:
            print("Numele nu este valid.")

# 4. adresa URL
def adresa_url():
    try:
        adresa_url = input("Introduceți adresa url: ")
        pattern = r'^(http|https)://[^\s/$.?#].[^\s]*$'
        # să înceapă cu "http://" sau "https://" și să conțină cel puțin un caracter "." după "http://" sau "https://".
        if re.match(pattern, adresa_url):
            print("Adresa este valida.")
        else:
            raise ValueError
    except ValueError:
            print("Adresa nu este validă.")

# 5.parola

def parola():

    try:
        parola = input("Introduceți parola: ")
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,16}$'
        # să aibă între 8 și 16 caractere și să conțină cel puțin o literă majusculă,
        # o literă minusculă, o cifră și un caracter special (de exemplu, @, #, $, %)
        if re.match(pattern, parola):
            print("parola este valida")
        else:
            raise ValueError
    except ValueError:
            print("parola nu este validă.")

def main():
    while True:
        print("1. Email")
        print("2. Cod postal")
        print("3. Nume utilizator")
        print("4. Adresa url")
        print("5. Parola")
        print("6. Iesire")
        optiune = input("Alege optiunea: ")

        if optiune == "1":
            email()
        elif optiune == "2":
            cod_postal()
        elif optiune == "3":
            nume_utilizator()
        elif optiune == "4":
            adresa_url()
        elif optiune == "5":
            parola()
        elif optiune == "6":
            print("Ati iesit")
            break
        else:
            print("Numar invalid, alege una din obtiunile propuse.")

if __name__ == '__main__':
    main()