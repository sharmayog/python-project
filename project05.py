'''Design a module math_utils.py with functions:
factorial(n)
is_prime(n.)  
gcd(a,b){greatest common divisor}
Include exception handling for invalid or negative inputs.
import and test these functions from another script.
CONCEPTS: loops, recursion, functions, input validation'''

def factorial(n):
    if n==0 or n==1:
        return 1 
    result = 1
    for i in range (2 , n+1):
        result *= i
    return result

def is_prime(n):
    if n<2:
        return False
    for i in range (2 , n):
        if n%i == 0: 
            return False
        return True
    
def gcd (a,b):
    while b != 0 :
        a,b = b, a%b 
    return a 

print("factorial of 5 : " , factorial(5))
print("is 7 prime? " , is_prime(7))
print("GCD of 48 and 18: " , gcd(48,18))