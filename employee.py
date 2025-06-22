
from person import Person

class Employee(Person):
    def __init__(self, id, name, age, field_of_work, salary, dict_data):
        super().__init__(id, name, age, dict_data)
        self._field_of_work = field_of_work
        self._salary = salary 
       
        
    def getFiledOfWork(self):
        return self._field_of_work 
    
    def getSalary(self):
        return self._salary 
    
  
    def printEmployee(self):
        print_str = self.getPersonString() + "\n" + "Field of work: " + self.getFiledOfWork() + "\n" +"Salary: " + self.getSalary()
        print(print_str)
    
    def printMyself(self): 
        self.printEmployee()
