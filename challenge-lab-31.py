#!/usr/bin/env python3

import random

# PART 1: create wordbank list

wordbank = ["indentation", "spaces"]

# PART 2: create student list

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

# tlgstudents = ['Albert', 'Anthony']

# PART 3: append 4 to wordbank list

wordbank.append(4)

# PART 4: get user input for numbers 0 - 20 and save as variable num

# num = input('Choose a number between 0 and 20: ')

num = int(input(f"Enter a number between 1 and {len(tlgstudents)}: ")) - 1 # Bonus 2 solution

# PART 5: convert num to integer

num = int(num)

# PART 5: create variable student_name to save sliced index

student_name = tlgstudents[num]

# student_name = tlgstudents[random.randint(0,20)] # Bonus 1 solution

# PART 6: print output in format: <student_name> always uses <4> <spaces> to indent.

print(student_name, 'always uses', wordbank[2], wordbank[1], 'to indent.')

# BONUS 1: randomize what student name is picked

# BONUS 2: set num to account for changing list lengths and code input() to allow user to type a number beginning from 1

# num = input(('Choose a number from 1 to ' + str(len(tlgstudents))) + ': ')
