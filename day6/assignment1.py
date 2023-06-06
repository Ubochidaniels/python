# percentage = 0
# question1 = input(""" what is the capital city of Abia state? 

# a. Owerri
# b. Aba 
# c. Awka
# d. Umuahia

# """)
# if question1 == "d":
#     percentage+=10
#     print(f"correct you now have {percentage}%")
# else:
#     print("incorrect")

# question2 = input("""How old is Obi?

# a. 12 
# b. 15
# c. 16

# d. 78 """)
# if question2 == "b":
#     print (" correct")
# else:
#     print ("not correct")
    

# score = 1
# question1 = int(input("""Even numbers are numbers ?

# 1) Numbers divisible by 2
# 2) Numbers not divisible by 2
# 3) Numbers divisible by 3
# 4) All of the above 
# """))

# if question1 == 1:
#     score *= 10
#     print(f" great answer and your score is {score}")
# else:
#     print(f"not correct and you have {-2} ")



# question2 = input(""" How many states does the US have ?

# A. 30
# B. 40
# C. 50
# D. 45
# """)
 
# if question2 == "C":
#     score +=10
#     print(f" correct and you now have {score}%")
# else:
#     print("incorrect")
# question3 = input( """ Which of these options is not a noun ?

# A. Chike 
# B. Dog 
# C. Table
# D. Sorry
# E. Sad
# F. President""")
# percentage *=3
# if question3 == "F":
#     print(f" correct{percentage}%")
# else:
#     print("incorrect")

# A python Program that loops through even numbers

# num1 = [1,2,3,4,5,6,6,8,9,10]
# for  num in num1:
#     if num % 2 == 0:
#         print(num)


 #Python Program that will accept user input and then reverse it 
user = input("what is ur name ?")
reversed = user[::-1]
kprint(reversed)

# # A program that can create user registration
inputName =input ("Enter your name \n")
inputEmail = input("Enter your email \n")


# if "@" not in inputEmail and ".com" not in inputEmail:
#     print("invalid email")
#     exit()cc
while "@" not in inputEmail and ".com" not in inputEmail:
    print("invalid email")
    inputEmail = input("reenter email address")
   
inputAddress = input("home address")
inputpassword = input("Eneter Password \n")
while str() not in inputpassword and int(2) not in inputpassword:
    print ("reenter password")
inputpassword = input("correct password")

print (f"Your name is {inputName} your email address is {inputEmail} and your home address is {inputAddress}   correct password {inputpassword}") 










