import traceback
import pandas as pd 
import os  
import json
from person import Person 
from student import Student
from employee import Employee
from operation import OperationType
from personType import PersonType

def printPersonTypes(set_types):
    for index, person_str in enumerate(set_types):
        print(str(index) + ". " + person_str)

def getPersonTypeEnum(input_type):
    person_type = PersonType.PERSON
    if input_type == "0":
        person_type = PersonType.PERSON
    elif input_type == "1":
        person_type = PersonType.STUDENT
    elif input_type == "2":
        person_type = PersonType.EMPLOYEE
    return person_type

def getPerson(person_type, dict_data):
    if person_type == PersonType.PERSON:
        person = Person(dict_data["id"], dict_data["name"], dict_data["age"], dict_data)
    elif person_type == PersonType.STUDENT:
        person = Student(dict_data["id"], dict_data["name"], dict_data["age"], dict_data["field of study"], dict_data["year of study"] , dict_data["score average"], dict_data)
    elif person_type == PersonType.EMPLOYEE:
        person =  Employee(dict_data["id"], dict_data["name"], dict_data["age"], dict_data["field of work"] , dict_data["salary"], dict_data)
    return person

def getInputByPersonType(person_type, dict_entries_by_Id):
    id = input("ID: ")
    if id.isdigit() == False:
        print("Error: ID must be a number." + " " + id + " is not a number")
        return 
    if id in dict_entries_by_Id:
        print("Error: ID already exists: " + str(dict_entries_by_Id[id]))
        return 
    name = input("Name: ")
    age = input("Age: ")
    if age.isdigit() == False:
        print("Error: Age must be a number." + " " + age + " is not a number")
        return 
    
    dict_data = {"id" : id, "name" : name, "age" : age}
    
    if person_type == PersonType.STUDENT:
        field_of_study = input("Field of study: ")
        year_of_study = input("Year of study: ")
        if year_of_study.isdigit() == False:
            print("Error: year of study must be a number." + " " + year_of_study + " is not a number")
            return 
        score_average = input("Score average: ")
        if score_average.isdigit() == False:
            print("Error: score average must be a number." + " " + score_average + " is not a number")
            return 
        
        dict_data["field of study"] = field_of_study
        dict_data["year of study"] = year_of_study
        dict_data["score average"] = score_average 

    elif person_type == PersonType.EMPLOYEE:
        field_of_work = input("Field of work: ")
        salary = input("Salary: ")
        if salary.isdigit() == False:
            print("Error: Salary must be a number." + " " + salary + " is not a number")
            return
        dict_data["field of work"] = field_of_work
        dict_data["salary"] = salary
    
    return dict_data
    

def saveNewEntry(list_ids, dict_entries_by_Id, dict_age_average):
    
    types = ("Person", "Student", "Employee")


    printPersonTypes(types)
    input_type = input("Please enter your choice number: ")
    if int(input_type) < 0 or int(input_type) > 2: 
        print("Error: Type entered " + input_type + " is not one of the options")
        return 
    
    person_type = getPersonTypeEnum(input_type) 

    dict_data = getInputByPersonType(person_type, dict_entries_by_Id)
    if dict_data == None:
        return 
        
    person = getPerson(person_type, dict_data)
    
    dict_entries_by_Id[person.getId()] = person
    list_ids.append(person.getId())
    dict_age_average["sum"] = dict_age_average["sum"] + int(person.getAge())
    dict_age_average["number_of_people"] = len(list_ids)
    print("ID " + "[" + person.getId() + "]" + " " + "saved successfuly")


def calculateAverage(dict_age_average):
    if(dict_age_average["number_of_people"] != 0): 
        average = dict_age_average["sum"] / dict_age_average["number_of_people"]
    else: 
        average = 0
    dict_age_average["average"] = average

def printAgesAverage(dict_age_average):
    calculateAverage(dict_age_average)
    print(dict_age_average["average"])
   
def searchById(dict_entries_by_Id):
    input_user_id = input("Please enter the ID you want to look for: ")
    if input_user_id.isdigit() == False:
        print("Error: ID must be a number." + " " + input_user_id + " is not a number")
        return 
    if  input_user_id not in dict_entries_by_Id:
        print("Error: ID " +  input_user_id + "is not saved")
        return 
    printEntry(dict_entries_by_Id, input_user_id)

def printEntry(dict_entries_by_Id, id):
    person = dict_entries_by_Id[id]
    person.printMyself()

def printAllNames(list_ids, dict_entries_by_Id):
    for index, id in enumerate(list_ids):
        print(str(index) + ". " + dict_entries_by_Id[id].getName())

def printAllIds(list_ids):
     for index, id in enumerate(list_ids):
        print(str(index) + ". " + id)

def printAllEntries(list_ids, dict_entries_by_Id):
      for index, id in enumerate(list_ids):
        print(str(index) + ". ")
        printEntry(dict_entries_by_Id, id)

