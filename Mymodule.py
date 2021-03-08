def gcd(m, n):
    if n == 0:
        return 
    else:
        return gcd(n, m % n)

def sum(a, b):
    return a + b

def check_leap_year(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print("閏年")
    else:
        print("平年")

def hello_world():
    print("hello world")

def max(a, b):
    if a > b:
        return a
    else:
        return b
            