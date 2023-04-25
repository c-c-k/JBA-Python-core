try: 
    from .messages import HABITATS
except ImportError:
    from messages import HABITATS


def main():
    print('Please enter the number of the habitat '
          'you would like to view:')
    print('enter "exit" to exit the Zoo Keeper.')
    while True:
        command = input()
        if command == 'exit':
            break
        try:
            habitat_id = int(command)
        except ValueError:
            print('habitat id must be a number, please try again.')
        else:
            if 0 <= habitat_id < len(HABITATS):
                print(HABITATS[habitat_id])
            else:
                print('habitat id not found, please try again')
    print('See you later!')


if __name__ == "__main__":
    main()
