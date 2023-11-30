import os
import json

# print('hello')


# name="""
# mosab
# mophammed
# gazy
# """
# print(name)

# num1=5
# print(num1)

# num2=2.5
# print(num2)

# listP=['a','b','c','d']
# print(listP)    

# tb=(11,22,334,55,66)
# print(tb)

# person={
#     'name':'mosab',
#     'age':20,
#     'country':'jordan',
#     'skiills':['cp','java']

# }
# print(person)
# print(person['skiills'])


# list=[1,2,3,4,5]
# for i in list:
#     print(i)

# x=23
# for i in range(0,14,3):
#     print(i)

# person={
#     'name':'mosab',
#     'age':20,
#     'country':'jordan'
# }
# for i in person:
#     print(i,':',person[i])


# news={
#     'sunday':['welcome':'welcome to the news website','title':'sunday news','content':['the wether the 28 degrees']],
#     'monday':['welcome':'welcome to the news website','title':'monday news','content':['the wether the 35 degrees']],
#     'tuesday':['welcome':'welcome to the news website','title':'tuesday news','content':['the wether the 40 degrees']]
#     }


# if True:
#     print('myaw')
# else:
#     print('else')


# import numbers


# choose1=input('enter your choice : ')

# if choose1.isdigit():
#     print(choose1)
    
# else:
#     print('Please enter num2 ')

# i=0
# for i in range(11):
#     if i % 2==0:
#         print(i)
#     else:
#         print('odd')

# num=input('Enter a number : ')


# if num%2==0:
#     print('even')
# # else:
# #     print('odd')    



# news = {
#     'sunday': {'welcome': 'welcome to the news website', 'title': 'sunday news', 'content': ['the weather is 28 degrees']},
#     'monday': {'welcome': 'welcome to the news website', 'title': 'monday news', 'content': ['the weather is 35 degrees']},
#     'tuesday': {'welcome': 'welcome to the news website', 'title': 'tuesday news', 'content': ['the weather is 40 degrees']}
# }

# for i in news:
#     print(i,':',news[i])

    

# def myFunction():
#     print('my function')

# myFunction()

# def myFunction(name,name2):
#     print(name,name2)

# myFunction('hq','mohjammed')    


# def myFunction():
#     return print('my function111')

# myFunction()
# print(myFunction)

# num1=int(input('pleses enter ur firrsst num : '))
# num2=int(input('pleses enter ur sconde1 num : '))
# def numbers(num1,num2):
#     return num1 + num2

# print(numbers(num1,num2))

# i=0
# wileTest=True
# while wileTest:
    
#     if i==5:
#         i+=1
#         continue
#     print(i)
#     i+=1
#     if i==10:
#         break
# i=1
# while i:
#     i+=1
#     print(i)
#     if i==10:
#         break


# name=input('enter ur name : ')   
# print(name)

# allpersons=[]
# person={}
# print("welcome to out app")
# while True:
#     print('__'*20)
#     print("1-addd new person")
#     print("2-see all persons")
#     print("3-exit")
#     choice=input('enter ur choice :')
#     if choice=='1':
#         name=input("Enter the person name : ")
#         while True:
#             age =input( "enter the person age : ")
#             if age.isdigit():
#                 age=int(age)
#                 break
#             else:
#                 print("please enter a number for age")
#         job=input('enter the person job :')
#         person['name']=name
#         person['age']=age
#         person['job']=job
#         allpersons.append(person)
#         print("you added person successfully")
#     elif choice=='2':
#        counter=1
#        print('__'*20)
#        print("all persons")
#        for i in allpersons:
#           print("person",":",counter)
#           for key in i:
#               print("   ",key,":",i[key])
#               counter+=1
#     elif choice=='3':
#         print("thanks for using our app")
#         break
    


# try:
#     print('0')
# except print(0):
#     pass    



# allpersons=[]
# person={}
# print("welcome to out app")
# while True:
#     print('__'*20)
#     print("1-addd new person")
#     print("2-see all persons")
#     print("3-exit")
#     choice=input('enter ur choice :')
#     if choice=='1':
#         name=input("Enter the person name : ")
#         while True:
#             try:
#                 age =int(input( "enter the person age : "))
#                 break
#             except:
#                 print("please enter a number for age")

#         job=input('enter the person job :')
#         person['name']=name
#         person['age']=age
#         person['job']=job
#         allpersons.append(person)
#         print("you added person successfully")
#     elif choice=='2':
#        counter=1
#        print('__'*20)
#        print("all persons")
#        for i in allpersons:
#           print("person",":",counter)
#           for key in i:
#               print("   ",key,":",i[key])
#               counter+=1
#     elif choice=='3':
#         print("thanks for using our app")
#         break


