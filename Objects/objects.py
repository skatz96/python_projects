# class Dog:
# 	def __init__(self, name, breed, age, color, weight, DOB, tricks):
# 		self.name = name
# 		self.breed = breed
# 		self.age = age
# 		self.color = color
# 		self.weight = weight
# 		self.DOB = DOB
# 		self.tricks = tricks



# 	def getName(self):
# 		return self.name

# 	def bark(self):
# 		return "woof"

# 	def addTrick(self, trick):
# 		self.tricks.append(trick)


# d1 = Dog("Barney", "Black Lab", 12, "black", 100, "September 21", [])
# d2 = Dog("Oliver", "Cream Retriever", 7, "White", 100, "Feb 21", [])
# d3 = Dog("Sandy", "Black Lab", 12, "black", 100, "Oct 22", [])


# # d1.addTrick("Roll over")
# # d1.addTrick("Paw")
# # print(d1.tricks)


# arr = []
# arr.append(d1)
# arr.append(d2)
# arr.append(d3)

# for x in range(0,len(arr)):
# 	print(arr[x].name)






class Student:
	def __init__(self, name, school, year, major, ID):
		self.name = name 
		self.school = school
		self.year = year
		self.major = major
		self.ID = ID

	def findSchool(self):
		return self.school

	def getName(self):
		return self.name

	def findID(self):
		return self.ID

s1 = Student("Sadie", "University of Maryland", "senior", "communication", "113556180")

class Instructor:
	def __init__(self, name, department, degree, classes, university):
		self.name = name
		self.department = department
		self.degree = degree
		self.classes = classes
		self.university = university 

	def findDepartment(self):
		return self.department 

	def getDegree(self):
		return self.degree 

	def findUniversity(self):
		return self.university

	def findClasses(self):
		return self.classes

I1 = Instructor("Ms. Katz", "communication", "PhD", ["listening","persuasion"],"UMD")

print(I1.findClasses())

print(s1.getName(), "goes to", s1.findSchool())









































