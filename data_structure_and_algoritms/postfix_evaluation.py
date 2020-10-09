



def evaluate_postfix(expression_string):
    operators = ['+', '-', '*', '/']
    expression_list = expression_string.split(' ')
    stack = []
    for item in expression_list:
        if item not in operators:
            stack.insert(0, item)
        else:
            operand2 = stack.pop(0)
            operand1 = stack.pop(0)
            result = "(" + operand1 + " " + item + " " + operand2 + ")"
            stack.insert(0, result)
    return stack.pop()


expression_string = "A B * C D / +"


evaluated_string = evaluate_postfix(expression_string)

print("Evaluated string: ", evaluated_string)
print("----------------------------")
