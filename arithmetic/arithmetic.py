from operator import add, sub, mul
from random import randint, choice

LEVEL_DESCRIPTIONS = {
    "1": "simple operations with numbers 2-9",
    "2": "integral squares of 11-29",
}


class QuestionSimple:
    def __init__(self):
        self.operand_1 = int(randint(2, 9))
        self.operand_2 = int(randint(2, 9))
        self.operator_symbol = choice("*+-")
        self.operator_function = self._get_op_func()
        self.result = self._calc_solution()

    def _get_op_func(self):
        match self.operator_symbol:
            case "+":
                operator_function = add
            case "-":
                operator_function = sub
            case "*":
                operator_function = mul
        return operator_function

    def _calc_solution(self):
        return self.operator_function(self.operand_1, self.operand_2)

    def __str__(self):
        return f"{self.operand_1} {self.operator_symbol} {self.operand_2}"


class QuestionQuadric:
    def __init__(self):
        self.base = int(randint(11, 29))
        self.result = self._calc_solution()

    def _calc_solution(self):
        return self.base**2

    def __str__(self):
        return str(self.base)


def select_question_level():
    while True:
        print("Which level do you want? Enter a number:")
        for level, description in LEVEL_DESCRIPTIONS.items():
            print(level, "-", description, sep=" ")

        level = input()
        if level in LEVEL_DESCRIPTIONS.keys():
            return level
        else:
            print("Incorrect format.")
            continue


def select_question_template(level):
    match level:
        case "1":
            question_template = QuestionSimple
        case "2":
            question_template = QuestionQuadric
    return question_template


def execute_exam(question_template):
    mark = 0
    for _ in range(5):
        question = question_template()
        print(question)

        while True:
            try:
                user_sulution = int(input())
            except ValueError:
                print("Incorrect format.")
            else:
                break

        if question.result == user_sulution:
            print("Right!")
            mark += 1
        else:
            print("Wrong!")

    return mark


def is_request_save():
    print("Would you like to save your result to the file? Enter yes or no.")
    return input().lower() in {"yes", "y"}


def save_results(mark, level):
    print("What is your name?")
    username = input()
    with open("results.txt", "a") as f:
        f.write(
            f"{username}: {mark}/5 "
            f"in level {level} ({LEVEL_DESCRIPTIONS[level]})"
        )
    print('The results are saved in "results.txt".')

def main():
    level = select_question_level()
    question_template = select_question_template(level)
    mark = execute_exam(question_template)

    print(f"Your mark is {mark}/5.", end="")
    if is_request_save():
        save_results(mark, level)


if __name__ == "__main__":
    main()
