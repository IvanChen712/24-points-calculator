from itertools import permutations, product
from utils import extract_numbers, extract_ops, level, find_op_pos, ops_same_level
from consts import Goal, Number_count, Ops


# get numbers from user input
def get_numbers(length):
    num_list = []

    for i in range(length):
        while True:
            try:
                num = float(input(f'Number {i + 1}: '))
                if num.is_integer():
                    num = int(num)
                num_list.append(num)
                break
            except ValueError:
                print('Invalid input. Please enter a valid number.')

    return num_list


# get all possible equations without parentheses
def get_raw_equations(num_list, op_list):
    raw_equations = []

    for num_perm in set(permutations(num_list)):
        for op_perm in product(op_list, repeat=len(num_list) - 1):
            equation = "".join(f"{num}{op}" for num, op in zip(num_perm, op_perm))
            equation += str(num_perm[-1])
            raw_equations.append(equation)

    return raw_equations


# add parentheses to a raw equation
def add_parentheses(eq, pattern):
    poses = find_op_pos(eq, '+-*/')
    if pattern == 0:
        return f"(({eq[:poses[1]]}){eq[poses[1]:poses[2]]}){eq[poses[2]:]}"
    elif pattern == 1:
        return f"({eq[:poses[1]]}){eq[poses[1]]}({eq[poses[1]+1:]})"
    elif pattern == 2:
        return f"({eq[:poses[0]+1]}({eq[poses[0]+1:poses[2]]})){eq[poses[2]:]}"
    elif pattern == 3:
        return f"{eq[:poses[0]+1]}(({eq[poses[0]+1:poses[2]]}){eq[poses[2]:]})"
    elif pattern == 4:
        return f"{eq[:poses[0]+1]}({eq[poses[0]+1:poses[1]+1]}({eq[poses[1]+1:]}))"


# swap two parts in the equation
def swap_equation(index1, index2, index3, index4, eq):
    part1 = eq[index1:index2]
    part2 = eq[index3:index4]
    swapped_eq = eq[:index1] + part2 + eq[index2:index3] + part1 + eq[index4:]
    return swapped_eq


# get the beginning and ending indexes for two parts between an operand
def get_op_part(pos, eq):
    left_bracket_pos = find_op_pos(eq, '(')
    right_bracket_pos = find_op_pos(eq, ')')

    if eq[pos-1].isdigit():
        i = 1
        while pos - i >= 0 and eq[pos - i].isdigit():
            i += 1
        index1_begin = pos-i+1
        index1_end = pos

    else:
        if (len(list(filter(lambda x: x < pos, left_bracket_pos)))
                > len(list(filter(lambda x: x < pos, right_bracket_pos)))):
            # more left brackets in the left of the operand
            index1_begin = left_bracket_pos[1]
            index1_end = pos
        else:
            index1_begin = left_bracket_pos[0]
            index1_end = pos

    if eq[pos+1].isdigit():
        i = 1
        while pos + i < len(eq) and eq[pos + i].isdigit():
            i += 1
        index2_begin = pos + 1
        index2_end = pos + i

    else:
        if (len(list(filter(lambda x: x > pos, left_bracket_pos)))
                < len(list(filter(lambda x: x > pos, right_bracket_pos)))):
            # less left operands in the right of the operand
            index2_begin = pos + 1
            index2_end = right_bracket_pos[0] + 1
        else:
            index2_begin = pos + 1
            index2_end = right_bracket_pos[-1] + 1

    return index1_begin, index1_end, index2_begin, index2_end


# swap two parts between the operand according to its position
def swap_by_op_pos(op_pos, eq):
    index1_begin, index1_end, index2_begin, index2_end = get_op_part(op_pos, eq)
    swapped_eq = swap_equation(index1_begin, index1_end, index2_begin, index2_end, eq)
    return swapped_eq


# If eq1 and eq2 can become the same by swapping parts between "+" or "*", they are basically equal.
# By using recursion, we can deal with equations that have 2 or 3 operands.
# With this function, 3,3,7,7 will only give 1 solution.
def basically_equal(eq1, eq2, depth=0):
    if eq1 == eq2:
        return True

    op_positions = find_op_pos(eq1, '+') + find_op_pos(eq1, '*')
    max_depth = len(op_positions)

    if depth >= max_depth:
        return False

    for pos in op_positions:
        swapped_eq1 = swap_by_op_pos(pos, eq1)
        if basically_equal(swapped_eq1, eq2, depth + 1):
            return True


# add parentheses for all equations and remove duplicate and incorrect equations
def add_parentheses_all_check(eqs, goal):
    correct_equations = set()
    for eq in eqs:
        for pattern in range(5):
            equation_with_parentheses = add_parentheses(eq, pattern)
            try:
                if eval(equation_with_parentheses) == goal:
                    correct_eq = equation_with_parentheses
                    if all(not basically_equal(correct_eq, previous_eq) for previous_eq in correct_equations):
                        correct_equations.add(correct_eq)
            except ZeroDivisionError:
                continue
    return correct_equations


