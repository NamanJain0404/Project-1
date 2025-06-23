#day 4 
from ast import NameConstant
import numbers
from pickle import TRUE
from re import I


print("hello world",7)    
print(5)
print("bye")
print(17*13) 

#day 5 (back-slash)\n means escape sequence character,#means it will display comment form,ctrl+/ will be for comment or uncomment form, '''or""" will be multiline comment
print("hey i am \"good boy\"\nand this viewer is also good boy/girl") #print hi
print("hey",6,7, sep="~",end="009\n") #sep means separator,tilde(~)character has been appeared after"hey",end=009 means will be print before next print statement,\n bydefault
print("harry")

#day 6 variable and datatype
a=complex(1,2) #datatype
print(a)
#naman=4
a1=9 #in this variable should be same no.or name
b="naman" #datatype ""print will be naman,without this"" print will be 4
c=True
print(b)
print(c)
print(a+a1)
print("the type of a is",type(a))
print("the type of b is",type(b))
print("the type of c is",type(c))
print("the type of a1 is",type(a1))

list1=[8,2.3,[-4,5],["apple","banana"]] #list 
print(list1)

tuple1=(("parrot","sparrow"),("lion","tiger")) #tuple
print(tuple1)

dict1={"name":"naman","age":21,"canVote":True} #dictionary
print(dict1)

# In python everything will be object

