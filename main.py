# name=input('What is your name?')
# print('Hi ' +name)

# birth_year = input("Enter your birth_year:")
# print(type(birth_year))
# age=2022-int(birth_year)
# print(age)
# print(type(age))

                        # Type Casting
#
# weight_lbs = input("Enter the weight in (lbs)")
# weight_kg=int(weight_lbs)*0.45
# print(weight_kg)

                #HOW TO USE SINGLE QUOTES IN STRING CONTENT

# mgs="It's Amazing"
# print(mgs)

                #HOW TO USE DOUBLE QUOTES IN STRING CONTENT

# content = 'this is "Omkar"'
# print(content)

            #To Get the content as per the formatting

# msg= '''
# HI Omkar,
#     Welcome to CrossAsyst....
#          This is Omkar Rawool
# '''
# print(msg)


                                #Manipulating the String
#
# course='Python tutorial for beginners'
# print(course[0])
# print(course[3:-1])
#
# another=course[:]

# name='jennifer'
# print(name[1:-3])


                                    #Formatted Strings

# first="Omkar"
# last="Rawool"
# msg=f'{first} [{last}] is a coder......'
# print(msg)

                                #String Methods

# msg='India is my country'
# print(len(msg))
# print(msg.upper())     #INDIA IS MY COUNTRY
# print(msg)             #India is my country
# print(msg.find("country"))  #12
# print(msg.replace("India","Australia"))   #Australia is my country
# print('Indian' in msg)
# print(msg.title())  #India Is   My Country


                                #Arithmetic Operators
# print(10+3)    #13
# print(10%3)    #1
# print((10 ** 3))   #1000

                                    #SHORTHAND OPERATORS

# x=10
# x+=3
# print(x)         #13

                                #OPERATOR PRECEDENCE
# x= 10 + 3 * 2  #16
# print(x)

                                #MATH FUNCTIONS
# import math
# x=23.5
# print(round(x))    #24
#
# print(abs(-23.57))  #23.57
#
# print(math.ceil(22.12)) #23


                                #IF STATEMENTS
# is_hot=False
#
# if is_hot:
#      print("It's a hot day")
#      print("Enjoy Your Day..")
# else:
#     print("It's cold Today")
#
# print("End of the Statement")

# price=1000000
# good_credit=True
#
# if good_credit:
#     payment=price*0.01
# else:
#     payment=price*0.02
# print(f' Down Payment:{payment}')

#
# temp=9
# if temp>30:
#     print("it's a hot day...")
# elif temp<10:
#     print("it's a cold day...")
# else:
#     print("its neither hot nor cold..")


#                                       COMPARISON OPERATOR
#
# name=input("Enter your name")
# if len(name)<3:
#     print("name should be atleast 3 characters")
# elif len(name)>7:
#     print("name can be a maximum of 7 characters")
# else:
#     print("name looks good..🥳")

                                        #WEIGHT CONVERTER


# weight=input("Weight: ")
# key=input("(L)bs or (K)g: ")
# if key=="K" or key=="k":
#     value=f'{float(weight)*2.2}'            #Formatted String
#     print("Your weight is "+value+" Lbs.")
# elif key=="L" or key=="l":
#     value = f'{float(weight) / 2.2}'
#     print("Your weight is " + value+" Kg.")
# else:
#     print("Invalid selection..Please select L or K ")


                        #while loop

# i=1;
# while i<=5:
#     print("* "*i);
#     print()
#     i+=1

                        # Guessing Game


# secret_number=9;
#
# guess_count=0
# guess_limit=3
# while guess_count<guess_limit:
#     guess=int(input("Guess: "))
#     guess_count+=1
#     if guess==secret_number:
#       print('you won..')
#       break
#     else:
#         print("Sorry...You failed...")

                #Car Game
# command=""
# isStarted=False
# isStopped=True
# while True:
#     command=input("> ").lower()
#     if command=="start":
#         if isStarted:
#             print("Car is already Started")
#         else:
#             print("Car Started")
#             started=True
#     elif command=="stop":
#         if isStopped:
#             print("Car is already stopped")
#         else:
#             print("Car Stopped...")
#             isStopped=False
#     elif command=="help":
#         print("""
#         start => Car Started
#         stop => Car Stopped
#         Quit => To Quit
#
#         """)
#     elif command=="quit":
#         break
#
#     else:
#       print("Please enter Valid command")


                        #FOR LOOP
# for item in 'Python':
#     print(item)


