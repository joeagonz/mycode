#!/usr/bin/env python3

import random

wordbank = ["indentation", "spaces"]
wordbank.append(4)
tlgstudents = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Heidi", "Isaac", "Julia", "Katie", "Liam", "Mia", "Nathan", "Olivia", "Peter", "Quincy", "Rachel", "Samuel", "Tina", "Ulysses"]

while True:
    try:
        num = int(input(f"Enter a number between 1 and {len(tlgstudents)}: ")) - 1
        if num < 0 or num >= len(tlgstudents):
            print("Invalid input. Please enter a number between 1 and", len(tlgstudents))
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and", len(tlgstudents))

student_name = tlgstudents[num]

print(f"{student_name} always uses {wordbank[-1]} {wordbank[1]} to indent.")

