from StacksModule import Stacks

def operation(operator, op1, op2):
    if operator == "+":
        return op1 + op2
    elif operator == "-":
        return op1 - op2
    elif operator == "*":
        return op1 * op2
    elif operator == "/":
        return op1 / op2
    
def evaluate_prefix(expression):
    stacks = Stacks()
    index = -1
    for counter in expression:
        operand = expression[index]
        if operand in ["0","1","2","3","4","5","6","7","8","9"]:
            operand_int = int(operand)
            stacks.push(operand_int)
        else:
            operand_one = stacks.pop()
            operand_two = stacks.pop()
            result = operation(operand, operand_one, operand_two)
            stacks.push(result)
        index = index + (-1)
    return stacks.display_stacks()
    
expression = "-,+,*,2,3,*,5,4,9".split(",")
evaluate_prefix(expression)
