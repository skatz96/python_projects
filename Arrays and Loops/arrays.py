
# # arr = [1,2,3,4]

# # print(arr[3])

# arr1 = ["Sadie","loves","to","eat", "apples","coding"]

# # print(arr1[0])

# # print(len(arr1))

# # for num in range(0,len(arr1)):
# # 	print(arr1[num])


# # x = len(arr1) - 1

# # while(x >= 0):
# # 	print(arr1[x]) 
# # 	x = x - 1

# for x in range(len(arr1)-1, -1, -1):
# 	print(arr1[x])




# arr2 = ["Sadie", "cannot", "wait", "for", "weekend"]

#   # for x in range(0,len(arr2)):
#  	# print(arr2[x])

#   # for x in range (len(arr2)-1,-1,-1):
#   # 	print(arr2[x])

#   # for x in range (0,len(arr2),+):
#  	# print(arr2[x])



# def isEven(arr2):
# 	if (len(arr2) % 2 == 0):
# 		return True
# 	else:
# 		return False

# print(isEven(arr2))


# arr3 = [1,2,3,4,5,6,7]

# def findProduct(arr3):
# 	product = 0
# 	for x in range(0,len(arr3)):
# 		product = product + arr3[x]
# 	return product



# # for x in range(1,len(arr3),2):
# # 	print(arr3[x])

# for x in range(0,len(arr3)):
# 	if(arr3[x] % 2 != 0):
# 		print(arr3[x]) 


# arr4 = []
# print(len(arr4))

# for x in range(1,11):
# 	arr4.append(x)
# # print(len(arr4))

# arr5 = [1,5,9,2,3]

# runningMax = -1
# for x in range(0,len(arr5)):
# 	if (arr5[x] > runningMax):
# 		runningMax = arr5[x]

# print(runningMax)







# print(findProduct(arr3))


# arr6 = [7,2,8,3,5]

# runningMin = 1000
# for x in range(0,len(arr6)):
# 	if (arr6[x] < runningMin):
# 		runningMin = arr6[x]

# print(runningMin)



# def


# def printDuplicates(num,arr8):
# 	runningCount = 0
# 	for x in range(0,len(arr8)): 
# 		if (arr8[x] == num):
# 			runningCount = runningCount + 1
# 	print(runningCount)

# arr8 = [7,2,8,3,3,5,3]

# printDuplicates(3,arr8)



# def dogBreed(breed):
# 	if (breed == "lab"):
# 		return True
# 	elif (breed == "yorkie"):
# 		return True
# 	elif (breed == "husky"):
# 		return True
# 	else:
# 		return False


# print(dogBreed("lab"))




# answer = raw_input()
# while (answer == "yes"):
# 	print("hi")
# 	answer = raw_input()


# def sumArray(arr9):
# 	num = 0
# 	for x in range(0,len(arr9)):
# 		num = num + arr9[x]
# 	return num

# # arr9 = [1,2,3,4,5]

#   print(sumArray(arr9))




#   def copyArray(arr10):
# 	elt = arr[0]
# 	for x in range(1,len(arr10)):
# 		arr[x] = elt
# 	return arr10

# arr = [1,0,0,0]



# def copyReverse(arr11):
# 	elt = arr11[len(arr11)-1]
# 	for x in range(0, len(arr11)):
# 		arr11[x] = elt
# 	return arr11

# arr11 = [0,0,0,1, 2, 3]

# def printArray(arr):
# 	for x in range(0,len(arr)):
# 		print(arr[x])

# printArray(copyReverse(arr11))	




# arr = [1,2,3]

# runningProduct = 1
# for x in range(0,len(arr)):
# 	runningProduct = arr[x] * runningProduct

# # print(runningProduct)

# arr = [1,2,3]

# for x in range(0,len(arr)):
# 	arr[x] = arr[x]**2

# print(arr)



# arr = [1,2,3]

# runningDiff = 0
# for x in range(len(arr)-1,-1,-1):
# 	runningDiff = runningDiff - arr[x]
# print(runningDiff)