# list1=[{"new2":"new"},{"new3":"new"},{"new4":"new"}]
# dic1={"dic1":"dic1"}
# dic2={"dic2":"dic2"}
# list1.insert(0,dic1)
# print(list1)

# list1.insert(3,dic2)
# print(list1)

# list1.sort(dic2)

# list3=['aa','ab','at','5','h','7','t','q','c','7']
# # list3.sort()
# print(list3)

# # list3.reverse()
# print(list3)

# print(list3.count('7'))
# print(list3.__len__())

# # list3.clear()
# # print(list3)
# # print(list3.__len__())

# # list3.remove()

# list3.pop(7)
# print(list3)

# dic1={
#     'name': 'ahmed',
#     'age':'33',
#     'jobs':'softwwares',
#     'skills':['cpp',
#               'javascript','python']
# }
# print(dic1.keys())
# print(dic1.values())
# print(dic1.items())
# print(dic1.get('age'))
# dic1['name']='mosab'
# print(dic1.get('name'))
# dic1['skills'].append('html')
# dic1['skills'].remove('javascript')
# dic1['skills'].insert(1,'css')
# print(dic1)

# and password=='@-_#$%&*' and password=='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# import re


# allpersons=[]
# person={}
# # listOfBooks=[
# #     {'name':'book1', 'author':'author1', 'pages':100,'price':100,'content':'this is the content of the book'},
# #     {'name':'book2', 'author':'author2', 'pages':200,'price':200,'content':'this is the content of the book'},
# #     {'name':'book3', 'author':'author3', 'pages':300,'price':300,'content':'this is the content of the book'}
# # ]

# print("welcome to out app")
# while True:
#     print('__'*20)
#     print("1-create account")
#     print("2-login")
#     print("3-exit")
#     print('4-show all persons')
#     choice=input('enter ur choice :')
#     if choice=='1':
#         name=input("Enter the user name : ")
#         if allpersons !=[]:
#             isExi=True
#             while isExi:
#                 for i in allpersons:
#                     if name==i['name']:
#                         print('this name is already exist')
#                         name=input("Enter the user name : ")
#                         isExi=True
#                         break
#                     else:
#                         isExi=False
                    
#         while True:
#             try:
#                 age =int(input( "enter the user age : "))
#                 break
#             except:
#                 print("please enter a number for age")

#         job=input('enter the user job :')
#         skills=[]
#         while True:
#             try:
#                 counter2=int(input('enter the number of skills :'))
#                 break
#             except Exception as e:
#                 print('please enter a valid number')
#                 continue

#         for i in range(counter2):
#             print('enter the skills number ',i+1,':')
#             skills.append(input())

#         uppercasse1=False
#         lowercase=False
#         numbers=False
#         while True:
#             password=input("Enter the user password : ")
#             if len(password)>=8:
#                 for i in password:
#                     if i.isupper():
#                         uppercasse1=True
#                     elif i.islower():
#                         lowercase=True
#                     elif i.isdigit():
#                         numbers=True
#                 if uppercasse1 and lowercase and numbers:
#                     print('the password is strong') 
#                     break
#                 else:
#                     if uppercasse1!=True:
#                         print('the password dont have a uppercase') 
#                     if lowercase!=True:
#                         print('the password dont have a lowercase')  
#                     if numbers!=True:
#                         print('the password dont have a numbers')           
                    
#             else:
#                 print('the password is shorter than 8')                           

                            
#         person={
#             'name':name,
#             'age':age,
#             'job':job,
#             'password':password
#         }
#         allpersons.append(person)
#         print("you added person successfully")
#     elif choice=='2': 
#        print("__"*20)
#        print('please enter ur name and ur password :')
#        name=input('Enter the name :')
#        password=input('Enter the password :')
#        for i in allpersons:
#            if i['name']==name and i['password']==password:
#                print('welcome',name)
#                userChoose=input('**u can update ur info do u wanna update it yes or no**')  
#                if userChoose=='yes': 
#                    print('1-name')
#                    print('2-password')
#                    print('3-job')
#                    print('4-age')
#                    print('5-Exit')
#                    choice2=input('inter ur choice :')
#                    if choice2=='1':
#                        print('enter ur new name :')
#                        person['name']=input()
#                    elif choice2=='2':
#                             print('enter ur new password :')
#                             person['password']=input()
#                    elif choice2=='3':
#                        print('enter ur new job :')
#                        person['job']=input()
#                    elif choice2=='4':
#                        print('enter ur new age :')
#                        person['age']=input() 
                 
#            else:
#             print('the name or password is incorrect')

#        print('do you wanna add new filed')
#        userChoose2=input('Enter the yes or no :')
#        if userChoose2=='yes':
#             userfiled=input('please Enter your new filed type:')


