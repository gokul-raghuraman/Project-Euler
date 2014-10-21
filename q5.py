def getMinMultiple(n):
    num = 1;
    while(True):
        divisible = True
        for i in range(n + 1):
            if not (num % (i + 1) == 0):
                divisible = False
                print(str(num) + " is not divisible by " + str(i + 1))
        if divisible == True:
            return num
        num += 1
        
def getLCM(numRange):
    multiples = []
    divisor = 2
    numList = range(numRange+1)[1:]
    while(True):
        if not _isPrime(divisor):
            divisor += 1
            continue
        
        isMultiple = False
        for i in range(len(numList)):
            if (numList[i] % divisor == 0):
                numList[i] /= divisor
                isMultiple = True

        if isMultiple:
            multiples.append(divisor)
        else:
            divisor += 1
            continue
        allOnes = True
        for num in numList:
            if not num == 1:
                allOnes = False
                break    
        if allOnes:
            break
    
    lcm = 1    
    for multiple in multiples:
        lcm *= multiple
         
    return lcm
                
    
def _isPrime(m):
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
    print getLCM(20)