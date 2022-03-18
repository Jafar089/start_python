# from playsound import playsound
# import time
# time.sleep(3)
# playsound('C:\\Users\\hp\\Music\\majalis and nohay\\Ali.mp3')


# a=int("123")
# print(a+3)

# a=23
# b=21
# c=a+b
# print("The sum of a and b is: ",c)

# a=34
# b=21
# c=(a<b)
# print(c)

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=(a+b)/2
# print(c)

# a=10
# square=a*a
# print(square)

# string slicing

# name="Jafar"
# print(name[0:4])

# skipping letters in name by using this semicolounms
# name="Jafarisgood"
# d=name[0::3]
# print(d)

# printing length of string and some functions..!

# story='''give thanks to allah for the moon 
# and the stars praise him all day for what is and what was'''
# print(len(story))
# print(story)
# print(story.endswith("was"))
# print(story.count("for"))
# print(story.capitalize())
# print(story.find("for"))
# print(story.replace("moon", "sun"))

# paractice set of string
# letter writting

# name=input("Enter name")
# date=input("Enter date")
# letter='''Dear <name>\nYou are selected!\n<date>'''
# letter=letter.replace("<name>", name)
# letter=letter.replace("<date>", date)
# print(letter)

# paractice of lists in python

# a=[1,5,43,2,11,3,6,22]
# a.sort()
# a.pop(3)
# print(a)
# a.reverse()
# a.append(100)
# a.insert(5,2)
# a.remove(43)
# print(a)

# paractice of tuple in python

# t=(1,2,34,3,2,33,2)
# print(t.count(2)) # Give the count of given element in tuple
# print(t.index(33)) # Give the index of given element in tuple


# some dictionaries method in python

# Mydict={
#     "fast": "in a quick manner",
#     "jafar": "coder",
#     "pressure cooker":"To boil something",
#     "marks": [1, 2, 3],
#     1: 2,
#     "anotherDict":{'jafar':'player'}
# }
# print(Mydict['fast'])
# print(Mydict['anotherDict']['jafar'])
# print(list(Mydict.keys()))
# print(list(Mydict.values()))
# print(list(Mydict.items()))
# print(Mydict)
# updateDict={
#     "lovish":"to lovely person"
# }
# Mydict.update(updateDict)
# print(Mydict)

# sets paractice and different methods

# a=set()
# print(type(a))
# print(a)
# a.add(2)
# a.add(4)
# a.add(5)
# a.add(4)
# a.add((1,2,3)) # you also add tuple in sets
# print(len(a)) # print length of the elements of set
# a.remove(4) # remove element which you can give
# print(a)
# print(a.pop()) # remove any element in the set and then print it 
# print(a)
# print(a.clear()) # empty the set
# print(a)

#  if elif and else statements in python

# a=4
# if(a>3):
#     print("value of a is gretaer than 3")
# elif(a<3):
#     print("value of a is less than 3")
# else:
#     print("value of a is equal to 3")

# a=10
# b=[1,2,3,43]
# # check element in array if hay then true else no
# print(2 in b) 
# # check agar hay to if wali condition true kr do
# if(a is 10):
#     print("Oh, Baby your value is 10: ")



# Text=input("Enter user_name: ")
# if(len(Text)>10):
#     print("This username is greater than ten characters..!")
# else:
#     print("This username is less than ten characters..!")


# marks=int(input("Enter your marks to check grade:\n"))
# if(marks<50):
#     print("Your grade is F")
# elif(marks>=50 and marks<=60):
#     print("Your grade is D")
# elif(marks>60 and marks<=70):
#     print("Your grade is C")
# elif(marks>70 and marks<=80):
#     print("Your grade is B")
# elif(marks>80 and marks<=90):
#     print("Your garde is A")
# elif(marks>90 and marks<=100):
#     print("Your garde is Ex")

# string='harry is a good programmer. his code is very brilliant. I really appriciate for that'
# print(string)
# if('harry' in string):
#     print("\nYes, you talk about Harry..!")
# else:
#     print("\nYou dont talk about Harry..!")

# loops in python

# fruits=['banana','mango','grapes']
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i=i+1

# fruits=['banana','mango','grapes']


# for item in fruits:
#     print(item)


# num=int(input("Enter a number: "))
# for i in range(10, 0, -1):
#     print(f"{num} x {i} = {num*i}")

# for i in range(5):
#     for j in range(i+1):
#         print("* ",end="")
#     print("\n")

# def greet(name):
#     print("Good day, With " + name)
# greet(input("Enter your name: "))

# def factorial(n):
#     product=1
#     for i in range(1,n+1):
#         product=product*i
#     return product
# f=factorial(int(input("Enter number to find factorial: ")))
# print("Your factorial is",f)

# for i in range(5):
#     for j in range(i+1):
#         print("* ",end="")
#     print("\n")
# c=int(input("enter another number to find factorial: "))
# g=factorial(c)
# print("Your another factorial is: ",g)

# x=5
# print(x**2) # for power we use 2 times * this sign.

# def factorial_recursive(n):
#     if n==1 or n==0:
#         return 1
#     return n*factorial_recursive(n-1)

# f=factorial_recursive(5)
# print(f)


# from playsound import playsound
# import time
# playsound('C:\\Users\\hp\\Music\\majalis and nohay\\Ali.mp3')

from gtts import gTTS
from playsound import  playsound
mytext="piyari maa mujh ko teri dua chaeyay tery aanchal ki thandhi hawa chaeyay."
language='en'
voice=gTTS(text=mytext,lang=language,slow=False)
voice.save("counting.mp3")
playsound("counting.mp3")

# arr = [25, 11, 7, 7, 56]
# max = arr[0]      
# for i in range(0, len(arr)):     
#    if(arr[i] > max):    
#        max = arr[i]          
# print("Largest element present in given array: " + str(max))