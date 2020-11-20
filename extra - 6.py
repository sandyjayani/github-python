#Write a function called check_formula. The check_formula
#function should take as input one parameter, a string. It
#should return True if the string holds a correctly
#formatted arithmetic integer formula according to the rules
#below, or False if it does not.
#
#For this problem, here are the rules that define a
#correctly-formatted arithmetic string:
#
# - The only characters in the string should be digits or
#   the five arithmetic operators: +, -, *, /, and =. Any
#   other characters, including spaces, periods, commas,
#   or any letters, are not permitted.
# - There may not be any consecutive arithmetic operators.
#   Any arithmetic operator must have a number on either
#   side of it.
# - There must be an equals sign in the formula.
#
#You do not need to worry about negative numbers or
#parentheses, and you do not need to worry about whether
#the equation is accurate. You may also assume all the
#numbers in the string will be only one digit.
#
#Here are some examples of valid and invalid arithmetic
#formulas:
#
#   Valid     Invalid
#   5*3=5+2   5*3+5+2 (no equals)
#   5=7       5= (equals sign isn't in the middle)
#   5=2-5     50=-5 (consecutive arithmetic operators)
#   6/2=5/2   a=51 (illegal character)
#             -5=5+2 (starts with an operator)
#
#Hint: Remember, as soon as you find *one* thing wrong
#with the string, you know it's invalid and can return
#False. So, go character-by-character through the string
#checking everything that could be wrong. If you don't
#find anything wrong, return True!


#Write your function here!
def check_formula(formula):
    symbols = ['+', '-', '*','/' , '=']
    found_equals = False
    found_op = False
    
    for i in range (len(formula)):
        character = formula[i]
        if character in symbols: #checks against symbol list
            if found_op:
                return False
            if i==0 or i == len(formula) -1: #checks if symbol at beg or end
                return False
            if not formula[i-1].isdigit() or not formula[i+1].isdigit():
                return False #checks if digit on either side symbol
            found_op = True
            if character == '=': #checks f equal symbol
                found_equals = True
        elif character.isdigit(): #checks if is a digit
            found_op = False #false if not allowed symbol nor a digit
        else:
            return False
    if not found_equals: 
        return False
    
    return True

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print True, then several Falses.
print(check_formula("5*3=5+2"))
print(check_formula("5*3+5+2"))
print(check_formula("5="))
print(check_formula("5=-5"))
print(check_formula("a=5"))
print(check_formula("-5=5+2"))




