class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_pay(self):
        return self.salary + self.bonus


# --- Test ---
employee = Employee("Alex", 1000)
manager = Manager("Sarah", 1000, 300)

print("Employee pay:", employee.calculate_pay())
# Expected: 1000

print("Manager pay:", manager.calculate_pay())
# Expected: 1300
