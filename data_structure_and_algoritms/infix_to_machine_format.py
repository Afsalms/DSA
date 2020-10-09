



def convert_infix_postfix(string):
    stack = []
    postfix_string = ""
    operators = ['+', '-', '*', '/']
    for item in string:
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
    return postfix_string


def convert_infix_prefix(string):
    stack = []
    prefix_string = ""
    operators = ['+', '-', '*', '/']
    for item in reversed(string):
        print("item ", item)
        if item == ")":
            stack.insert(0, item)
        elif item == "(":
            while stack and (i:= stack.pop(0)) != ")":
               prefix_string += i
        elif item in operators:
            if item in ['*', '/'] and stack and stack[0] in operators:
                while stack and (i:= stack.pop(0)) != ")":
                    stack.insert(0, ")")
                    prefix_string += i
            stack.insert(0, item)
        else:
            prefix_string += item
    return prefix_string[::-1]



infix_string = input("Enter the infix expression")

a = convert_infix_postfix(infix_string)
b = convert_infix_prefix(infix_string)
print("postfix: ",a)
print("prefix: ", b)
