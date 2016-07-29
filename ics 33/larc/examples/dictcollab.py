# 1) Write a function called count_occurence that takes in a list of strings
# and returns a dictionary where every key is a string the given list and the value is 
# how many times the string is in the list 
# Example: 

my_list = ['a', 'b', 'c', 'a', 'd', 'c', 'a', 'e', 'z', 'a', 'a']
my_result = count_occurence(my_list)
print(my_result) --> {'c': 2, 'b': 1, 'a': 5, 'e': 1, 'd': 1, 'z': 1}


# Regular way
def count_occurence(alist: list) -> dict:
    answer = {}
    for each_element in alist:
        if each_element not in answer.keys():
            answer[each_element] = 0
        answer[each_element] += 1   
    return answer
    
# Defaultdict
from collections import defaultdict

def count_occurence(alist):
    answer = defaultdict(int)
    for each_element in alist:
        answer[each_element] += 1
    return dict(answer) # convert it back to a regular dict when you return 
    
    print(answer) --->  {'c': 2, ...}
        
        
 
# We want a dictionary that represents how many times
# we have been to a city

cities_traveled_to = ['Los Angeles', 'Austin', 'New York', 'Los Angeles', 'Irvine', 'Atlanta', 'Irvine', 'Irvine']
        
----> {'Los Angeles':  "X", "Austin": "XXXXX", Houston: "XXXXX"}   
        

def count_occurence(alist: list) -> dict:
    answer = defaultdict(str)
    for each_element in alist:
        answer[each_element] += 'X'
    return dict(answer)
            
            
 # 2) What is the different between sort and sorted?
            
   sort mutates a list and sorted provided a sort of "mirror"
   
- sort: is a method that can be only be used by lists.
- s = "sjdifdksjfdsjk"
- s.sort() ---> you can't call sort on a string because it will raise an exception
- sort will mutate your list


- sorted: is an iterator (a function) and it doesn't mutate

alist = [1, 3, 5, 2, 99, 2]
sorted(alist)
print(alist) ---> [1, 3, 5, 2, 99, 2]


for num in sorted(alist):
    print(num)
    
1
2
2
3
5
99

sorted(dict) --> sorted is good for sorting a dictionary inside a for loop

for thing in alist.sort() <--- won't work because sort method returns none


# EBNF (Not python)
# Language used to describe the structure and syntax of things.
# The tools (words of EBNF)
    - | choice
    - [] option
    - {} repetition
    -    sequence
    
#Describe a phone number using EBNF
#<= less than sign engulfs equals sign

#(949) 555-5555
#digit <= 0|1|2|3|4|5|6|7|8|9
#phone_number <= (digit digit digit) digit digit digit - digit digit digit digit

#(949)555-5555 or (949)555.5555
#digit <= 0|1|2|3|4|5|6|7|8|9
#phone_number <= (digit digit digit) digit digit digit (-|+) digit digit digit digit

---------
# Which of the following pairs of code are not equivalent? An easy way to do solve
# this problem would be simply to copy and paste both bits of codes into Python and run
# however, try to see if you can get the right answer by simply looking at the code
'''
##a) NOT THE SAME
##return 150 if Home.price_appraisal() < 500 else return 250
##
##if Home.price_appraisal() < 500:
##    return 250
##else:
##    return 150
##
##b)
##grades = []
##for student in classroom:
##    grade = GradeBook.get_grade(student)
##    grades.append(grade)
##
##grades = [GradeBook.get_grade(student) for student in classroom]
##
##c)
##passing_students = []
##for student in classroom:
##    grade = GradeBook.get_grade(student)
##    if grade > 70:
##        passing_students.append(student)
##
##passing_students = [student for student in classroom if GradeBook.get_grade(student) > 70]
##
##d) 
##is_adult = True if age > 18 else False
##
##if age > 18:
##    return True
##else:
##    return False
##---------------
##ANSWERS:

