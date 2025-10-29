class Employee:
    """Родительский класс для сотрудника с именем и базовой зарплатой."""

    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        """Возвращает базовую зарплату сотрудника."""

        return self.base_salary
    
    def __str__(self):
        """Информация о сотруднике"""

        return f"Сотрудник: {self.name}, зарплата: {self.calculate_salary()}"

class Manager(Employee):
    """Класс менеджера, наследует Employee и добавляет бонус к зарплате."""

    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        """Возвращает зарплату менеджера с учётом бонуса."""

        return self.base_salary + self.bonus
    
class Developer(Employee):
    """Класс разработчика, наследует Employee и использует коэффициент для расчёта зарплаты."""

    def __init__(self, name, base_salary, coefficient):
        super().__init__(name, base_salary)
        self.coefficient = coefficient

    def calculate_salary(self):
        """Возвращает зарплату менеджера с учётом бонуса."""

        return int(self.base_salary * self.coefficient)
    
    

staff_manager = Manager('Андрей', 100_000, 20_000)
staff_developer = Developer('Никита', 100_000, 1.3)
staff_employee = Employee('Джон', 50_000)

print(staff_manager)
print(staff_developer)
print(staff_employee)