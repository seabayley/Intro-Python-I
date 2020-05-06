def eratosthenes(n):
    # Populate a list with True
    primes = [True for i in range(n+1)]
    # We start at 2 because a number must be greater than 1 to be prime.
    p = 2
    # Prevents us from going past the sqrt of n.
    while (p * p <= n):
        # Only check an integer if it hasn't been marked as composite.
        if (primes[p] == True):
            # From the square of p to n+1, step by p.
            for i in range(p*p, n+1, p):
                # Mark each as composite.
                primes[i] = False
        # Increment p by 1 to check the next.
        p += 1
    # Iterate over each integer in range 2 to n
    for p in range(2, n):
        # Check if it has not been marked composite.
        if primes[p]:
            # print it out =D
            print(p)


eratosthenes(30)
