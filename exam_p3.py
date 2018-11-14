class Employee:
    """
    the base class
    """
    
    def __init__(self, name):
        self.name = name


    def get_name(self):
        return self.name
        

    def weekly_pay(self, hours_worked):
        return 0
 

class Nonexempt_Employee(Employee):

    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate

    # Overrides the superclass method.
    def weekly_pay(self, hours_worked):
        if hours_worked > 40:
            ot = (hours_worked - 40) * ((self.hourly_rate/2) + self.hourly_rate)
            rt = self.hourly_rate * 40 
            return ot + rt
        else:
            return self.hourly_rate * hours_worked


class Exempt_Employee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def weekly_pay(self, hourly_rate):
        return self.salary / 52

        


class Manager(Exempt_Employee):
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus
    
    def weekly_pay(self, hourly_rate):
        return (self.salary + self.bonus) / 52
    


def main():
    all_employees = []
    all_employees.append(Nonexempt_Employee("Aaron Wendell", 40.0))
    all_employees.append(Exempt_Employee("Alden Pexton", 60000.0))
    all_employees.append(Manager("Allison Fernandez", 94000.0, 50.0))
   

    for employee in all_employees:
        hours = int(input("Hours worked by " + employee.get_name() + ": "))
        pay = employee.weekly_pay(hours)
        print("Salary: ", pay)


if __name__ == '__main__':
    main()
