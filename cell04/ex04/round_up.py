#!/usr/bin/env python3

us_in = input("Give me a number: ")
number = float(us_in)

if number == int(number):
    rounded_up = int(number)
else:
    rounded_up = int(number) + 1

print(rounded_up)
