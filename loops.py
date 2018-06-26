def doSomethingAgain(num1,num2):
    sum = num1+num2
    product = num1*num2
    if(num1==0):
        return num2
    else:
        return num1

for i in range(10):
    print(doSomethingAgain(0,2))
