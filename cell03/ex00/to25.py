#!/usr/bin/env python3
print("Enter a number less than 25")
user_inp = input()
user_int = int(user_inp)

if(user_int <= 25):
	while user_int <= 25:
		print(f"Inside the loop, my variable is {user_int}")
		user_int += 1
else:
	print("Error")

