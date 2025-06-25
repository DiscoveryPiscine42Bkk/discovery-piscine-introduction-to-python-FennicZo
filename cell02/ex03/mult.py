#!/usr/bin/env python3
print("Enter the first number: ")
f_num = input()
f_int = int(f_num)
print("Enter the second number: ")
l_num = input()
l_int = int(l_num)

result = f_int * l_int
print(f"{f_int} x {l_int} = {result}")

if(result == 0):
	print("The result is both positive and negative.")
elif(result < 0):
	print("The result is negative.")
else:
	print("The result is positive.")
