class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")

def add_employee(employees):
    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    salary = input("Enter employee salary: ")
    employee = Employee(name, position, salary)
    employees.append(employee)

def view_employees(employees):
    for employee in employees:
        employee.display_info()
        print("---")

def update_employee(employees):
    name = input("Enter employee name to update: ")
    found = False
    for idx, employee in enumerate(employees):
        if employee.name == name:
            found = True
            new_position = input("Enter new position: ")
            new_salary = input("Enter new salary: ")
            employee.position = new_position
            employee.salary = new_salary
    if not found:
        print("Employee not found.")

def delete_employee(employees):
    name = input("Enter employee name to delete: ")
    found = False
    for idx, employee in enumerate(employees):
        if employee.name == name:
            found = True
            del employees[idx]
            break
    if not found:
        print("Employee not found.")

def main():
    employees = []
    while True:
        choice = input("""
        Employee Management System:
        1. Add employee
        2. View employees
        3. Update employee
        4. Delete employee
        5. Quit
        Enter your choice: """)
        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            view_employees(employees)
        elif choice == "3":
            update_employee(employees)
        elif choice == "4":
            delete_employee(employees)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()