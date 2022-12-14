# This is the file you'll use to submit most of Lab 0.

# Certain problems may ask you to modify other files to accomplish a certain
# task. There are also various other files that make the problem set work, and
# generally you will _not_ be expected to modify or even understand this code.
# Don't get bogged down with unnecessary work.


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.

# You get to check multiple choice answers using the tester before you
# submit them! So there's no reason to worry about getting them wrong.
# Often, multiple-choice questions will be intended to make sure you have the
# right ideas going into the problem set. Run the tester right after you
# answer them, so that you can make sure you have the right answers.

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):
import math

ANSWER_1 = '2'

# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

def cube(x):
    return x ** 3

def factorial(x):
    return math.factorial(x)

def count_pattern(pattern, lst):
    pattern_index = 0
    matches = 0
    for char in lst:
        if char == pattern[pattern_index]:
            pattern_index += 1
        else:
            pattern_index = 0

        if pattern_index == len(pattern):
            matches += 1
            pattern_index = 0

    return matches

# Problem 2.2: Expression depth

def depth(expr):
    if type(expr) is list:
        max_depth = 1

        for i in expr:
            if type(i) is list:
                current_depth = 1 + depth(i)
                if current_depth > max_depth:
                    max_depth = current_depth

        return max_depth
    else:
        return 0


# Problem 2.3: Tree indexing

def tree_ref(tree, index):
    i = 0
    for node in tree:
        if index[0] == i:
            if type(node) is list and len(index[1:]) > 0:
                return tree_ref(node, index[1:])
            else:
                return node
        i += 1


# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod

# Section 4: Survey _________________________________________________________

# Please answer these questions inside the double quotes.

# When did you take 6.01?
WHEN_DID_YOU_TAKE_601 = "never"

# How many hours did you spend per 6.01 lab?
HOURS_PER_601_LAB = "0"

# How well did you learn 6.01?
HOW_WELL_I_LEARNED_601 = "never"

# How many hours did this lab take?
HOURS = "~5 (b/c i had to figure out how to get python 2 running and finding an IDE that would work with it, and also this whole lab I didn't know the PDF was available)"
