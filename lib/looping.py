#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i>0:
        print(i)
        i+= -1
    if i == 0:
        print("Happy New Year!")    
    pass
  

def square_integers(int_list):
    # code goes here!
    return [num**2 for num in int_list]
    pass

def fizzbuzz():
    # code goes here!
    num = 1
    for num in range(1,101):
        if num%3 == 0 and num%5 == 0:
            print('FizzBuzz')
        elif num%3 == 0:
            print("Fizz")    
        elif num%5 == 0:
            print("Buzz")
        else:
             print(num)    
        pass


# for height in player_heights:
#     inch_height = height * 7920
#     inc_heights.append(inch_height)
