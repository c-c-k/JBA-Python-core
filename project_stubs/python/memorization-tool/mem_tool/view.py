from . import messages as msg
from . import model


def print_message(message):
    print(message.strip())


def get_user_input(message):
    print_message(message)
    return input().strip()


# main menu
def get_menu_choice_main():
    return get_user_input(msg.MENU_MAIN)


# add_flashcards menu
def get_menu_choice_add_flashcards():
    return get_user_input(msg.MENU_ADD_FLASHCARD)


# get new flashcard data
def get_non_blank_input(prompt):
    while True:
        print_message(prompt)
        test_input = input().strip()
        if test_input != "":
            return test_input


def flashcard_create():
    question = get_non_blank_input(msg.PROMPT_NEW_QUESTION)
    answer = get_non_blank_input(msg.PROMPT_NEW_ANSWER)
    model.add_new_flashcard({"question": question, "answer": answer})


# practice flashcards
def print_no_flashcards():
    print_message(msg.ERROR_NO_FLASHCARDS)


def get_menu_choice_practice(flashcard):
    return get_user_input(
        msg.MENU_PRACTICE.substitute(
            question=flashcard.question))


# update flashcards
def get_menu_choice_update_flashcard():
    return get_user_input(msg.MENU_UPDATE_FLASHCARD)


def flashcard_update_edit(flashcard):
    flashcard_data = {}
    for attribute in ['question', 'answer']:
        new_value = get_user_input(
            msg.PROMPT_EDIT_FLASHCARD.substitute(
                attribute=attribute,
                current_value=getattr(flashcard, attribute)))
        if new_value != "":
            flashcard_data[attribute] = new_value
    model.update_flashcard(flashcard, flashcard_data)


def flashcard_update_delete(flashcard):
    model.delete_flashcard(flashcard)


# Learning by Leitner system
def get_menu_choice_learning(flashcard):
    return get_user_input(
        msg.MENU_LEARNING.substitute(
            answer=flashcard.answer))


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