def printEntryByIndex(list_ids, dict_entries_by_Id):
    input_user_index = input("Please enter the index of the entry you want to print: ")
    if input_user_index.isdigit() == False:
        print("Error: index must be a number." + " " + input_user_index + " is not a number")
        return 
    if int(input_user_index) < 0 or int(input_user_index) >= len(list_ids):
        print("Error: index out of range. The maximum index allowed is " + str(len(list_ids) - 1))
        return 
    id_str = list_ids[int(input_user_index)]
    printEntry(dict_entries_by_Id, id_str)

def createDictData(dict_entries_by_Id):
    list_dict_datas = []

    for person in dict_entries_by_Id.values():
        list_dict_datas.append(person.getDictionary())
    return list_dict_datas

def writeToCsv(path_current, output_name, dict_data): 
    sufix = ".csv"
    if output_name.endswith(sufix) == False:
        output_name = output_name + sufix

    df = pd.DataFrame(dict_data)
    path = path_current + "\\" + output_name
    df.to_csv(path)

def saveAllDataToCsv(dict_entries_by_Id):
    
    output_name = input("What is your output file name? ")
    path_current = os.getcwd()
  
    list_dict_datas = createDictData(dict_entries_by_Id)
    
    writeToCsv(path_current, output_name, list_dict_datas)


def runOperation(operation, list_ids, dict_entries_by_Id, dict_age_average):
    if operation == OperationType.SAVENEWENTRY:
       saveNewEntry(list_ids, dict_entries_by_Id, dict_age_average)
    elif operation == OperationType.SEARCHBYID:
        searchById(dict_entries_by_Id)
    elif operation == OperationType.PRINTAGESAVERAGE:
        printAgesAverage(dict_age_average)
    elif operation == OperationType.PRINTALLNAMES:
        printAllNames(list_ids, dict_entries_by_Id)
    elif operation == OperationType.PRINTALLIDS: 
        printAllIds(list_ids)
    elif operation == OperationType.PRINTALLENTRIES: 
        printAllEntries(list_ids, dict_entries_by_Id)
    elif operation == OperationType.PRINTENTRYBYINDEX: 
        printEntryByIndex(list_ids, dict_entries_by_Id)
    elif operation == OperationType.SAVEALLDATATOCSV:
        saveAllDataToCsv(dict_entries_by_Id)
    input_continue = input("Press enter to continue ")

def getOperationEnum(input_user):
    
    operation = OperationType.SAVENEWENTRY
    if input_user == "1":
       operation = OperationType.SAVENEWENTRY
    elif input_user == "2":
        operation = OperationType.SEARCHBYID
    elif input_user == "3":
        operation = OperationType.PRINTAGESAVERAGE
    elif input_user == "4":
        operation = OperationType.PRINTALLNAMES
    elif input_user == "5": 
        operation = OperationType.PRINTALLIDS
    elif input_user == "6": 
        operation = OperationType.PRINTALLENTRIES
    elif input_user == "7": 
        operation = OperationType.PRINTENTRYBYINDEX
    elif input_user == "8":
        operation = OperationType.SAVEALLDATATOCSV
    elif input_user == "9":
        operation = OperationType.EXIT
    
    return operation

def isNumber(input_user):
    if input_user.isdigit() == False:
        raise ValueError("Error: input must be a number." + " " + input_user + " is not a number")

def isOutOfBounds(input_user, list_menu_str):
    if int(input_user) > len(list_menu_str) or int(input_user) <= 0: 
        raise IndexError("Error: input is out of range." + "[" + input_user + "]" + "is out of range")


def printMenu(list_menu_str):
    for index, item in enumerate(list_menu_str):
        print(str(index + 1) + ". " + item)


def exitCheck(): 
        while True:
            input_exit = input("are you sure? y/n ")
            if input_exit == "y":
                exit = True
                return exit
            elif input_exit == "n":
                exit = False
                return exit


def main():
    list_menu_str = [
        "Save a new entry",
        "Search by ID", 
        "Print ages average", 
        "Print all names", 
        "Print all IDs", 
        "Print all entries", 
        "Print entry by index", 
        "Save all data",
        "Exit"
        ]
    
    dict_entries_by_Id = {}
    dict_age_average = {"sum": 0, "average": 0, "number_of_people": 0}
    exit_operation = OperationType.EXIT
    list_ids = []
    exit = False
    try:
        while True: 
            
            try: 
                printMenu(list_menu_str) 
                input_user = input("Please enter your choice: ") 
                isNumber(input_user)
                isOutOfBounds(input_user, list_menu_str)
                operation = getOperationEnum(input_user)

                if operation != exit_operation:
                    runOperation(operation, list_ids, dict_entries_by_Id, dict_age_average)
                elif operation == exit_operation: 
                    exit = exitCheck()
                
                if  exit:
                    print("Goodbye") 
                    break 
          
            except IndexError:
                print("Error: input is out of range. " + "[" + input_user + "] " + "is out of range")
            except ValueError:
                print("Error: option must be a number." + " " + input_user + " is not a number") 
    except KeyboardInterrupt:
        print("Goodbye")
    
main()





    