#             if userfiled=='int':
#                     userfiled2=input('Enter the filed name :')
#                     while True:
#                         try:
#                             userfilrdint=int(input('Enter the filed value :'))
#                             # print(userfiled2+' is:  '+userfilrdint)
#                             print('thanks for adding new filed') 
#                             break
#                         except Exception as e:
#                             print('please enter a valid number') 


#             elif userfiled=='string':
#                 userfiled3=input('Enter the filed name :')
#                 userfilrdString=input('Enter the filed value :')
#                 print(userfiled3+' is:  '+userfilrdString)
#                 print('thanks for adding new filed')


#             elif userfiled=='list':
#                     userfiled2=input('Enter the filed name :')
#                     userChoose3=input('please int the type of ur list')
#                     listUser=[]

#                     if userChoose3=='string':      
#                         Usercounter=int(input('enter the number of ur ......:'))
#                         for i in range(Usercounter):
#                             print('please enter ur ..... ',i+1,':')
#                             listUser.append(input())
#                         print('thanks for adding new filed') 
#                     elif userChoose3=='int':
                        
#                         Usercounter2=int(input('enter the number of ur ......:'))
#                         for i in range(Usercounter2):
#                             print('please enter ur ..... ',i+1,':')
#                             listUser.append(input())
#                         print('thanks for adding new filed') 

                        
#                     elif userChoose2=='no':
#                         break           
       
#        print('__'*20)
#        print('1-read book')
#        print('2-add book')
#        print('3-buy book')
#        choiceBook=input('enter ur choice')
#        if choiceBook=='1':
#            listBooks=[]
#            for i in listOfBooks:
#                listBooks.append(i['name'])
#            for i in range(len(listBooks)):
#                print(i+1,'-',listBooks[i])
#            xChoice=input('enter ur choice :')
#            print(listOfBooks[int(xChoice)-1]['content'])
#        elif choiceBook=='2':
#            newBook={}
#            name=input('inter the name of the book')
#            author=input('enter the author of the book')
#            pages=input('inter the pages of the book')
#            price=input('enter the price of the book')
#            content=input('inter the content of the book')
#            newBook['name']=name
#            newBook['author']=author
#            newBook['pages']=pages
#            newBook['price']=price
#            newBook['content']=content
#            listOfBooks.append(newBook)
#     elif choice=='3':
#         print("thanks for using our app")
#         break
#     elif choice=='4':
#         isAdmin=input('please enter admin password :')
#         if isAdmin=='myaw':
#             counter=1
#             print('__'*20)
#             print("all persons")
#             for i in allpersons:
#                 print("person",":",counter)
#             for key in i:
#                 print("   ",key,":",i[key])
#                 counter+=1
#         else:
#            print('wrong pass') 
#     else:
#         print('wrong choice')


# testStr='hello world'

# def replaceL(foundl):
#     beforeE=[]
#     for i in foundl:
#         if i=='l':
#             beforeE.append('*')
#     else:
#         beforeE.append(i)    
#     afterE=''
#     for i in beforeE:
#         afterE+=i
#     return afterE
# print(replaceL(testStr))    

# player1=input('choice a world :')
# list1=[]
# tryes=(len(player1))
# for i in range(len(player1)):
#     list1+='_'
# print(list1)
# gameOver=True
# while gameOver:
#     player2=input('choice a character: ')
#     for i in range(len(player1)):
#         char=player1[i]
#         if char==player2:
#             list[i]=player2   
#     if player2 not in player1:
#         tryes-=1
#         if tryes==0:
#             print('game over')
#             break

# words=[]
# player1=input('enter the world :')
# for i in player1:
#     words.append('_')
# print(words)    
# player2=input('enter the character :')
# while True:
#     if player1.__len__==1:
#             for i in player1:
#                 if i==player2:
#                     print('2')
#                 else:
#                      print('else2')    
                    
#     else:
#         print('only one character')   
#         break 
                     

# class Person:
#     name='mosab'
#     phone='0561334282'
#     age=20
#     city='irbid'
# person1=Person()
# print(person1.city)     


# class Person():

#     def __init__(self, name, phone,age, city,pass): 
#         self.name=name
#         self.phone=phone
#         self.age=age
#         self.city=city
#         self.passwoord=pass
    
#     def nameAndPhone(self):
#         return f'name:{self.name},phone:{self.phone}'
#     def eatingWith(self,nameP):
#         return f'{self.name} is eating with {nameP}'
#     def __str__(self):
#         return f'name: {self.name} ,phone: {self.phone} ,age:{self.age} ,city:{self.city}'
# Person1=Person(age=20,name='khalid',phone=11111111,city='irbid')
# Person2=Person(age=30,name='mosab',phone=222222,city='amman')
# def checkpass(password):

