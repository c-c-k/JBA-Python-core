from operator import add, sub, mul

def main():
    operand_1, operator_symbol, operand_2 = input().split()
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)

    match operator_symbol:
        case "+":
            op_func = add
        case "-":
            op_func = sub
        case "*":
            op_func = mul

    print(op_func(operand_1, operand_2))

    
if __name__ == "__main__":
    main()
