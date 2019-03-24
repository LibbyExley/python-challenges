"""
Write a program that prints the numbers from 1 to 100. If it’s a multiple of 3, 
it should print “Fizz”. If it’s a multiple of 5, it should print “Buzz”. 
If it’s a multiple of 3 and 5, it should print “Fizz Buzz”.
"""
numbers = list(range(1,101))
for number in numbers:
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

