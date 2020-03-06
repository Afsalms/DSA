



def convert_infix_postfix(string):
    stack = []
    postfix_string = ""
    operators = ['+', '-', '*', '/']
    for item in string:
        print("item: ", item)
        if item == "(":
            stack.insert(0, item)
        elif item == ")":
            while stack and (i:= stack.pop(0)) != "(":
               postfix_string += i
        elif item in operators:
            if item in ['*', '/'] and stack and stack[0] in operators:
                while stack and (i:= stack.pop(0)) != "(":
                    stack.insert(0, "(")
                    postfix_string += i
            stack.insert(0, item)
        else:
            postfix_string += item
        print("iteration ", stack)
        print(".....................................")
    return postfix_string




infix_string = "(A*(B+(C/D)))"

a = convert_infix_postfix(infix_string)

print("Result: ",a)
