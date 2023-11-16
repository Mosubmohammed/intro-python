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
#     'sunday': {'welcome': 'welcome to the news website', 
#     'title': 'sunday news', 'content': ['the weather is 28 degrees']},
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
import re


# allpersons=[]
# person={}
# listOfBooks=[
#     {'name':'book1', 'author':'author1', 'pages':100,'price':100,'content':'this is the content of the book'},
#     {'name':'book2', 'author':'author2', 'pages':200,'price':200,'content':'this is the content of the book'},
#     {'name':'book3', 'author':'author3', 'pages':300,'price':300,'content':'this is the content of the book'}
# ]

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

words=[]
player1=input('enter the world :')
for i in player1:
    words.append('_')
print(words)    
player2=input('enter the character :')
while True:
    if player1.__len__==1:
            for i in player1:
                if i==player2:
                    words[i]=player2
                else:
                     print('else2')    
                    
    else:
        print('only one character')   
        break 
                     

