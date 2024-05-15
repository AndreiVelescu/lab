import re
from datetime import datetime


class Employee:
    def __init__(self, name, phone, birth_date, email, specialty, monthly_salary=None):
        self.name = name
        self.phone = phone
        self.birth_date = birth_date
        self.email = email
        self.specialty = specialty
        self.monthly_salary = monthly_salary

    def calculateAge(self):
        today = datetime.now()
        birth_date = datetime.strptime(self.birth_date, '%Y-%m-%d')
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    


class HourlyEmployee(Employee):
    def __init__(self, name, phone, birth_date, email, specialty, hourly_rate):
        super().__init__(name, phone, birth_date, email, specialty)
        self.hourly_rate = hourly_rate

    def calculateSalary(self, hours_worked):
        return self.hourly_rate * hours_worked

    # Alte metode specifice angajatului cu plată pe oră


class SalaryEmployee(Employee):
    def __init__(self, name, phone, birth_date, email, specialty, monthly_salary):
        super().__init__(name, phone, birth_date, email, specialty)
        self.monthly_salary = monthly_salary

    def calculateSalary(self):
        return self.monthly_salary
