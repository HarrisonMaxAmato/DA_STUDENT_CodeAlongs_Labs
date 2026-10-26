#!/usr/bin/env python3
"""Day 1 code-along: Control Flow & Conditionals. Run: python3 <file>"""

# ===== 1. If/Elif/Else, Live =====
# Print "Too hot", "Too cold", or "Just right" based on temperature.
print('----- 1. If/Elif/Else, Live -----')
<<<<<<< HEAD
# TODO: set temperature to any number, then write the
# if/elif/else check yourself before revealing the answer
foodweight = 20
if foodweight > 20:
    print("Too heavy")
elif foodweight < 20:
    print("Too light")
else:
    print("Just right")
foodweight = 20
# >20 too heavy, <20 too light, =20 just right
=======
# TODO: set temperature to any number
# TODO: write the if/elif/else check yourself
temperature = 71


>>>>>>> upstream/main
# ===== 2. For Loop, Live =====
# Print the four scores, one per line, so the output is 88, 92, 75, then 100.
print('----- 2. For Loop, Live -----')
# TODO: write a for loop that prints every value in scores
scores = [88, 92, 75, 100]
for item in scores:
    print(item)


# ===== 3. range() Generates Numbers to Loop Over =====
# Count from 0 to 4 with range(). Notice it stops before 5.
print('----- 3. range() Generates Numbers to Loop Over -----')
# TODO: use range() to print the numbers 0 through 4
<<<<<<< HEAD
for i in range(5):
    print(i)
print(range(5))
# PREDICT before you run: Change range(5) to range(3). What does the loop print
#                         now?
=======

# PREDICT before you run: Change range(5) to range(3). What prints now?
>>>>>>> upstream/main
# Your answer:
#


# ===== 4. While Loop, Live =====
# Count up from 0 and stop after 3, printing 0, 1, 2, 3.
# DISCUSS: Put these in order: A: run body. B: check again. C: first check.
# Your answer:
#
print('----- 4. While Loop, Live -----')
# TODO: write a while loop that prints 0, 1, 2, 3 (check the condition!)
count = 0

# PREDICT before you run: Make it count < 3, not count <= 3. How many print?
# Your answer:
#


# ===== 5. Loop and Conditional, Together =====
# Label each score: 90+ gets "great job", lower gets "keep practicing".
print('----- 5. Loop and Conditional, Together -----')
# TODO: loop over scores; print "great job" if a score is 90 or above
# TODO: otherwise print "keep practicing"
scores = [88, 92, 75, 100]
for score in scores:
    if score >= 90:
        print("great job")
    else:
        print("keep practicing")