# print(Person1.nameAndPhone())
# print(Person2.eatingWith('malak'))

# ! read a text file and save the var inside this txt file 

# database = open('./databse.txt','w' )
# print(database.write('hi iam from jordan'))
# database = open('./databse.txt','r' )
# print(database.read())


# def loadData():
#     try:
#         with open('./databse.txt','r')as file:
#             json.load(file)
#         return file
#     except Exception as e:
#         print(e)
# print(loadData())        

    
# def saveData(data):
#     with open('./databse.txt','w') as file:
#         json.dump(data,file)
#     print('data saved',data)    

# x={'mosab':'20'}
# saveData(x)



# class student():

#     def __init__(self,name,age,address,id,phone,email,password,twjehimark):
#         self.name = name
#         self.age = age
#         self.__password=password
#         self.address= address
#         self.__phone= phone
#         self.__id=id
#         self.__twjehimark =twjehimark
#         self.email = email
#         self.major=self.getMajoor(self.__twjehimark)
        

#     def getID(self):
#         return self.__id    

#     def setID(self,newID):
#         self.__id = newID
#     def getMajoor(self,mark):
#         majorList=[]
#         if mark >=90:
#              majorList=['doctor','cs']
#         elif  mark >=80:
#            majorList=['eng','cs']
#         elif mark>=70:
#             majorList=['lawyer','cs']

#         for i in range(len(majorList)):
#             print(i+1,'-',majorList[i])
#         choice=input('enter ur choice :') 
#         major=majorList[int(choice)-1]
#         return major
#     def __readeMark(self):
#         return self.getMajoor
#     def getMark(self):
#         return self.__readeMark   

# print('hellow to our school')
# name=input('enter your name : ')
# age=input('enter your age : ')
# id=input('enter your id : ')
# phone=input('enter your phone : ')
# address=input('enter your address : ')
# email=input('enter your email : ')
# password=input('enter your password : ')
# twjehimark=int(input('Enter your twajehi mark: '))

# student1=student(name,age,address,id,phone,email,password,twjehimark)
# # student2=student('mosab',20,'address',151181,'0561334282','email','111',85.0)
# student1.setID(122121122)
# print(student1.getID())     
# print(student1.major)


# class Teacher:
#     def __init__(self, name2, age2, major2, phone2, address2, email2, id2, password2):
#         self.name2 = name2
#         self.age2 = age2
#         self.major2 = major2
#         self.phone2 = phone2
#         self.address2 = address2
#         self.email2 = email2
#         self.__password2 = password2
#         self.__id2 = id2
#         self.__studentList = []

#     def addStudent(self, student):
            
#             if student.major == self.major2:
#                 self.__studentList.append(student)
#             else:
#                 print("Cannot add a student with a different major.")

#     def getStudentList(self):
#         return self.__studentList
      
# teacher1=Teacher('ahmed',35,'cs','0561334282','irbid','mosup.050@gmail.com','151181','123456')
# teacher1.addStudent(student1)
# teacherList = teacher1.getStudentList()
# for student in teacherList:
#     print(student.name)


 # ! example polymorphism

# class animal():
#     def __init__(self,name):
#         self.name=name
#     def makeSounf(self):
#             print('iam animal')

# class dog(animal):
#     def __init__(self,name):

# from pacage1 import *

# pac11=pac1('iam form main')
# pa22=pac2('iam pac22 form main file')

# import emojis

# emojis.encode('This is a message with emojis :smile: :snake:')


# emojis.decode('This is a message with emojis 😄 🐍')


# emojis.get('Prefix 😄 🐍 😄 🐍 Sufix')
# {'😄', '🐍'}

# emojis.count('😄 🐍 😄 🐍')


# emojis.count('😄 🐍 😄 🐍', unique=True)


# emojis.db.get_emoji_by_alias('snake')


# emojis.db.get_categories()
# {'Activities', 'Travel & Places', 'Smileys & Emotion', 'Symbols', 'Food & Drink', 'Animals & Nature', 'People & Body', 'Objects', 'Flags'}
# mo=emojis.encode(':snake:')
# print(mo)

# from stringcolor import * 
# print(cs("here we go", "orchid"))   

class vehicle():

    def __init__(self,brand,fuelType,milege):
        self.brand = brand
        self._fuelType=fuelType
        self.__milege=milege

    def getFuelType(self):
        return self._fuelType
    
    def set_fuel_type(self, fuel_type):
        self._fuelType=fuel_type

    def get_mileage(self):    
        return self.__milege
    def update_mileage(self, miles):
        self.__milege=miles


class car(vehicle):    
    def __init__(self, brand, fuel_type, mileage, model):
        super().__init__(brand,fuelType,)