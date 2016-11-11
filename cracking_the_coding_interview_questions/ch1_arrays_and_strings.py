# 1.1: Determine if a string has all unique characters


def check_unique_chars(s):

	charmap = {}

	for char in s:
		charmap[char] = charmap.get(char, 0) + 1
		if charmap.get(char, 0) > 1:
			return False
	return True

	# Thoughts on algorithmic time complexity:
	# Each iteration of the loop contains operations that take O(1)
	# If there are n characters in the string s, then this algorithm is O(n)


# 1.2: Check if one string is the permutation of another


def check_strings_permuted(s1, s2):
	charmap1 = {}
	charmap2 = {}

	for char in s1:
		charmap1[char] = charmap1.get(char, 0) + 1

	for char in s2:
		charmap2[char] = charmap2.get(char, 0) + 1

	return charmap2 == charmap1

	# Thoughts on algorithmic time complexity:
	# Each iteration of the first loop contains operations that take O(1)
	# Each iteration of the second loop contains operations that take O(1)
	# If there are n characters in the string s1, and m characters in the string s2, then the overall function is O(m+n)


# 1.3: Replace the white spaces in a string with '%20'


def replace_white_space(s):
	''.join(char if char != ' ' else '%20' for char in s)

	# Thoughts on algorithmic time complexity:
	# Iterates through length of string, doing O(1) work in each iteration
	# If there are n characters in the string, then the function's time complexity is O(n)


# 1.4: Determine if a string is a permutation of a palindrome

def check_palindrome_permuted(s):
	# to be a palindrome permutation, s must have an even number of every char, with the exception of at most one char with an odd number

	charmap = {}

	for char in s:
		if char != ' ':
			charmap[char] = charmap.get(char, 0) + 1

	odd = 0
	print charmap
	for count in charmap.values():

		if count%2 != 0:
			odd += 1

		if odd > 1:
			return False

	return True

	# Thoughts on algorithmic time complexity:
	# first for loop iterates through characters in s, doing O(1) work for each iteration
	# second loop iterates through the char counts and does O(1) work for each iteration
	# If there are n characters in s and m unique characters in s, then the time complexity is O(n+m)


# 1.5: Check if one string is 1 or 0 edits away from being another string

def check_edit_strings(s1, s2):
	# allowed edit operations are inserting a character, removing a character, or replacing a character
	# use insert if char to left is correct but current char should be to the right
	# use delete if char to left is correct but char to right should be current char
	# use replace if char to left is correct and char to right is correct, but current char is not

	i = 0
	j = 0

	# all the logic is meant for editing s2 to match s1
	edit = False
	while i < len(s1) and j < len(s2):
		# insert case
		if s1[i] != s2[j] and s1[i+1] == s2[j]:
			i += 1
			if edit:
				return False
			edit = True

		# delete case
		elif s1[i] != s2[j] and s1[i] == s2[j+1]:
			j += 1
			if edit:
				return False
			edit = True

		# replace case
		elif s1[i] != s2[j] and s1[i+1] == s2[j+1]:
			i += 1
			j += 1
			if edit:
				return False
			edit = True

		else:
			i += 1
			j += 1

	return True


# 1.6: compress a string, representing repeat characters with a count following the character


def compress_string(s):
	prevchar = s[0]
	retstring = ''
	count = 0
	for char in s:

		if char == prevchar:
			count += 1

		if char != prevchar:
			retstring += prevchar + str(count)
			count = 1

		prevchar = char

	retstring += prevchar + str(count)

	if len(retstring) <= len(s):
		return retstring

	else:
		return s


# 1.7: rotate matrix clockwise in place

def rotate_matrix(matrix):

	for i in range(0, 4):
		saverow = matrix[0]

# 1.8
# 1.9



