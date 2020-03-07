#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created - Jan 2018

@author: adhamlin
"""


def fizz_buzz():
    """
    FizzBuzz: Clasic computer science interview problem.
    Create a script that completes the following tasks:
        a.) Prints numbers from 1 to 100, one number per row
        b.) If a number is divisible by 3, print "Fizz"
        c.) If a number is divisible by 5, print "Buzz"
        d.) If a number is divisible by both 3 and 5, print "FizzBuzz!"
    """
    start_num = int(input("Enter a starting whole number: "))
    stop_num = int(input("Enter a stoping whole number: "))

    for i in list(range(start_num, stop_num + 1)):
        if i % 2 == 0:
            print(f"{i} is even.")
        else:
            print(f"{i} is odd. FIZZ!")
        if i % 5 == 0:
            print(f"{i} is divisible by 5. BUZZ!")
        if i % 5 == 0 and i % 3 == 0:
            print(f"{i} is divisible by 3 and 5. Bart!S")
        if i % 3 == 0 and i % 5 == 0 and i % 15 == 0:
            print(f"{i} is divisible by 3, 5 and 15. FIZZBUZZ - WOW!")


fizz_buzz()
