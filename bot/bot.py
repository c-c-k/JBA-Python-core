def main():
    print("Hello! My name is Aid.")
    print("I was created in 2020.")
    print("Please, remind me your name.")
    fleshbag_name = input()
    print(f"What a great name you have, {fleshbag_name}!")
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    remainder3, remainder5, remainder7 = [int(input()) for _ in range(3)]
    fleshbag_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {fleshbag_age}; "
          "that's a good time to start programming!")
    print("Now I will prove to you that I can count to any number you want.")
    for i in range(int(input()) + 1):
        print(f"{i} !")
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    while True:
        if input() == "2":
            break
        else:
            print("Please, try again.")
    print("Congratulations, have a nice day!")

if __name__ == "__main__":
    main()
