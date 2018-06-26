numlist = [0,2,4,6,8,3,5,9,1,4]

def doSomethingAgain(num1,num2):
    sum = num1+num2
    product = num1*num2
    if(num1==0):
        return num2
    else:
        return num1

# for i in list
print(doSomethingAgain(numlist[0:9],numlist[0:9]))
