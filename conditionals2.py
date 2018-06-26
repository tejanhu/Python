def doSomethingAgain(num1,num2,flag):
    sum = num1+num2
    product = num1*num2
    if(flag):
        return sum
    elif(num1==0):
        return num2
    elif(num2==0):
        return num1
    else:
        return product

print(doSomethingAgain(1,2,None))
