class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary
    
    def __str__(self):
        return f"Сотрудник: {self.name}, зарплата: {self.calculate_salary()}"
