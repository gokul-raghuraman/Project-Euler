def getEvenFibSum():
    num = 1
    prevNum = 0
    sum = 0
    
    while(True):
        temp = prevNum
        prevNum = num
        num += temp
        
        if (num >= 4000000):
            break
        
        if (num % 2 == 0):
            sum += num
            
        print(str(num) + ", Sum : " + str(sum))

    
if __name__ == '__main__':
    getEvenFibSum()