from stringcolor import * 
from student import *
class Teacher:
    def __init__(self, name2, age2, major2, phone2, address2, email2, id2, password2):
        self.name2 = name2
        self.age2 = age2
        self.major2 = major2
        self.phone2 = phone2
        self.address2 = address2
        self.email2 = email2
        self.__password2 = password2
        self.__id2 = id2
        self.__studentList = []

    def addStudent(self, student):
            
            if student.major == self.major2:
                self.__studentList.append(student)
            else:
                print("Cannot add a student with a different major.")

    def getStudentList(self):
        return self.__studentList
      
teacher1=Teacher('ahmed',35,'cs','0561334282','irbid','mosup.050@gmail.com','151181','123456')
teacher1.addStudent(student1)
teacherList = teacher1.getStudentList()
for student in teacherList:
    # print(student.name)
    print(cs(student.name, "orchid"))  

