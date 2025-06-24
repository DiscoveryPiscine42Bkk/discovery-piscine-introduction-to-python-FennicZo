user_inp = input()
user_int = int(user_inp)

if(user_int == 0):
	print("This number is both positive and negative.")
elif(user_int < 0):
	print("This number is negative.")
else:
	print("This number is positive.")
