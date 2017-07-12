# Name:Richard Young
# Date:7-11-17

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
number =int(raw_input("how many Fibonaci numbers would you like?: "))
loop_control = 0
Fibo = 1
naci = 1
while loop_control <number:
    loop_control = loop_control + 1
    print naci
    Z = naci + Fibo
    Fibo = naci
    naci = Z
loop_control = False
