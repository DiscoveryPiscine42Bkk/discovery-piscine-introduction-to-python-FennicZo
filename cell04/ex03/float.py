#!/usr/bin/env python3

num = input("Give me a number: ")
fl_num = float(num)

if "." in num:
    print("This number is a decimal.")
else:
    print("This number is an integer.")
