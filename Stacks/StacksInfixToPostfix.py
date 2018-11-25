from StacksModule import Stacks


class InfixToPostfix:
    def __init__(self):
        self.stacks = Stacks()

    def higher_precedence(self, op1, op2):
        if op1 == op2:
            return True
        else:
            if (op1 == "+" and op2 == "-") or (op1 == "-" and op2 == "+"):
                return True
            elif (op1 == "*" and op2 == "/") or (op1 == "/" and op2 == "*"):
                return True
            elif (op1 == "*" and op2 == "+") or (op1 == "*" and op2 == "-"):
                return True
            elif (op1 == "/" and op2 == "-") or (op1 == "/" and op2 == "+"):
                return True
            else:
                return False

    def conversion(self, infix_expression):
        result = ""
        index = 0

        for counter in range(len(infix_expression)):
            item = infix_expression[index]
            if item in "({[":
                self.stacks.push(item)
            elif item not in "*/+-({[]})":
                operand = item
                result += operand
            else:
                operator = item
                while not self.stacks.is_empty():
                    if operator in "})]":
                        if self.stacks.top() in "{([":
                            self.stacks.pop()
                        else:
                            result += self.stacks.pop()
                    else:
                        if self.higher_precedence(self.stacks.top(), operator):
                            result += self.stacks.pop()
                        else:
                            break

                if operator in ")]}":
                    self.stacks.push(operator)
                    self.stacks.pop()
                else:
                    self.stacks.push(operator)
            index += 1

        while not self.stacks.is_empty():
            if self.stacks.top() in "[{()}]":
                self.stacks.pop()
            else:
                result += self.stacks.pop()
        return result


# a*b+(c-d) = ab*cd-+
# a*b+c = ab*c+
# a+b*c-d/e*f = abc*+de/f*-
# 2+3*4 = 234*+
# a*b+5 = ab*5+
# (3+4)/(5-2) = 34+52-/
# (1+2)*7 = 12+7*
# (((3+6)*(2-4))+7) = 36+24-*7+
# ((a/(b-c+d))*(e-a)*c) = abc-d+/ea-*c*
