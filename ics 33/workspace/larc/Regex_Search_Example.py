# LARC ICS 33 Spring 2014
# Regular Expressions File Searcher
# This program, given a pattern, will print out the lines that contain the given pattern

import re

file_to_be_searched = "supersecretfile.txt"
pattern = "Password:\d{4}" # your answer goes here

compiled_pattern = re.compile(pattern)


for i, line in enumerate(open(file_to_be_searched)):
	for match in re.finditer(compiled_pattern, line):
		print("Found a password! Line Number: " + str(i + 1))


l = ['a', 'b', 'c', 'd']
for i, l in enumerate(l):
	print(i, l)