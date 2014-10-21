def getLargestPrimeFactor(n):
    primeFactors = []
    i = 2
    while(True):
        if isPrime(i) and n % i == 0:
            n = n / i;
            primeFactors.append(i)
        else:
            i += 1
        if n == 1:
            break

    return max(primeFactors)    
                
def isPrime(m):
    factors = 0
    for i in range(m+1):
        if i == 0:
            continue
        if m % i == 0:
            factors += 1
    if (factors == 2):
        return True
    return False

    
if __name__ == '__main__':
    print getLargestPrimeFactor(600851475143)