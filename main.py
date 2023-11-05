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


allpersons=[]
person={}
print("welcome to out app")
while True:
    print('__'*20)
    print("1-addd new person")
    print("2-see all persons")
    print("3-exit")
    choice=input('enter ur choice :')
    if choice=='1':
        name=input("Enter the person name : ")
        while True:
            try:
                age =int(input( "enter the person age : "))
                break
            except:
                print("please enter a number for age")

        job=input('enter the person job :')
        person={
            'name':name,
            'age':age,
            'job':job
        }
        allpersons.append(person)
        print("you added person successfully")
    elif choice=='2':
       counter=1
       print('__'*20)
       print("all persons")
       for i in allpersons:
          print("person",":",counter)
          for key in i:
              print("   ",key,":",i[key])
              counter+=1
    elif choice=='3':
        print("thanks for using our app")
        break


