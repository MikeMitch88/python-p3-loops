#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i <= 10:
        print(i)
        if i == 1:
            print("Happy New Year!")
            break
        i -= 1
        
def square_integers(int_list):
    # code goes here!
    squaredIntegers = list()

    for item in int_list:
        squaredItem = pow(item, 2)
        squaredIntegers.append(squaredItem)

    return squaredIntegers
    

    
    

def fizzbuzz():
    # code goes here!
     for item in range(1, 101):
        # !with if...elif...else
        if item % 3 == 0 and item % 5 == 0:
            print("FizzBuzz")
        elif item % 3 == 0:
            print("Fizz")
        elif item % 5 == 0:
            print("Buzz")
        else:
            print(item)
        
        # !with match...case/python 3.10
        # match item:
        #     case item % 3 == 0 and item % 5 == 0:
        #          print("FizzBuzz")
        #     case number % 3 == 0:
        #         print("Fizz")
        #     case number % 5 == 0:
        #         print("Buzz")
        #     case _:
        #         # _ wildcard/no matching case
        #         print(number)


fizzbuzz()
    
    