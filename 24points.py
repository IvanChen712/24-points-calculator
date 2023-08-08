from itertools import permutations, product

Goal = 24
Number_count = 4
Ops = ['/', '*', '+', '-']


def level(op):
    if op == '*' or op == '/':
        lv = 2
    else:
        lv = 1
    return lv


def get_numbers(length):
    num_list = [0] * length
    for i in range(length):
        num_list[i] = input(f'Number {i + 1}:')
    return num_list


def get_raw_equations(num_list, op_list):
    raw_equations = []

    for num_perm in set(permutations(num_list)):
        for op_perm in product(op_list, repeat=len(num_list) - 1):
            equation = "".join(f"{num}{op}" for num, op in zip(num_perm, op_perm))
            equation += str(num_perm[-1])
            raw_equations.append(equation)

    return raw_equations


# This only works for 4 numbers.
def add_parentheses(eq, pattern):
    if pattern == 0:
        return f"(({eq[:3]}){eq[3:5]}){eq[5:7]}"
    elif pattern == 1:
        return f"({eq[:3]}){eq[3]}({eq[4:7]})"
    elif pattern == 2:
        return f"({eq[:2]}({eq[2:5]})){eq[5:7]}"
    elif pattern == 3:
        return f"{eq[:2]}(({eq[2:5]}){eq[5:7]})"
    elif pattern == 4:
        return f"{eq[:2]}({eq[2:4]}({eq[4:7]}))"


def find_op_pos(eq, op):
    op_pos = []
    for i, char in enumerate(eq):
        if char == op:
            op_pos.append(i)
    return op_pos


def swap_equation(index1, index2, index3, index4, eq):
    part1 = eq[index1:index2]
    part2 = eq[index3:index4]
    swapped_eq = eq[:index1] + part2 + eq[index2:index3] + part1 + eq[index4:]
    return swapped_eq


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
            # 左边的左括号比右括号多
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
            # 右边的左括号比右括号少
            index2_begin = pos + 1
            index2_end = right_bracket_pos[0] + 1
        else:
            index2_begin = pos + 1
            index2_end = right_bracket_pos[-1] + 1

    return index1_begin, index1_end, index2_begin, index2_end


def add_parentheses_all_check(eqs, goal):
    correct_equations = set()
    for eq in eqs:
        for pattern in range(5):
            equation_with_parentheses = add_parentheses(eq, pattern)
            try:
                if eval(equation_with_parentheses) == goal:
                    correct_eq = equation_with_parentheses
                    # print(correct_eq)
                    plus_pos = find_op_pos(correct_eq, '+')
                    multiply_pos = find_op_pos(correct_eq, '*')
                    # print(f'pos: {plus_pos + multiply_pos}')
                    flag = True
                    for i in plus_pos + multiply_pos:
                        index1_begin, index1_end, index2_begin, index2_end = get_op_part(i, correct_eq)
                        swapped_eq = swap_equation(index1_begin, index1_end, index2_begin, index2_end, correct_eq)
                        # print(f'seq: {swapped_eq}')
                        if swapped_eq in correct_equations:
                            flag = False
                            break
                    if flag:
                        correct_equations.add(correct_eq)
            except ZeroDivisionError:
                continue
    return correct_equations


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
    equations = get_raw_equations(numbers, Ops)
    equations = set(add_parentheses_all_check(equations, Goal))
    print_result(equations)
