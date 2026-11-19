**Topic: Python Functions**
**Level: Beginner to Intermediate**
**Total Questions: 10**
Instructions: Choose the correct option (A, B, C or D) for each question.
Section A: Basic Concepts of Functions**

# Q1. Which keyword is used to define a function in Python?

    A) function

    B) def

    C) define

    D) fun

# Q2. What is the purpose of the return statement in Python?

    A) To print a value

    B) To repeat a function

    C) To return a value from a function

    D) To define a variable

# Q3. What will be the output of the following program?
python

def greet():
    print("Hello Python")

greet()

    A) Hello

    B) Python

    C) Hello Python

    D) Error

Section B: Output-Based Programs Using Functions

# Q4. What will be the output?
python

def add(a, b):
    return a + b

print(add(10, 20))

    A) 10

    B) 20

    C) 30

    D) 1020

# Q5. What will be the output?
python

def square(n):
    return n * n

print(square(5))

    A) 10

    B) 15

    C) 20

    D) 25

# Q6. What will be the output?
python

def display(name):
    print("Welcome", name)

display("Rahul")

    A) Welcome

    B) Rahul

    C) Welcome Rahul

    D) Error

# Q7. What will be the output?
python

def calculate(x):
    return x * 2

a = calculate(5)
print(a + 3)

    A) 8

    B) 10

    C) 13

    D) 15

# Q8. What will be the output?
python

def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check(9))

    A) Even

    B) Odd

    C) 9

    D) None

# Q9. What will be the output?
python

def test(a, b=5):
    return a + b

print(test(10))

    A) 5

    B) 10

    C) 15

    D) 50

# Q10. What will be the output?
python

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))

    A) 4

    B) 10

    C) 16

    D) 24