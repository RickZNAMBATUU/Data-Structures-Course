from StacksBalancingParentheses import BalancingParentheses
from StacksInfixToPostfix import InfixToPostfix
from StacksPostfix import PostfixEvaluation

balancing_parentheses = BalancingParentheses()
infix_to_postfix = InfixToPostfix()
postfix_evaluation = PostfixEvaluation()

infix_expression = "(((3+6)*(2-4))+7)"

if balancing_parentheses.is_parentheses_balanced(infix_expression):
    postfix_expression = infix_to_postfix.conversion(infix_expression)
    result = postfix_evaluation.evaluate_postfix(postfix_expression)
    print("Infix Expression: {}\nPostfix Expression: {}\nResult: {}".format(
        infix_expression, postfix_expression, result))
else:
    print("Expression Not Balanced!")
