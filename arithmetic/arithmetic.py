from operator import add, sub, mul
from random import randint, choice


def main():
    operand_1 = int(randint(2, 9))
    operand_2 = int(randint(2, 9))
    operator_symbol = choice("*+-")

    match operator_symbol:
        case "+":
            op_func = add
        case "-":
            op_func = sub
        case "*":
            op_func = mul

    program_solution = op_func(operand_1, operand_2)
    print(operand_1, operator_symbol, operand_2, sep=" ")
    user_sulution = int(input())
    result = "Right!" if program_solution == user_sulution else "Wrong!"
    print(result)


if __name__ == "__main__":
    main()
