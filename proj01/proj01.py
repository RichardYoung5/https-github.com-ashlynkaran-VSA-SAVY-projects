# Name: Richard Young
# Date: 7-10-17

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!


Name = raw_input("Enter Your Name: ")
Age = raw_input("Enter Your Age : ")
Y =raw_input("What Year is it?: ")
B =raw_input("Have you already had a Birthday this year?: ")
W = int(Y) - int(Age)
L = W + 100
if B == "Yes":
    L+1
elif B == "yes":
    L+1
else:
    L-1

if Age > 99:
    W+100
else:
    W+0

if Age < 99:
    print(Name),'you turned 100 during the year',(L)
else:
    print(Name),'you are going to turn 100 during the year',(L)