# Levi VonBank

## Creates a class employee with a name and salary
class Employee:
    def __init__(self, name, salary):
        self._name = name
        # Checks if salary is a valid number
        try:
            newSalary = float(salary)
            self._salary = round(newSalary, 2)
        except ValueError:
            raise ValueError("Salary isn't a valid number")
    
    ## Returns the employees name
    def getName(self):
        return self._name
    
    ## Returns employees salary
    def getSalary(self):
        return self._salary
    
    ## Enables the change of a salary
    def setSalary(self, salary):
        try:
            newSalary = float(salary)
            self._salary = round(newSalary, 2)
        except ValueError:
            raise ValueError("Salary isn't a valid number")
    
    ## A representation of the employee
    def __repr__(self):
        return "Employee " + str(self._name) + \
        " receives a salary of $" + str(self.getSalary())

## Creates a class Manager with a department and title (inherits from Employee)
class Manager(Employee):
    def __init__(self, name, salary, department = ""):
        super().__init__(name, salary)
        self._department = str(department)
      
    ## Enables the change or addition of a department
    def setDepart(self, department):
        self._department = str(department)
    
    ## Returns a department string
    def getDepart(self):
        return self._department
    
    ## Helper method for __repr__()
    # determines the department applicability
    def _departStr(self):
        departStr = ""
        if not self._department == "":
            departStr = " of " + str(self._department)
        return departStr
    
    ## A representation of the Manager
    def __repr__(self):
        return "Manager " + str(self.getName()) + self._departStr() \
        + " receives a salary of $" + str(self.getSalary())

## Creates a class Executive with a new title (inherits from Manager)
class Executive(Manager):
    def __init__(self, name, salary, department = ""):
        super().__init__(name, salary, department)
        self._department = str(department)
    
    ## A representation of the Executive
    def __repr__(self):
        return "Executive " + str(self.getName()) + self._departStr() \
        + " receives a salary of $" + str(self.getSalary())

if __name__ == "__main__":
    employees = []
    employees.append(Employee('John', 5050))
    employees.append(Manager('Larry', 8000, 'Customer Service'))
    employees.append(Executive('Jarry', 100000))
    
    for employee in employees:
        print(employee)
    print()
    
    employees[0].setSalary(6000)
    print(employees[1].getName())
    print(employees[1].getSalary())
    print(employees[1].getDepart())
    employees[2].setDepart("Accounting")
    print()

    for employee in employees:
        print(employee)
    print()    