#day 7 operators and day8 exercise 1 solution
print(5+6)
print(15-6)
print(15*6)
print(15/6)
print(15//6) # floor division operator//
print(5%3)
print(5**3) #means 5 ratio 3(5*5*5)
#create calculator exercise 1
a=50
b=3

print("the value of",a,"+",3,"is:",a+b) #alt shift down key
print("the value of",a,"-",3,"is:",a-b)
print("the value of",a,"*",3,"is:",a*b)
print("the value of",a,"/",3,"is:",a/b)
print("add",a+b)

#day 9 typecasting
a="1" # "1" is string 
#a=1 
b="2"
#b=2
print(int(a)+int(b)) #if we use int then string will be convert into integer form

#explicit typecasting doubt
string="15"
number=7
string_number=int(string)
sum= number + string #throws an error if the string is not valid integer
print("the sum of both the numbers:",sum)

#implicit typecasting
c=1.9
d=8

print(c+d)
#python automatically converts
#a to int
a=7
print(type(a))

#python automatically converts b to float
b=3.0
print(type(b))

#python automatically converts c to float as it is a float addition
c=a+b
print(c)
print(type(c))

#day 10 taking user input in python
a=input("enter your name:")
print("my name is",a)

x=input("enter first number: ")
y=input("enter second number: ")
print(x + y) #concatenation

print(int (x)+int (y)) #arithmetic operation

#day 11 string 
name="naman"
friend="dhruvil"
anotherfriend='lovish'
apple='''he said,       
hi Naman
hey i am good
"i want to eat an apple'''     #we have create string of apple if we use any sentences in string if error comes the we use '''   ''' quotation

name="naman"
print("hello, "+ name)
print(apple)
print(name[0]) #accessing character osf string
print(name[1])
print(name[2])
print(name[3])
print(name[4])
#print(name[5])#throws an error
print("lets use a for loop\n")
for character in apple:   #loop through the string we use for loop so all character will be in individual in new line
    print(character)

#day 12 string slicing and operations
names="naman,shikha" #print(names[0:5]) means 0 to n-1 and n value is pi
print(len(names))

fruit="mango" #length of string
len1=len(fruit)
print("mango is a",len1,"letter word.")

fruit="mango" #length of string
mangolen=len(fruit)
print(mangolen)
#print(fruit[0:4]) #including 0 but not 4
#print(fruit[1:4])
#print(fruit[:4])
#print(fruit[:])
#print(fruit[:5])
#print(fruit[0:-3])
#print(fruit[0:len(fruit)-3])
print(fruit[-1:len(fruit)-3])
print(fruit[-3:-1]) #2:4

pie="applepie" #slicing
print(pie[:5]) #slicing from start
print(pie[5:]) #slicing till end
print(pie[2:6]) #slicing in between
print(pie[-8:]) #slicing using negative index

#qiuck qiuz
name="naman"
print(name[-4:-2])

#day 13 string method
#strings are immutable
a="naman! !!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("naman","shikha"))
print(a.split(" "))
blogheading="introduction to js" #capitalize in this first letter will capital 
print(blogheading.capitalize())

str1="welcome to the console!!!"
print(len(str1)) #it will show len of string
print(len(str1.center(50))) #string will come center it will leave 50 space then it will print string
print(a.count("naman")) #it will count words in a

str1="welcome to the console!!!" #endswith()
print(str1.endswith("!!!"))

str1="welcome to the console!!!"
print(str1.endswith("to",4,10))

str1="he's name is dan.he is an honest man."
print(str1.find("ishh")) #it will return index of first occurance of "is" 
#print(str1.index("ishh")) #output is valueerror:substring not found

str1="welcomeToTheConsole" #isalnum
print(str1.isalnum()) #A-Z,a-z,0-9 return true otherwise false

str1="welcome" #isalpha
print(str1.isalpha()) #A-Z,a-z return true ,if 0-9 then false

str1="hello world" #islower
print(str1.islower()) #if all characters will lower return true otherwise false

str1="we wish you a merry christmas" #isprintable
print(str1.isprintable()) # string have printable character return true ,if \n use or any other then false

str1="   " #using Spacebar
print(str1.isspace())
str2="  " #using tab
print(str2.isspace())

str1="World Health Organization" #islittle
print(str1.istitle()) #return true if first letter will capitalize otherwise false

str1="python is a Interpreted language" #startswith
print(str1.startswith("python")) #start with given value return true otherwise false

str1="python is a Interpreted language" #swapcase
print(str1.startswith("python")) #uppercase convert to lower and lower convert to upper

str1="He's name is Dan.Dan ia an honest man." #title
print(str1.title()) #captialize each letter of word in string

#day 14 if else conditional statements
a=int(input("enter your age: "))
print("your age is:0",a)
# conditional operators
# >,<,>=,<=,==,!=
#print(a>18)
#print(a<=18)
#print(a==18)
#print(a!=18)
if(a>18):
    print("you can drive")
    print("yes")
else:
    print("you cannot drive")
    print("no")
print("yay!")

appleprice=210 #if-else
budget=200
if(appleprice<=budget):
    print("alexa,add 1 kg apples to the cart.")
else:
    print("alexa,do not add apples to the cart.")

appleprice=10
budget=200
if(budget - appleprice>50):
    print("alexa,add 1 kg apples to the cart.")
elif(budget - appleprice>70):
    print("its okay you can buy")
else:
    print("alexa,do not add apples to the cart.")

num=int(input("enter the value of num:")) #elif
if(num<0):
    print("numberis negative.")
elif(num==0):
    print("number is zero.")
elif(num==999):
    print("number is special.")
else:
    print("number is positive.")

print("i am happy now")

num=18 #nested
if(num<0):
    print("number is negative.")
elif(num>0):
    if(num<=10):
        print("number is between 1-10")
    elif(num>10 and num<=20):
        print("number is between 11-20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")

#day 15 exercise 2
    # pending

#day 16 match case statement
x=int(input("enter the value of x:"))
# x is the variable to match
match x:
    #if x is 0
    case 0:
        print("x is zero")
    #case with if-condition
    case 4:
        print("case is 4")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:    
        print(x,"is not 80")
    case _:
        print(x)

#day 17 for loops
name = 'naman'  #iterating over string
for i in name:   #for string
    print(i)     #
    if(i=="a"):
        print("this is something special!")

colors = ["red","green","blue","yellow"]     #iterating over list
for color in colors:
  print(color)
  for i in color:
      print(i)

for k in range(5):   #range
    print(k+1)

for k in range(1, 20001):   #range
    print(k)
#quick quiz
for k in range(1, 12, 3):   #range
    print(k)

#day 18 while loop
for i in range(3):
    print(i)

i=0            # while loop execute while the condition is true
while(i<=3):
    print(i)
    i=i+1

print("done with loop")

i=int(input("enter the number:"))
while(i<=38):
    i=int(input("enter the number:"))
    print(i)

print("done with loop")

count=5
while(count>0):
    print(count)
    count=count-1
else:                             #else with while loop
    print("i am inside else")

#day 19 break and continue
for i in range(12):       #break  it will skip the loop
    if(i==10):
        break
    print("5 X",i+1,"=",5*(i+1))

print("left the loop and go")

for i in range(12):      #continue     it will skip the iteration
    if(i==10):
        print("skip the iteration")
        continue
    print("5 X",i+1,"=",5*(i+1))

for i in range(12):      #continue
    if(i==10):
        print("skip the iteration")
        continue
    print("5 X",i,"=",5*i)

i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
      break

#day 20 functions   doubt
def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
       print("first number is greater")
    else:
       print("second number is greater or equal")

def isLesser(a,b):
  pass

a=9
b=8
isGreater(a,b)
calculateGmean(a,b)
#gmean1=(a*b)/(a+b)
#print(gmean1)
c=8
d=74
isGreater(c,d)
calculateGmean(c,d)
#gmean2=(c*d)/(c+d)
#print(gmean2)

#day 21 function arguments
def average(a,b):     #create a function and it is required arguments
    print("the average is", (a+b)/2)

average(4,6)

def average(a=9,b=1):     #it is default arguments
    print("the average is", (a+b)/2)
average()
#average(4,6)

def name(fname,mname="jhon",lname="whatson"):  #default 
    print("hello,",fname,mname,lname)

name("amy")

def average(a=9,b=1):     #keyword argument
    print("the average is", (a+b)/2)

average(b=9)

average(b=9,a=21)

def average(a,b,c=1):      #required argument in this all the value will be require otherwise error
    print("the average is",(a+b+c)/2)

average(5,6)

def name(fname,mname,lname):  #require
    print("hello,",fname,mname,lname)

name("peter","quill")

def average(*numbers):         #keyword arbitrary arguments 
    #print(type(numbers))
    sum=0
    for i in numbers:
      sum=sum+i
    print("average is: ", sum / len(numbers))

average(5,6,7,1)

def name(**name):
    #print(type(name))
    print("hello,",name["fname"],name["mname"],name["lname"])

name(mname="buchanan",lname="barnes",fname="james")

def average(*numbers):         #return statements
    #print(type(numbers))
    sum=0
    for i in numbers:
      sum=sum+i
    #print("average is: ", sum / len(numbers))
    return sum / len(numbers)

c=average(5,6,7,1)
print(c)

def name(fname,mname,lname):      #return
    return "hello,"+fname+mname+" "+lname

print(name("james","buchanan","barnes"))

#day 22 introduction to lists
marks=[3,5,6,"harry",True, 6,7,2,32,345]         #list and in this we can write boolean also
#print(marks)
#print(type(marks))
#print(marks[0])
#print(marks[1])
#print(marks[2])

#print(marks[-3])  #negative index
#print(marks[len(marks)-3])  #positive index
#print(marks[5-3])  #positive index
#print(marks[2])  #positive index

if 6 in marks:
    print("yes")
else:
    print("no")
#same thing apply on string as well!
if "ha" in "harry":
    print("yes")


list1=[1,2,2,3,5,4,6]    #list
list2=["red","green","blue"]
print(list1)
print(list2)

colors=["red","green","blue","yellow","green"]   #negative indexing
print(colors[-1])
print(colors[-3])
print(colors[-5])

marks=[3,5,6,"harry",True, 6,7,2,32,345]  #print elements within particular ranges
print(marks)
print(marks[1:9])
print(marks[1:9:3])

animals = ["cat","dog","bat","mouse","pig","horse","donkey","goat","cow"]
print(animals[::2])      #using positive indexes
print(animals[-8:-1:2])  #using negative indexes
print(animals[1:8:3])

lst = [i*i for i in range(10)]      #list comprehension
print(lst)
lst = [i*i for i in range(10) if i%2==0]    # it will print even numbers
print(lst)

names = ["milo","sarah","bruno","anastasia","rosa"]     #accept items which have more than 4 letters
nameswith_0 = [item for item in names if (len(item)>4)]
print(nameswith_0)

#day 23
