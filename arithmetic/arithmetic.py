from operator import add, sub, mul
from random import randint, choice

class Question:
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
        


def main():
    correct_answers = 0

    for _ in range(5):
        question = Question()
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
            correct_answers += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct_answers}/5.")


if __name__ == "__main__":
    main()
