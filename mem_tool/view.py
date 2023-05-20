from . import messages as msg


def print_message(message):
    print(message.strip())


def get_menu_choice(message):
    print_message(message)
    return input().strip()


# main menu
def get_menu_choice_main():
    return get_menu_choice(msg.MENU_MAIN)


# add_flashcards menu
def get_menu_choice_add_flashcards():
    return get_menu_choice(msg.MENU_ADD_FLASHCARD)


# get new flashcard data
def get_non_blank_input(prompt):
    while True:
        print_message(prompt)
        test_input = input().strip()
        if test_input != "":
            return test_input


def get_flashcard_data():
    question = get_non_blank_input(msg.PROMPT_NEW_QUESTION)
    answer = get_non_blank_input(msg.PROMPT_NEW_ANSWER)
    return {"question": question, "answer": answer}


# practice flashcards
def print_no_flashcards():
    print_message(msg.ERROR_NO_FLASHCARDS)


def practice_flashcard(flashcard):
    print_message(
        msg.INFO_SHOW_QUESTION.substitute(
            question=flashcard['question']))
    show_answer = get_menu_choice(msg.PROMPT_YES_NO_REVEAL_ANSWER)
    if show_answer == 'y':
        print_message(
            msg.INFO_SHOW_ANSWER.substitute(
                answer=flashcard['answer']))


def practice_flashcards(flashcards):
    for flashcard in flashcards:
        practice_flashcard(flashcard)


# print wrong choice message and redirect
def print_invalid_menu_choice_error(invalid_choice):
    print_message(
        msg.ERROR_INVALID_MENU_CHOICE.substitute(
            invalid_choice=invalid_choice))


# exit
def print_exit_message():
    print_message(msg.INFO_GOODBYE)


# unhandled command
def print_unhandled_command_message(*unhandled_command):
    print("ERROR: unhandled_command: ", unhandled_command)
