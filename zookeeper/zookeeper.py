try: 
    from .messages import HABITATS
except ImportError:
    from messages import HABITATS


def main():
    print('Please enter the number of the habitat '
          'you would like to view:')
    while True:
        try:
            habitat_id = int(input())
        except ValueError:
            print('habitat id must be a number, please try again.')
        else:
            if 0 <= habitat_id < len(HABITATS):
                print(HABITATS[habitat_id])
                break
            elif habitat_id == -1:
                print('exiting, have a good day')
                break
            else:
                print('habitat id not found, please try again')
        print('enter "-1" to exit')
    print("---\nYou've reached the end of the program. "
          'To check another habitat, please restart the watcher.')


if __name__ == "__main__":
    main()
