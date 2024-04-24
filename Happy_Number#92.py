import random
#Problem:
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

#TODO:
#We must first get the square of digits from n
#We can get each digit by doing n // 2 for all digits except for the first, and to retrieve the first digit we get the remainder by j % 10.
#Then lets square the first placed value digit, and add to the result.
#Set num to the remaining digits by n // 2.
#We can create a helper function for that, and return the result.
#Repeat the process until the result equals 1, or loops endlessly.
#To determine if it loops endlessly, we can create a set for all the results that have been passed. If we encounter a repeat number then there is a cycle.


def squareOfNums(num):
    result = 0
    while num:
        #Obtain the first place valued digit.
        digit = num % 10
        #Multiply by 2
        digit = digit ** 2
        result += digit
        num = num // 10
    return result
        
def isHappy(n):
    previousResults = set()
    while n != 1:
        n = squareOfNums(n)
        if n in previousResults:
            return False
        previousResults.add(n)
    return True
randomNum = random.randint(1,100)
result = isHappy(randomNum)
if result is True:
    print(randomNum,"is a happy number :)")
else:
    print(randomNum,"is a sad number :(")
