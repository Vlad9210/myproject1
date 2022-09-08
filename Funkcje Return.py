
def return_number ():
    return 42
    
result = return_number()
print (result)


def square(x):
    return x * x
    
print (square(2))
print (square(6))


def absolute (x):
    if x >= 0:
        return x
    else:
        return -x
        
print (absolute(2))
print (absolute(-3))


def factorial (num):
    result = 1 
    for i in range (1, num + 1):
        result *= i
    return result
    
    
def factorial (num):
    if num <= 1:
        return 1 
        
    return num * factorial (num - 1)
    
print (factorial (4))


def days_to_millis (day): # zamienia liczbę dni na liczbę milisekund
    return day * 24 * 60 * 60 * 1000
    
print (days_to_millis(5))

def biggest (a, b, c): # zwraca największa liczbę
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c
        
print (biggest (3, 9, 6))


def open_website (url, incognito=False):
    if incognito:
        print (f"Opening {url} in incognito")
    else:
        print (f"Opening {url}")
        
open_website ("google.com")
open_website ("facebook.pl", incognito=True)
