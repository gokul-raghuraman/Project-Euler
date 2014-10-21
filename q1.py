def getSum(n=1000):
    sum = 0
    for i in range(n - 1):
        if (i + 1) % 3 == 0 or (i + 1) % 5 == 0:
            sum += i + 1
    print sum
    
if __name__ == '__main__':
    getSum()