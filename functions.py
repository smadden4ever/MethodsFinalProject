import math
import pytest

## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    infile = open(filename, "r")

    print("File opened.")

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    return num1 / num2

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)

    return dist

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    test = temp[::-1]

    if(test == temp):
        return True

    else:
        return False

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    div = num1 / num2

    print("Your numbers divided is:", div)

## returns the squareroot of a particular number
def sq(num):
    return math.sqrt(num)

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    print("Your item at", index, "index is", numbers[index])


##################Test Files#################
##not worked
def test_openFile():
    assert openFile("testing.txt") == None

##not worked
def test_numbers():
    assert numbers() == 4

##not worked
def test_dist():
    assert dist() == 9

##not worked
def test_isPalindrome():
    assert isPalindrome("hello") == 0

##not worked
def test_divide():
    assert divide(1,2) == .5

##not worked
def test_sq():
    assert sq(2) == 0

##not worked
def test_greetUser():
    assert greetUser("hello", "something", "somthing") == None

##not worked
def test_displayItem():
    assert displayItem([1,2,3,4], 2) == 4

