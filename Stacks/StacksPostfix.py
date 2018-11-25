from StacksModule import Stacks


class PostfixEvaluation:
    def __init__(self):
        self.stacks = Stacks()

    def operation(self, operator, op1, op2):
        if operator == "+":
            return op1 + op2
        elif operator == "-":
            return op1 - op2
        elif operator == "*":
            return op1 * op2
        elif operator == "/":
            return op1 / op2

    def evaluate_postfix(self, expression):
        for item in expression:
            if item not in "+/-*":
                operand_int = int(item)
                self.stacks.push(operand_int)
            else:
                operator = item
                operand_two = self.stacks.pop()
                operand_one = self.stacks.pop()
                result = self.operation(operator, operand_one, operand_two)
                self.stacks.push(result)

        total = 0
        for i in self.stacks.display_stacks():
            total += i
        return total
