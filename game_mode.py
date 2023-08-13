import random

from calculator import cal_goal, print_result
from consts import Goal, Ops
from utils import extract_numbers


# Choose four random integers from 1~13
def random_numbers():
    nums = [random.randint(1, 13) for _ in range(4)]
    print(f"The four numbers are {nums}")
    print(f"If you think there is no solution, input 'No'.")
    print(f"Otherwise, input the expression with no spaces.")
    return nums


def get_input(nums):
    ans = input("😚 Please input your answer:")
    if ans == 'No':
        return ans
    if extract_numbers(ans) != sorted(nums):
        print("You should use all and only use the numbers given.😅😅😅 ")
        return get_input(nums)

    try:
        val = eval(ans)
        return val
    except (NameError, ZeroDivisionError, ValueError):
        print("Invalid input.😅 Please input again.")
        return get_input(nums)


def check_answer(answer, goal, nums, ops):
    if answer == goal:
        print("Correct!🤩 Do you want to see all the solutions? [y/n]")
        while True:
            choice = input()
            if choice == 'y':
                print_result(cal_goal(nums, goal, ops))
                break
            elif choice == 'n':
                print("OK. Solutions will not be presented.")
                break
            else:
                print("What are you doing?🤔 Please input y/n.")
        return True
    elif answer == 'No' and len(cal_goal(nums, goal, ops)) == 0:
        print("Brilliant!😍 You are so smart.😚 ")
        return True
    else:
        if len(cal_goal(nums, goal, ops)) == 0:
            print("HAHA!😀 Actually, there is no solution.😝🤗 ")
        else:
            print("HAHA!😄 You lose.🤣👉🤡 ")
            print_result(cal_goal(nums, goal, ops))
        return False


if __name__ == "__main__":
    numbers = random_numbers()
    player_answer = get_input(numbers)
    check_answer(player_answer, Goal, numbers, Ops)
