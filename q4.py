def getLargestPalindrome(numDigits):
    num = 0
    for i in range(numDigits):
        num += 9 * pow(10, i)
    maxProd = 0
    numRange = range(num + 1)
    numRange.reverse()
    for i in numRange:
        for j in numRange:
            if _isPalindrome(i * j) and i * j > maxProd:
                maxProd = i * j
                
    return maxProd

def _isPalindrome(n):
    digits = _getDigits(n)
    numDigits = len(digits)
    for i in range(numDigits / 2 + 1):
        digit1 = digits[i]
        digit2 = digits[numDigits - i - 1]
        if not (digit1 == digit2):
            return False
    return True 
        

def _getDigits(n):
    numDigits = _getNumDigits(n)
    digits = []
    for i in range(numDigits):
        div = pow(10, numDigits - i - 1)
        digits.append(n / div)
        n -= (n / div) * div
    return digits
        
def _getNumDigits(n):
    numDigits = 1
    while(True):
        n = n / 10;
        if n == 0:
            break
        numDigits += 1
    return numDigits

    
if __name__ == '__main__':
    print getLargestPalindrome(3)

