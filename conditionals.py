def doSomethingAgain(num1,num2,flag):
    sum = num1+num2
    product = num1*num2
    if(flag):
        return sum
    else:
        return product

print(doSomethingAgain(1,2,False))
