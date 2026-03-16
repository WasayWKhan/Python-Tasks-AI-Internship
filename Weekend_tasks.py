# =========================================
# AI Internship - Weekend Python Tasks
# Author: Wasay Khan
# =========================================

# Task 1 — FizzBuzz (1 to 50)
print("\n----- Task 1: FizzBuzz -----")

for i in range(1, 51):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)



# Task 2 — Leap Year Logic
print("\n----- Task 2: Leap Year Check -----")

def is_leap_year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

    return False


test_years = [1900, 2000, 2024, 2100, 2400]

for year in test_years:
    print(year, "->", is_leap_year(year))



# Task 3 — Identity vs Equality
print("\n----- Task 3: Identity vs Equality -----")

L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 3, 4, 5]
L3 = L1

print("L1 == L2 :", L1 == L2)
print("L1 is L2 :", L1 is L2)

print("L1 == L3 :", L1 == L3)
print("L1 is L3 :", L1 is L3)



# Task 4 — Bitwise Swap (XOR)
print("\n----- Task 4: Bitwise Swap -----")

a = 987654
b = 123456

print("Before swap:", a, b)

a = a ^ b
b = a ^ b
a = a ^ b

print("After swap:", a, b)



# Task 5 — First 10 Prime Numbers
print("\n----- Task 5: First 10 Prime Numbers -----")

count = 0
number = 2

while count < 10:

    for i in range(2, number):
        if number % i == 0:
            break

    else:
        print(number)
        count += 1

    number += 1



# Task 6 — Loop Breaker
print("\n----- Task 6: Loop Control -----")

for i in range(1, 21):

    if i == 18:
        print("Breaking loop at:", i)
        break

    if i == 13:
        print("Skipping unlucky number:", i)
        continue

    if i % 4 == 0:
        pass

    print(i)



# Task 7 — Grade Evaluation
print("\n----- Task 7: Grade Calculator -----")

def grade(score):

    if score >= 90:
        return "A"

    elif score >= 80:
        return "B"

    elif score >= 70:
        return "C"

    else:
        return "Fail"


scores = [96, 88, 73, 69, 91]

for s in scores:
    print("Score:", s, "Grade:", grade(s))



# Task 8 — Reverse Integer
print("\n----- Task 8: Reverse Integer -----")

num = 907856341
rev = 0
temp = num

while temp > 0:

    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print("Original number:", num)
print("Reversed number:", rev)



# Task 9 — Runner-Up Score
print("\n----- Task 9: Runner-Up Score -----")

scores = [78, 92, 92, 85, 91, 88, 91]

highest = max(scores)

runner_up = max(x for x in scores if x != highest)

print("Scores:", scores)
print("Highest:", highest)
print("Runner-up:", runner_up)



# Task 10 — Remove Duplicates
print("\n----- Task 10: Remove Duplicates -----")

numbers = [4, 7, 7, 2, 9, 2, 5, 4, 8, 9]

unique_numbers = list(set(numbers))

print("Original list:", numbers)
print("Unique list:", unique_numbers)



# Task 11 — List Intersection
print("\n----- Task 11: List Intersection -----")

L1 = [12, 45, 67, 89, 23, 45]
L2 = [90, 23, 45, 11, 67]

intersection = [x for x in L1 if x in L2]

print("List 1:", L1)
print("List 2:", L2)
print("Common elements:", intersection)



# Task 12 — Tuple Immutability
print("\n----- Task 12: Tuple Immutability -----")

t = ("AI", "Machine Learning", "Deep Learning")

try:

    t[1] = "Neural Networks"

except TypeError as e:

    print("Attempted modification error:", e)



# Task 13 — Character Frequency Counter
print("\n----- Task 13: Character Frequency -----")

text = "artificialintelligence"

freq = {}

for char in text:

    freq[char] = freq.get(char, 0) + 1

print("Text:", text)
print("Frequency:", freq)



# Task 14 — List Comprehension
print("\n----- Task 14: Squares of Even Numbers -----")

squares = [x**2 for x in range(1, 21) if x % 2 == 0]

print("Squares:", squares)



# Task 15 — Dictionary Comprehension
print("\n----- Task 15: Dictionary Comprehension -----")

d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

filtered_dict = {k:v for k,v in d.items() if v > 2}

print("Original dictionary:", d)
print("Filtered dictionary:", filtered_dict)
