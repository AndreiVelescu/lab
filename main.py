import re
from employee import Employee, HourlyEmployee, SalaryEmployee

# Funcție pentru verificarea inputului conform cerințelor
def validate_input(prompt, regex):
    while True:
        value = input(prompt)
        if re.match(regex, value):
            return value
        else:
            print("Input invalid. Reîncercați.")

# Introducerea datelor pentru angajați
name = validate_input("Introduceți numele angajatului: ", "^[a-zA-Z ]+$")
phone = validate_input("Introduceți numărul de telefon: ", r"^\+373\d{9}$")
birth_date = validate_input("Introduceți data nașterii (dd.mm.yyyy): ", r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19[6-9][0-9]|200[0-7])$")
email = validate_input("Introduceți adresa de email: ", r"^[a-zA-Z0-9._-]{2,20}@[a-zA-Z]{4,7}\.[a-zA-Z]{2,4}$")
specialty = validate_input("Introduceți specialitatea angajatului: ", "^[a-zA-Z ]{2,20}$")

hourly_rate = float(input("Introduceți tariful pe oră: "))
hours_worked = float(input("Introduceți numărul de ore lucrate: "))

monthly_salary = float(input("Introduceți salariul lunar: "))

# Crearea obiectelor
employee1 = Employee(name, phone, birth_date, email, specialty)
hourly_employee = HourlyEmployee(name, phone, birth_date, email, specialty, hourly_rate)
salary_employee = SalaryEmployee(name, phone, birth_date, email, specialty, monthly_salary)

# Afișarea salariilor
print("Salariul angajatului cu plată pe oră:", hourly_employee.calculateSalary(hours_worked))
print("Salariul angajatului cu salariu fix:", salary_employee.calculateSalary())