from stringcolor import * 
class student():

    def __init__(self,name,age,address,id,phone,email,password,twjehimark):
        self.name = name
        self.age = age
        self.__password=password
        self.address= address
        self.__phone= phone
        self.__id=id
        self.__twjehimark =twjehimark
        self.email = email
        self.major=self.getMajoor(self.__twjehimark)
        

    def getID(self):
        return self.__id    

    def setID(self,newID):
        self.__id = newID
    majorList=[]        
    def getMajoor(self,mark):
        majorList=[]
        if mark >=90:
             majorList=['doctor','cs']
        elif  mark >=80:
           majorList=['eng','cs']
        elif mark>=70:
            majorList=['lawyer','cs']

        for i in range(len(majorList)):
            print(i+1,'-',majorList[i])
        choice=input('enter ur choice :') 
        major=majorList[int(choice)-1]
        return major
    def __readeMark(self):
        return self.getMajoor
    def getMark(self):
        return self.__readeMark   

print('hellow to our school')
name=input('enter your name : ')
age=input('enter your age : ')
id=input('enter your id : ')
phone=input('enter your phone : ')
address=input('enter your address : ')
email=input('enter your email : ')
password=input('enter your password : ')
twjehimark=int(input('Enter your twajehi mark: '))

student1=student(name,age,address,id,phone,email,password,twjehimark)
# student2=student('mosab',20,'address',151181,'0561334282','email','111',85.0)
student1.setID(122121122)
# print(student1.getID())   
print(cs(student1.getID(), "#ffff87"))   
# print(student1.major)
print(cs(student1.major, "DeepPink3"))   

