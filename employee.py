import re


class Employee:
    def __init__(self, name, phone, birth_date, email, specialty, monthly_salary=None):
        self.name = name
        self.phone = phone
        self.birth_date = birth_date
        self.email = email
        self.specialty = specialty
        self.monthly_salary = monthly_salary


    def calculateAge(self):
        # implementați calculul vârstei aici
        pass

    def calculateSalary(self):
        # implementați calculul salariului aici
        pass

    # Getteri și setteri cu property() și decoratori
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if re.match("^[a-zA-Z ]+$", value):
            self._name = value
        else:
            raise ValueError("Invalid name format")

    # Alți getteri și setteri pentru celelalte proprietăți


class HourlyEmployee(Employee):
    def __init__(self, name, phone, birth_date, email, specialty, hourly_rate):
        super().__init__(name, phone, birth_date, email, specialty)
        self._hourly_rate = hourly_rate

    def calculateSalary(self, hours_worked):
        return self._hourly_rate * hours_worked

    # Alte metode specifice angajatului cu plată pe oră


class SalaryEmployee(Employee):
    def __init__(self, name, phone, birth_date, email, specialty, monthly_salary):
        super().__init__(name, phone, birth_date, email, specialty)
        self._monthly_salary = monthly_salary

    def calculateSalary(self):
        return self._monthly_salary

    # Alte metode specifice angajatului cu salariu fix