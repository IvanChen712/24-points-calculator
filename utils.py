import re


# define level for the four operands
def level(op):
    if op == '*' or op == '/':
        lv = 2
    else:
        lv = 1
    return lv


# find the position of an operand
def find_op_pos(eq, op):
    op_pos = []
    for i, char in enumerate(eq):
        if char in op:
            op_pos.append(i)
    return op_pos


def ops_same_level(eq):
    ops = extract_ops(eq)
    op_levels = [level(op) for op in ops]
    if all(le == op_levels[0] for le in op_levels):
        return True
    return False


def extract_numbers(expression):
    nums = re.findall(r'\d+', expression)
    nums = [int(num) for num in nums]
    nums.sort()
    return nums


def extract_ops(expression):
    ops = re.findall(r'[-+*/]', expression)
    ops = [op for op in ops]
    ops.sort()
    return ops
