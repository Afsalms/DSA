




def evaluate_prefix_expression(expression_string):
    print(expression_string)
    operators = ['+', '-', '*', '/']
    stack = []
    expression_list = expression_string.split(' ')
    for item in reversed(expression_list):
        if item not in operators:
            stack.insert(0, item)
        else:
            operand1 = stack.pop(0)
            operand2 = stack.pop(0)
            result = "( " + operand1 + " " + item + " " + operand2 + " )"
            stack.insert(0, result)
    return stack.pop()


expression_string = "+ * A B / C D"


evaluated_string = evaluate_prefix_expression(expression_string)

print("Evaluated string: ", evaluated_string)
print("----------------------------------")
