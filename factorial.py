# factorial.py

import time

def factorial(n):
    time.sleep(0.1)
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def sum_factorial():
    results = []
    for i in range(50):
        results.append(factorial(i))
    total = sum(results)
    print("Final SUM = {}".format(total))
    return total

if __name__ == "__main__":
    sum_factorial()
