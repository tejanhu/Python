class Exercise1(object):

    # Retrieve input from user
    def getInput(self):
        user_input = input("Enter your name: ")
        return user_input

    # Evaluate whether input contains valid expression and return the result
    def evalInput(self):
        try:
            user_input = input("Type an expression to evaluate: ")
            if(eval(user_input)):
                some_list = [eval(user_input)]
                return eval(user_input)
            else:
                pass         
        except :
            print("Error: Valid Expression Expected!")

some_exercise = Exercise1()

some_exercise.getInput()
print(some_exercise.evalInput())

    