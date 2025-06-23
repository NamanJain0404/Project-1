def greeting(name):
  print("Hello, " + name)

import mymodule
mymodule.greeting("Jonathan")  

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
import mymodule

a = mymodule.person1["age"]
print(a)

import mymodule as mx

a = mx.person1["age"]
print(a)

import platform

x = platform.system()
print(x)

x = dir(platform)
print(x)

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

from mymodule import person1

print (person1["age"])
#Dsa

#Array
#bubble sort
my_array = [39,9,10,4,30,18,17]  #small to big

n=len(my_array)
for i in range(n-1):
   for j in range(n-i-1):
      if my_array[j] > my_array[j+1]:
         my_array[j],my_array[j+1] = my_array[j+1],my_array[j]

print("sorted array:",my_array)

#selection sort
my_array=[39,9,10,4,30,18,17]

n=len(my_array)
for i in range(n-1):
   min_index=i
   for j in range(i+1,n):
      if my_array[j] < my_array[min_index]:
         min_index=j
   min_value=my_array.pop(min_index)
   my_array.insert(i,min_value)

print("sorted array:",my_array)

#Insertion sort
my_array=[39,9,10,4,30,18,17]

n=len(my_array)
for i in range(1,n):
   insert_index=i
   current_value=my_array.pop(i)
   for j in range(i-1,-1,-1):
      if my_array[j]>current_value:
         insert_index=j
   my_array.insert(insert_index,current_value)

print("sorted array:",my_array) 

#


for i in range(1,6):
   for j in range(1,6):
      print(i,end="")
   print()

a=4  #sum of two no.
b=5
sum=a+b
print(sum)

#print all prime no 
start=2
end=20
print("prime numbers between",start , "and" , end, "are:")
for i in range(start,end+1):
   if i>1:
     for j in range(2,i):
      if(i%j==0):
       break
     else:
       print(i)

#square of given num
num=int(input("enter number:"))
Square=num ** 2
print("square is:",Square)

#print table of given no
n=int(input("enter number to print table:"))
for i in range(1,11):
   print(i*n)

#print calendar
import calendar
yy=2025
mm=2
print(calendar.month(yy,mm))

import calendar
yy=2025
print(calendar.calendar(yy))

#factorial
num=7
fact=1
for i in range(1,num+1):
   fact=fact*i
   print("factorial is:{}".format(fact))

#pattern
rows=int(input("enter the numbers of rows: "))
for i in range(rows):
 for j in range(i+1):
   print("*",end=" ")
print()

#2
for i in range(1,6):
   for j in range(1,6):
      print(j,end="")
   print()

#3
for i in range(1,6):
   for j in range(1,6):
      print(i,end="")
   print()

#4
for i in range(1,6):
   for j in range(1,6):
      print("*",end="")
   print()

#5
for i in range(1,6):
   for j in range(1,6):
      print(j%2,end="")
   print()

#6
for i in range(1,6):
   for j in range(1,6):
      print(i%2,end="")
   print()

#7
for i in range(5,0,-1):
   for j in range(5):
      print(i,end="")
   print()

#8
for i in range(5,0,-1):
   for j in range(5):
      print(j,end="")
   print()

#9
for i in range(5,0,-1):
   for j in range(5,0,-1):
      print(j,end="")
   print()

#10
for i in range(5,0,-1):
   for j in range(5,0,-1):
      print("*",end="")
   print()

#11
for i in range(ord('a'),ord('e')+1):
   for j in range(ord('a'),ord('e')+1):
      print(chr(j),end="")
      print()

for i in range(ord('a'),ord('e')+1):
   for j in range(ord('a'),ord('e')+1):
      print(chr(i),end="")
      print()

for i in range(ord('e'),ord('a')-1,-1):
   for j in range(ord('e'),ord('a')-1,-1):
      print(chr(i),end="")
      print()

#12 simple pyra
rows = 5
for i in range(0, rows):
  for j in range(0, i + 1):
      print("*", end=' ')
  print()

#13 inverted
rows = 5
for i in range(rows+1,0,-1):
  for j in range(0, i - 1):
      print("*", end=' ')
  print()

#14 full
def full_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

full_pyramid(5)

#15 inverted full
def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

inverted_pyramid(5)

#16 half
def mirrored_half_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)

mirrored_half_pyramid(5)

#17 diamond
def diamond(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

diamond(5)

#alphabet_pyramid
def centered_alphabet_pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")  # Add leading spaces
        for j in range(i + 1):
            print(chr(65 + j), end=" ")
        print()

# Example: Centered alphabet pyramid with 5 rows
centered_alphabet_pyramid(5)

#swap
x=5
y=10
temp=x
x=y
y=temp
print('value of x after swapping :{}'.format(x))
print('value of y after swapping :{}'.format(y))

#oops
#student details --using list --creating student record
student_1 = ['naman',10] #name,grade
student_2 = ['jay',13]

student_1.append('A')
print(student_1)

print(f'{student_1[0]} is in class {student_1[1]}')
print(f'{student_2[0]} is in class {student_2[1]}')

#using oops --creating student record

#class - blueprint or template
# __init__ method - constructor, value initialize - fix
# self parameter - reference or connection build btw class and object - fix
class Student: # student class
   def __init__(self,name,grade,percentage,team): #1 method
       self.name = name # attribute 
       self.grade = grade # attribute
       self.percentage = percentage # attribute 
       self.team = team

   def student_details(self): #2 method
       print(f"{self.name} is in class {self.grade} with {self.percentage}%") 

team1='A'

#object - instance of class
student1 = Student('naman',10,96,team1)
#print(student1.name) we can print in this way also
#print(student1.__dict__) we can print in this way also
student1.student_details()  #2
print(student1.name,student1.grade)  #1

#modify object property
print(student1.team)
print(student1.percentage)
student1.percentage = 100 #modify
print(student1.percentage)

#delete object property
print(student1.__dict__)
del student1.percentage
print(student1.__dict__)

#delete object
del student1
print(student1)
