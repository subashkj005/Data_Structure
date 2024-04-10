def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

"""

Recursion is a programming concept in which a function calls itself to solve a problem or perform a task.
the function repeatedly calls itself with a smaller or simpler input until it reaches a base case where a 
direct solution can be determined without further recursive calls.

Disadvantages:
 * It may consume more memory because each function call is added to the call stack


"""
