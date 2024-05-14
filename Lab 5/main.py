import random

def factorial():
    nfact= int(input("introduceti: "))
    p = 1
    for i in range(1, nfact + 1):
        p *= i
    print("factorialul:", p)
    return p


def c_in_f(c):
    return (c * 9/5) + 32

def f_in_c(f):
    return (f - 32) * 5/9


    unitate = input("Introduceți unitatea de măsură(C sau F): ")

    if unitate.upper() == 'C':
        t1 = float(input("Introduceți temperatura(se va converta din C in F): "))
        t2 = c_in_f(t1)
        print(t1, "grade Celsius sunt egale cu ", t2,"grade Fahrenheit.")

    elif unitate.upper() == 'F':
        t1 = float(input("Introduceți temperatura(se va converta din F in C): "))
        t2 = f_in_c(t1)
        print(t1, "grade Fahrenheit sunt egale cu ",t2, "grade Celsius.")
    else:
        print("Input invalid")

def gameUgadaika():
    nr = random.randint(1, 100)
    i = 0

    print("Alege un numar de la 1 la 100")

    while True:
        g = int(input("Introduceti un numar: "))
        i += 1

        if g < nr:
            print("Prea mic! Incercati din nou.")
        elif g > nr:
            print("Prea mare! Incercati din nou.")
        else:
            print(" Ai ghicit numarul corect, acesta este", nr, ", ai reusit din", i, "incercari.")
            break
def main():
    while True:
        print("\nMeniu:")
        print("1. Task 1")
        print("2. Task 2")
        print("3. Task 3")
        print("4. Iesire")

        optiune = input("Alegeți o opțiune: ")

        if optiune == "1":
            factorial()
        elif optiune == "2":
            f = int(input("introduceti: "))
            print(f_in_c(f))
        elif optiune == "3":
            gameUgadaika()
        elif optiune == "4":
            print("Ati iesit.")
            break
        else:
            print("Opțiune invalidă. Alegeți 1, 2 sau 3.")

main()