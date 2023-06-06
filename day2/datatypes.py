'''DATA TYPES IN PYTHON
INTEGERS
integers are whole numbers, -ve and +ve numbers that are not inside a quotation mark (""). Examples of integers are as follows
'''
#types of comments are double and single. Example of double comments is ''' or """"  while single comment is simply #
f=60

print(type(f))
#FLOAT
# Float are Real numbers, they are basically numbers with decimal point eg 13.8 and they are not in quotation mark ""
# Examples of floats are as follows
q=30.9
print(type(q))
o=40.9
print(type(o))
#LIST
#List are group of items in a square bracket []
#Examples are:
t=["chike", "okoro", 36, 40.4]
print(type(t))
#STRINGS
#Strings are items in a quotation mark eg "b"
#Examples are as follows
e="b"
print(type(e))
g="34.8"
print(type(g))
#SET
#Set are group of items in in double circular bracket and they are unordered 
#Exaples of set are as follows
jk=(("chike","30", 40.9, 30))
print(type(jk))
#DICT
#Dict is used to define a group of items as it relates to what the entail, unordered key value pairs 
yu={"name": "chike", "age": 36, "school": "ashpot", "skills": "python,java", "location": "Aba" }


print(type(yu))
print(yu.keys())
print(yu.values())
print(yu["name"])
#TUPLE 
#Tuple is ordered and immutable and they are in circular brackets ()
w=("10", "chike", 12, 30.9)
print(type(w))
#BOOL
#Bool is used for logical explanations like true or false
b=(True)
print(b)