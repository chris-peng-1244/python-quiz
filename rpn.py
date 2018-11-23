PLUS = '+'
MINUS = '-'
TIMES = '*'
DIVIDE = '/'

OPERANDS = [PLUS, MINUS, TIMES, DIVIDE]

def rpn(expr):
    stack = []
    for val in expr:
        if val in OPERANDS:
            term1, term2 = stack.pop(), stack.pop()
            if val == PLUS:
                stack.append(term1+term2)
            elif val == MINUS:
                stack.append(term1 - term2)
            elif val == TIMES:
                stack.append(term1 * term2)
            elif val == DIVIDE:
                stack.append(term1 / term2)
        else:
            stack.append(val)
    return stack[0]

result = rpn([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1,'+', '+', '-'])
print(result)