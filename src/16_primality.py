def is_prime(n):
    wall = (n**0.5)
    if n == 2 or n == 3:
        return True
    if (n < 2) or (n % 2 == 0 or n % 3 == 0):
        return False
    c, i = 5, 2
    while c <= wall:
        if n % c == 0:
            return False
        c += i
        i = 6 - i
    return True


print(is_prime(29996224275832))
