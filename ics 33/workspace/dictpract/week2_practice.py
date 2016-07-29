# Practice Problems (Solutions are the bottom)

# 1) Write a function called count_occurence that takes in a list of strings
# and returns a dictionary where every key is a string the given list and the value is 
# how many times the string is in the list 
# Example: 
# my_list = ['a', 'b', 'c', 'a', 'd', 'c', 'a', 'e', 'z', 'a', 'a']
# my_result = count_occurence(my_list)
# print(my_result) --> {'c': 2, 'b': 1, 'a': 5, 'e': 1, 'd': 1, 'z': 1}

def count_occurence(alist: list) -> dict:
	pass

# 2) What is the different between sort and sorted?
# Your answer:

# 3) Write the fundamental theorem of object-oriented programming
# Your answer:

# 4) Write a function called flip_dict that takes as input a dictionary
# and returns the new dictionary where the keys and values of the inputted dictionary are flipped.
# Example:
# flip_dict({'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four', 'e': 'five', 'f': 'six'}) returns -->
# 	{'one': 'a', 'three': 'c', 'five': 'e', 'six': 'f', 'two': 'b', 'four': 'd'}

def flip_dict(a_dict: dict) -> dict:
	pass

# 5) Which of the following pairs of code are not equivalent? An easy way to do solve
# this problem would be simply to copy and paste both bits of codes into Python and run
# however, try to see if you can get the right answer by simply looking at the code
'''
a) 
return 150 if Home.price_appraisal() < 500 else return 250

if Home.price_appraisal() < 500:
	return 250
else:
	150

b)
grades = []
for student in classroom:
	grade = GradeBook.get_grade(student)
	grades.append(grade)

grades = [GradeBook.get_grade(student) for student in classroom]

c)
passing_students = []
for student in classroom:
	grade = GradeBook.get_grade(student)
	if grade > 70:
		passing_students.append(student)

passing_students = [student for student in classroom if GradeBook.get_grade(student) > 70]

d) 
is_adult = True if age > 18 else False

if age > 18:
	return True
else:
	return False
---------------


'''










# Solutions:

# 1)
def count_occurence(alist: list) -> dict:
	answer = {}
	for string in alist:
		if string not in answer.keys():
			# if the string is not already in my dictionary, I'm going to go ahead
			# and throw it in my dictionary and initialize it's count to 0
			answer[string] = 0
		answer[string] += 1
	return answer

# Solution using defaultdict
# Notice how by using defaultdict, we save ourselves from having
# to check if something is in the dictionary already?
from collections import defaultdict
def count_occurence(alist: list) -> dict:
	answer = defaultdict(int) # because all of my values will be ints, I will make it defaultdict of ints
	for string in alist:
		answer[string] += 1
	answer = dict(answer) # don't forget to convert your defaultdict back into a regular dict before returning!!!
	return answer

# 2)
# What is the difference between sort and sorted?

# A couple of things are different here: sort is a list method. That means that
# only list objects can use sort. For example, you cannot call sort on a string
# s = "hi I'm a string!"
# s.sort() ---> will raise an exception!
# sorted is called an iterator. You will learn more about this in week 4 but for now, 
# you can think of sorted as a function. You can call sorted on anything that you can
# loop over in a for loop (e.g. lists, tuples, sets, dict)

# Second, sort mutates a list. That means that it changes whatever list calls sort.
# Example:
# a_list = [3, 4, 1, 5]
# a_list.sort()
# print(a_list) ----> [1, 3, 4, 5]
# a_list has changed its order

# In contrast, sorted will not mutate whatever it is called on. You use sorted when you are trying to
# temporarily sort any container in a for loop.
# For example, we know that dictionaries don't have a sort method. Say we would like to
# print out a dictionary in alphabetical order. We would have to use sorted to do this:
# for key in sorted(dict):
#	print(key)
# in here, dict will not change its order (dictionaries aren't in any specific order in the first place)

# 3)
# The Fundamental Theorem of Object-Oriented Programming (TFTOOP)
# o.m(...) = type(o).m(o, ...)

# 4) 
def flip_dict(a_dict: dict) -> dict:
	answer = {}
	for key, value in a_dict.items():
		answer[value] = key
	return answer

#  solution using comprehension
def flip_dict(a_dict: dict) -> dict:
	return {value: key for key, value in a_dict.items()}

# 5) The two bits of code in letter a do different things.





