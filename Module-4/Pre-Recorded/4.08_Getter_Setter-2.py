# Access Control


class Employee:
    company_name = "Ostad Platform"

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary


    def get_Salary(self, password):                         # get method --> to only get the salary
        if password == "admin":
            print("Salary is:", self._salary)
        else:
            print("Invalid Access")
    

    def set_Salary(self, password, salary):                 # set method ---> to update the salary
        if password == "admin":
            self._salary = salary
            print("Updated Salary:", self._salary)
        else:
            print("Invalid Access")




obj1 = Employee("Rahim", 33000)
obj2 = Employee("Karim", 98800)


obj1.get_Salary("123")                          # invalid password --> so the salary won't be Shown
obj1.set_Salary("123", 22000)                   # invalid password --> so the salary won't be updated