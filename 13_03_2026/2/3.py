def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    _i = 3
    while _i * _i < n:
        if n % _i == 0:
            return False
        _i += 2
    return True
    
number = int(input())

print(isprime(number))