# judge whether a pair of parentheses can be removed
def can_del_parentheses(op1_pos, op2_pos, eq):
    if level(eq[op1_pos]) > level(eq[op2_pos]):
        return True
    elif op1_pos < op2_pos and level(eq[op1_pos]) == level(eq[op2_pos]):
        return True
    elif eq[op1_pos] == eq[op2_pos] and (eq[op1_pos] == '+' or eq[op1_pos] == '*'):
        return True
    return False


# delete redundant parentheses for an equation
def del_redundant_parentheses(eq):
    left_poses = find_op_pos(eq, '(')
    right_poses = find_op_pos(eq, ')')
    op_poses = find_op_pos(eq, '+-*/')
    corrected_eq = list(eq)

    if left_poses[1] < right_poses[0]:  # bracket in bracket
        for op_pos in op_poses:
            if op_pos in range(left_poses[1], right_poses[0]):
                op1_pos = op_pos
            elif op_pos in range(left_poses[0], right_poses[1]):
                op2_pos = op_pos
            else:
                op3_pos = op_pos

        if can_del_parentheses(op1_pos, op2_pos, eq):
            corrected_eq[left_poses[1]] = ' '
            corrected_eq[right_poses[0]] = ' '

        if can_del_parentheses(op2_pos, op3_pos, eq):
            corrected_eq[left_poses[0]] = ' '
            corrected_eq[right_poses[1]] = ' '

    else:  # brackets on two sides
        for op_pos in op_poses:
            if op_pos in range(left_poses[0], right_poses[0]):
                op1_pos = op_pos
            elif op_pos in range(left_poses[1], right_poses[1]):
                op2_pos = op_pos
            else:
                op3_pos = op_pos

        if can_del_parentheses(op1_pos, op3_pos, eq):
            corrected_eq[left_poses[0]] = ' '
            corrected_eq[right_poses[0]] = ' '

        if can_del_parentheses(op2_pos, op3_pos, eq):
            corrected_eq[left_poses[1]] = ' '
            corrected_eq[right_poses[1]] = ' '

    return ''.join(corrected_eq).replace(' ', '')


# delete redundant parentheses for all correct equations
def del_redundant_parentheses_all(eqs):
    corrected_equations = set()
    for eq in eqs:
        corrected_eq = del_redundant_parentheses(eq)
        corrected_equations.add(corrected_eq)
    return corrected_equations


# If an expression's operands have the same level, delete all versions that have parentheses.
def same_level_repeat_parentheses(eq):
    left_poses = find_op_pos(eq, '(')
    right_poses = find_op_pos(eq, ')')
    if len(left_poses) == 0:
        return False
    if ops_same_level(eq):
        return True
    else:
        if len(left_poses) == 2 and left_poses[1] < right_poses[0]:  # bracket in bracket
            return same_level_repeat_parentheses(eq[left_poses[0]+1:right_poses[1]])
    return False


def del_same_level_repeat_parentheses(eqs):
    new_eqs = set()
    for eq in eqs:
        if not same_level_repeat_parentheses(eq):
            new_eqs.add(eq)
    return new_eqs


# If an expression's operands have the same level, changing the order of numbers doesn't generate new solutions.
def same_level_repeat_order(eq, pre_eq):
    left_poses_eq = find_op_pos(eq, '(')
    right_poses_eq = find_op_pos(eq, ')')
    left_poses_pre_eq = find_op_pos(eq, '(')
    right_poses_pre_eq = find_op_pos(eq, ')')
    ops_eq = extract_ops(eq)
    ops_pre_eq = extract_ops(pre_eq)
    nums_eq = extract_numbers(eq)
    nums_pre_eq = extract_numbers(pre_eq)
    if len(left_poses_eq) != len(left_poses_pre_eq):
        return False
    if len(left_poses_eq) == 0:
        if ops_same_level(eq) and len(ops_eq) > 1:
            return sorted(nums_eq) == sorted(nums_pre_eq) and sorted(ops_eq) == sorted(ops_pre_eq)
        else:
            return False
    elif len(left_poses_eq) == 1:
        return same_level_repeat_order(eq[left_poses_eq[0]+1:right_poses_eq[0]]
                                       , eq[left_poses_pre_eq[0]+1:right_poses_pre_eq[0]])


def del_same_level_repeat_order(eqs):
    new_eqs = set()
    for eq in eqs:
        if all(not same_level_repeat_order(eq, prev_eq) for prev_eq in new_eqs):
            new_eqs.add(eq)
    return new_eqs


def cal_goal(nums, goal, ops):
    eqs = get_raw_equations(nums, ops)
    eqs = set(add_parentheses_all_check(eqs, goal))
    if len(eqs) != 0:
        eqs = del_redundant_parentheses_all(eqs)
        eqs = del_same_level_repeat_parentheses(eqs)
        eqs = del_same_level_repeat_order(eqs)
    return eqs


# print result info
def print_result(eqs):
    if len(eqs) == 0:
        print('No solution.')
    else:
        for eq in eqs:
            print(eq)
        print(f'{len(eqs)} solutions in total.')
    return


if __name__ == "__main__":
    numbers = get_numbers(Number_count)
    equations = cal_goal(numbers, Goal, Ops)
    print_result(equations)
