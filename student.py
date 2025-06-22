from person import Person

class Student(Person):
    def __init__(self, id, name, age, field_of_study, year_of_study, score_avg, dict_data):
        super().__init__(id, name, age, dict_data)
        self._field_of_study = field_of_study
        self._year_of_study = year_of_study 
        self._score_avg = score_avg
        
       
    
    def getFiledOfStudy(self):
        return self._field_of_study 
    
    def getYearOfStudy(self):
        return self._year_of_study 
    
    def getScoreAvg(self):
        return self._score_avg
    
    
    def printStudent(self):
        str_print = self.getPersonString() + "\n" + "Field of study: " + self.getFiledOfStudy() + "\n" + "Year of study: " + self.getYearOfStudy() + "\n"  +"Score average: "  + self.getScoreAvg()
        print(str_print)
            
    def printMyself(self): 
        self.printStudent()

