def isEven(num):
	if (num % 2 == 0):
		return True
	else:
		return False

# print(isEven(7))






def isAMultipleOfFive(num):
	if (num % 5 == 0):
		return True 


def isAMultipleOfThree(num):
	if (num % 3 == 0):
		return True


def isAMultipleOfThreeAndFive(num):
	if (num % 5 == 0 and num % 3 == 0):
		return True








for num in range(1, 101):
	if (isAMultipleOfThreeAndFive(num)):
		print("FizzBuzz")
	elif (isAMultipleOfThree(num)):
		print("Fizz")
	elif (isAMultipleOfFive(num)):
		print("Buzz")
	else:
		print(num)