# for item in ['Omkar','Balram','Shambhu']:
#     print(item)

# for item in range(5,10):
#     print(item)         # 5,6,7,8,9




# for item in range(5,10,2):
#     print(item)           #5,7,9


# prices=[10,20,30]
# total=0
# for item in prices :
#        total+=item
# print(f'total={total}')


                             #NESTED FOR

# for x in range( 2):
#     for y in range(2):
#         print(f'({x},{y})')

# numbers=[5,2,5,2,2]
# for let in numbers:
#     print("X"*let)


                         #LISTS

# names=['Omkar','Balram','Shambhu','Saurabh','Manish']
# print(names )     #['Omkar','Balram','Shambhu']
# print(names[2:])  #['Shambhu','Saurabh','Manish']
# print(names[2:4])  #['Shambhu', 'Saurabh']
# names[0]="Omkar Rawool"
# print(names )


#LARGEST FROM THE LIST#
# numbers=[12,54,23,1,6,455,5]
# large=numbers[0]
# for number in numbers:
#  if number>large:
#   large=number
# print(large)

                     # 2D LISTS

# matrix=[
#      [1,2,3],
#      [4,5,6],
#      [7,8,9],
# ]
# print(matrix[0][2])
#
# for row in matrix:
#  for column in row:
#   print(column)
                                       #LIST OPERATIONS
#
# numbers=[5,2,1,2,2,7,4]
# numbers.append(20)
# print(numbers)         #[5, 2, 1, 7, 4, 20]
#
# numbers.insert(0,33)
# print(numbers)         #[33, 5, 2, 1, 7,2,3,4, 4, 20]
#
# print(numbers.index(1))
# print(3 in numbers)
# print(numbers.count(2))
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)


# numbers=[12,23,2,3,23,5,5,33,67,7,67]
# uniques=[]
# for n in numbers:
#     if n not in uniques:
#         uniques.append(n)
# print(uniques)

                                                    #TOUPLE (Touples are immutable)
# numbers=(12,23,1,2)
# w,x,y,z=numbers
# print(w*y*z*x)

                                                #DICTIONARIES
# customer ={
#     "name":"Omkar Rawool",
#     "age":24,
#     "is_varified":True
# }
#
# customer["birthdate"]="1-Jan-2022"
#
# print(customer["birthdate"])
# print(customer)
#
# print(customer.get("age",45))            #Prevents from KeyNull error when the related key is not present
# customer["company"]="Crossasyst"
# print(customer)

# phone=input("Phone:")
# digits={
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four"
# }
# output=""
# for ch in phone:
#      output+=digits.get(ch,"*")+ " "
# print(output)
                                                         #Printing Emojis

# msg=input(">")
# output=""
# words= msg.split(' ')
#
# emojis = {
#     ":)":"😅",
#     ":(": "🙁"
# }
# for word in words:
#     output += emojis.get(word , word)+" "
# print(output)
                                                            #FUNCTIONS IN PYTHON


# def say_hello():
#     print("Hello Omkar....")
#     print("say_hello() called...")
#
# print("Start...")
# say_hello()
# print("Finish..")


                                                        #PARAMETERIZED FUNCTIONS


# def greet_user(name):
#     print(f'Hello{name}, Welcome to Python tutorial')
#
# print("Start...")
# greet_user("Omkar")
# print("Finish..")

# num1=int(input("Enter first number>"))
# num2=int(input("Enter second number>"))
#
# def sum(a,b):
#     return a+b
# print(f'Sum is {sum(num1,num2)}')


#                                                     #KEY PARAMETERS
#
# #Improves the readibility of the code
# def hello_users(firstName,lastName):
#     print(f'Hello {firstName} {lastName}')
#
# hello_users("Omkar","Rawool")                           #Position Argument
# hello_users(lastName="Mahato",firstName="Balram")       #Key Arguments
# # hello_users(firstName="Shambhu","Sahoo")              #NA
# hello_users("Mahato",firstName="Balram")                #NA

                                                    #Return Statements

# def square(number):
#     return number*number
# print(square(4))

                            #Creating reusable function
# def emoji_converter(message):
#
#
#     words= message.split(' ')
#
#     emojis = {
#         ":)":"😅",
#         ":(": "🙁"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word , word)+" "
#     return output
#
#
# message=input(">")
# print(emoji_converter(message))



                                #EXPECTIONS
try:
    age = int(input('Age:'))
    print("Age:"+age)
except ValueError:
    print("Invalid Value")
