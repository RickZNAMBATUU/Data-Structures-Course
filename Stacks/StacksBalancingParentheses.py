from StacksModule import Stacks


class BalancingParentheses:
    def __init__(self):
        self.stacks = Stacks()

    def is_match(self, open_paren, close_paren):
        if open_paren == "{" and close_paren == "}":
            return True
        elif open_paren == "(" and close_paren == ")":
            return True
        elif open_paren == "[" and close_paren == "]":
            return True
        else:
            return False

    def is_parentheses_balanced(self, paren_string):
        is_balanced = True
        index = 0

        while index < len(paren_string) and is_balanced:
            paren = paren_string[index]
            if paren not in "[]{}()":
                is_balanced = True
            elif paren in "[({":
                self.stacks.push(paren)
            else:
                if self.stacks.is_empty():
                    is_balanced = False
                else:
                    top = self.stacks.top()
                    if self.is_match(top, paren):
                        self.stacks.pop()
                    else:
                        is_balanced = False
            index += 1

        if self.stacks.is_empty() and is_balanced:
            return True
        else:
            return False
