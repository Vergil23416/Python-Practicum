from itertools import product

OPERATORS = {
    'not': 'not',
    'and': 'and',
    'or': 'or',
    '^': '!=',
    '->': '<=',
    '~': '==',
}
PRIORITY = {
    'not': 0,
    'and': 1,
    'or': 2,
    '^': 3,
    '->': 4,
    '~': 5,
    '(': 6,
}


def convert_to_postfix(expression, variable_names):
    operator_stack, postfix_result, tokens = [], [], expression.split()
    for token in tokens:
        if token in variable_names:
            postfix_result.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                postfix_result.append(OPERATORS[operator_stack.pop()])
            operator_stack.pop()
        elif token in OPERATORS.keys():
            while len(operator_stack) and PRIORITY[token] >= PRIORITY[operator_stack[-1]]:
                postfix_result.append(OPERATORS[operator_stack.pop()])
            operator_stack.append(token)
    while operator_stack:
        postfix_result.append(OPERATORS[operator_stack.pop()])
    return postfix_result


def evaluate_postfix(postfix_expression, variable_values):
    evaluation_stack = []
    for token in postfix_expression:
        if token in variable_values.keys():
            evaluation_stack.append(variable_values[token])
        else:
            if token == 'not':
                evaluation_stack.append(not evaluation_stack.pop())
            else:
                operand2, operand1 = evaluation_stack.pop(), evaluation_stack.pop()
                eval_expression = f'{operand1} {token} {operand2}'
                evaluation_stack.append(eval(eval_expression))
    return int(evaluation_stack.pop())


s = input()
names = sorted(set([char for char in s if char.isupper()]))
print(' '.join(names), 'F')

rows = product([0, 1], repeat=len(names))
s = s.replace('(', '( ').replace(')', ' )')
postfix_expression_result = convert_to_postfix(s, names)

for truth_values in rows:
    variable_mapping = {variable: value for variable, value in zip(names, truth_values)}
    result = evaluate_postfix(postfix_expression_result, variable_mapping)
    print(' '.join(str(value) for value in truth_values), result)
