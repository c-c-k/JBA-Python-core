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
    print(f"Your age is {fleshbag_age}; that's a good time to start programming!")

if __name__ == "__main__":
    main()
