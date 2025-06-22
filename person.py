
class Person:

    def __init__(self, id, name, age, dict_data):
        self._id = id
        self._name = name 
        self._age = age
        self._dict_data = dict_data

    def getId(self):
        return self._id
    
    def getName(self):
        return self._name 
   
    def getAge(self): 
        return self._age
  
    
    def getDictionary(self):
        return self._dict_data
    
    def getPersonString(self): 
        str_print = "ID: " + self.getId() + "\n" + "Name: " + self.getName() + "\n"  +"Age: "  + self.getAge()
        return str_print

    def printMyself(self):
        print(self.getPersonString())

    
