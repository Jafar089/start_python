
# qs no 1

with open("poems.txt","r") as f:
    P=f.read()
    # print(P)
if "twinkle" in P:
    print("Yes")
else:
    print("No")

# qs no 2

# def game(num):
#     return num
# scr=game(4)
# with open('poems.txt','r') as f:
#     w=f.read()
# if(str(scr)>str(w)):
#     with open('poems.txt','w') as f:
#         w=f.write(str(scr))

# qs no 3

# for j in range(2,21):
#     with open(f"f/table of {j}",'w') as f:
#         for i in range(1,11):
#             f.write(f"{j} x {i} = {j*i}\n")

# qs no 4

# with open('poems.poems.txt','r') as f:
#     a=f.read()

# a=a.replace('donkey', '######')

# with open('poems.poems.txt','w') as f:
#     f.write(a)

# qs no 5

# lists=['donkey','lion','zebra']

# with open('poems.poems.txt','r') as f:
#     a=f.read()

# for i in lists:
#     a=a.replace(i, '######')

# with open('poems.poems.txt','w') as f:
#     f.write(a)

# qs no 6

# with open('poems.poems.txt') as f:
#     a=f.read().lower()
# if 'python' in a:
#     print('yes python is present: ')
# else:
#     print('python is not present: ')

# qs no 7

# i=0
# a=True
# with open('poems.poems.txt') as f:
#     while a:
#         a=f.readline().lower() 
#         i=i+1 
#         if 'python' in a:   
#              print(a)
#              print('yes python is present at line number: ')
#              print(i)

# qs no 8

# with open('poems.poems.txt') as f:
#     a=f.read()
# with open('copy.txt','w') as f:
#     f.write(a)     

# qs no 9

# file1='poems.poems.txt'
# file2='copy.txt'

# with open(file1) as f:
#     a=f.read()
# with open(file2) as f:
#     w=f.read()
# if a==w:
#     print("Yes, both files are identical!")
# else:
#     print("No, both files are not identical!")

# qs no 10

# with open('copy.txt') as f:
#     a=f.read()
# with open('copy.txt','w') as f:
#     f.write('')

# qs no 11
# import os

# with open('rename.txt') as f:
#     a=f.read()

# with open('rename.txt','w') as f:
#     f.write(a)
# os.rename('rename.txt','hogi.txt' )