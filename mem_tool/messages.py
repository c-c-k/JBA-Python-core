from string import Template


ERROR_NO_FLASHCARDS = "There is no flashcard to practice!"
ERROR_INVALID_MENU_CHOICE = Template("${invalid_choice} is not an option")
INFO_GOODBYE = "Bye!"
MENU_ADD_FLASHCARD = """
1. Add a new flashcard
2. Exit
"""
MENU_UPDATE_FLASHCARD = """
press "d" to delete the flashcard:
press "e" to edit the flashcard:
"""
MENU_MAIN = """
1. Add flashcards
2. Practice flashcards
3. Exit
"""
MENU_LEARNING = Template("""
Answer: ${answer}
press "y" if your answer is correct:
press "n" if your answer is wrong:
""")
MENU_PRACTICE = Template("""
Question: ${question}
press "y" to see the answer:
press "n" to skip:
press "u" to update:
""")
PROMPT_EDIT_FLASHCARD = Template("""
current ${attribute}: ${current_value}
please write a new ${attribute}:
""")
PROMPT_NEW_ANSWER = "Answer:"
PROMPT_NEW_QUESTION = "Question:"
