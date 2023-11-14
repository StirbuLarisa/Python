class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        return f"{self.name}, Employee ID: {self.employee_id}"

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id)
        self.salary = salary
        self.department = department

    def display_info(self):
        return f"{super().display_info()}, Salary: ${self.salary}, Department: {self.department}"

    def conduct_meeting(self):
        return f"{self.name} is conducting a meeting."

class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def display_info(self):
        return f"{super().display_info()}, Salary: ${self.salary}, Programming Language: {self.programming_language}"

    def write_code(self):
        return f"{self.name} is writing code in {self.programming_language}."

class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id)
        self.salary = salary
        self.sales_target = sales_target

    def display_info(self):
        return f"{super().display_info()}, Salary: ${self.salary}, Sales Target: ${self.sales_target}"

    def make_sale(self):
        return f"{self.name} made a sale exceeding the target."

# Example usage:
manager = Manager("Ana", "M001", 80000, "Marketing")
engineer = Engineer("Ion", "E001", 70000, "C#")
salesperson = Salesperson("Maria", "S001", 60000, 100000)

print(manager.display_info())
print(manager.conduct_meeting())

print(engineer.display_info())
print(engineer.write_code())

print(salesperson.display_info())
print(salesperson.make_sale())
