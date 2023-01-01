#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Helper script for editing J.B.A topic questions and projects.

This script executes a number of frequently used helper actions
for solving J.B.A. topic questions and projects.
It is meant to be invoked by an IDE shortcut that executes an external
program on the currently edited file.
The IDE should pass the file path and required action to this script.
The currently implemented actions are:
  - Paste question_text text copied from the J.B.A. site into the currently
   edited action file (NOTE: The X selection used here is the PRIMARY
   selection, that is highlighted text and not <C-V>).
  - Copy the currently edited question_text's solution code to the clipboard
   (NOTE: The X selection used here is the clipboard selection,
   that is <C-C> and not highlighted text ).
"""

# --------------------
# --IMPORTS
# --------------------
# Standard library modules:
# import argparse
import enum
import os
import typing
from pathlib import Path
import re
import string
import subprocess
import time


# Third party modules:

# Local scripts and modules:


# --------------------
# --EXCEPTIONS
# --------------------
class JBAHelperNonFatalError(Exception):
    pass


# --------------------
# --DATA TYPES
# --------------------
class LanguageInfo(typing.NamedTuple):
    language: "Language"
    action_file: Path
    full_archive: Path
    censored_archive: Path
    file_suffix: str
    template_file: Path
    re_element_extractor: typing.Pattern
    re_answer_extractor: typing.Pattern


# --------------------
# --ENUMS AND CONSTANTS
# --------------------
# Supported actions.
class Action(enum.Enum):
    IMPORT_QUESTION = enum.auto()
    EXPORT_ANSWER = enum.auto()


# Supported programing languages.
class Language(enum.Enum):
    PYTHON = enum.auto()
    HTML_CSS = enum.auto()
    JAVASCRIPT = enum.auto()


# --------------------
# --PATHS
# --------------------
PATH_ACTIONS_REQUEST = Path(
    "/dev/shm/jba_helper_action_request")
PATH_ACTIONS_REQUEST_READING = Path(
    "/dev/shm/jba_helper_action_request.reading")
PATH_JBA_ROOT = Path(__file__).resolve().parents[1]
# Currently worked on questions' paths.
PATH_TOPIC_QUESTIONS_BASE = Path(
    PATH_JBA_ROOT, "topic_question_solutions/")
PATH_QUESTIONS_CURRENT_PYTHON = Path(
    PATH_TOPIC_QUESTIONS_BASE, "current.py")
PATH_QUESTIONS_CURRENT_HTML = Path(
    PATH_TOPIC_QUESTIONS_BASE, "current.html")
PATH_QUESTIONS_CURRENT_CSS = Path(
    PATH_TOPIC_QUESTIONS_BASE, "current.css")
PATH_QUESTIONS_CURRENT_JAVASCRIPT = Path(
    PATH_TOPIC_QUESTIONS_BASE, "current.js")
# Full solution archives (This should not be uploaded to a public
# GitHub repo out of licensing concerns).
PATH_ARCHIVE_FULL_BASE = Path(
    PATH_TOPIC_QUESTIONS_BASE, "archive/full/")
PATH_ARCHIVE_FULL_PYTHON = Path(
    PATH_ARCHIVE_FULL_BASE, "python/")
PATH_ARCHIVE_FULL_HTML_CSS = Path(
    PATH_ARCHIVE_FULL_BASE, "html_css/")
PATH_ARCHIVE_FULL_JAVASCRIPT = Path(
    PATH_ARCHIVE_FULL_BASE, "javascript/")
# Censored solution archives (The full question_text text is removed
# out of licensing concerns).
PATH_ARCHIVE_CENSORED_BASE = Path(
    PATH_TOPIC_QUESTIONS_BASE, "archive/censored/")
PATH_ARCHIVE_CENSORED_PYTHON = Path(
    PATH_ARCHIVE_CENSORED_BASE, "python/")
PATH_ARCHIVE_CENSORED_HTML_CSS = Path(
    PATH_ARCHIVE_CENSORED_BASE, "html_css/")
PATH_ARCHIVE_CENSORED_JAVASCRIPT = Path(
    PATH_ARCHIVE_CENSORED_BASE, "javascript/")
# Per programing language solution template file.
DIR_TEMPLATE_BASE = Path(
    PATH_JBA_ROOT, "jba_helper/answer_templates/")
PATH_TEMPLATE_PYTHON = Path(
    DIR_TEMPLATE_BASE, "python.template.txt")
PATH_TEMPLATE_HTML = Path(
    DIR_TEMPLATE_BASE, "html.template.txt")
PATH_TEMPLATE_CSS = Path(
    DIR_TEMPLATE_BASE, "css.template.txt")
PATH_TEMPLATE_JAVASCRIPT = Path(
    DIR_TEMPLATE_BASE, "javascript.template.txt")

# --------------------
# --REGEX
# --------------------
re_question_name_archive = re.compile(r"^Question name: (.+)\n", re.MULTILINE)
re_question_topic_archive = re.compile(r"^Topic name: (.+)\n", re.MULTILINE)
re_archive_censor = re.compile(
    r"(-=- QUESTION BODY -=-\n).*(\n-=- QUESTION BODY -=-)",
    re.MULTILINE | re.DOTALL)
re_topic_category_spliter = re.compile("[A-Z]+[a-z0-9 ]*")
re_question_elements_head = re.compile(
    (
        r"(?P<TOPIC_CATEGORY>.+)\n"
        r"(?P<TOPIC_NAME>.+)\n"
        r"(?:Topic repetition\n)?"
        r"(?P<QUESTION_NAME>.+?)(?: Problem of the day)?\n"
        r"(?:Next problem in.+\n)?"
        r"(?P<QUESTION_RATING>Easy|Medium|Hard)\n"
        r"\d+ users solved...+\n"
        r"(?P<QUESTION_BODY>(?:.*\n)+?)"
        r"Report a typo\n"
    ), re.MULTILINE)
re_question_elements_tail_normal = re.compile(
    (
        r"(?P<SAMPLE_IO>(?:.*\n)*?)"
        r"Write a program.*\n"
        r"(?:.*\n)+?"
        r"^1\n(?:^\d+\n)*"
        r"(?P<ANSWER_CODE>(?s:.*))"
    ), re.MULTILINE)
re_question_elements_tail_html_css = re.compile(
    (
        r"Write HTML and CSS code\n"
        r"(?:.*\n)+?"
        r"^HTML\n"
        r"(?:.*\n)*?"
        r"^1\n(?:^\d+\n)*"
        r"(?P<HTML>(?:.*?\n)*)"
        r"^CSS\n"
        r"(?:.*\n)*?"
        r"^1\n(?:^\d+\n)*"
        r"(?P<CSS>(?s:.*?\n)*)"
        r"^Checklist\n"
        r"(?P<CHECK_LIST>(?s:.*))"
    ), re.MULTILINE)
re_question_elements_extractor_normal = re.compile(
    re_question_elements_head.pattern
    + re_question_elements_tail_normal.pattern,
    re.MULTILINE
)
re_question_elements_extractor_html_css = re.compile(
    re_question_elements_head.pattern
    + re_question_elements_tail_html_css.pattern,
    re.MULTILINE
)
re_answer_code_python = re.compile(
    r"^\s*# -=- ANSWER CODE START -=-\n"
    r"(?P<ANSWER_CODE>.*?)"
    r"# -=- ANSWER CODE END -=-\n",
    re.MULTILINE | re.DOTALL)
re_answer_code_html = re.compile(
    r"(?P<HTML>.*?)"
    r"^<!-- -=- HTML END -=- -->\n",
    re.MULTILINE | re.DOTALL)
re_answer_code_css = re.compile(
    r"(?P<CSS>.*)"
    r"^.+-=- CSS END -=-.+\n",
    re.MULTILINE | re.DOTALL)
re_answer_code_javascript = re.compile(
    r"// -=- ANSWER CODE START -=-\n"
    r"(?P<ANSWER_CODE>.*?)"
    r"// -=- ANSWER CODE END -=-\n",
    re.MULTILINE | re.DOTALL)

# --------------------
# --MAPPINGS
# --------------------
dict_action_file_to_language_info: dict[Path, LanguageInfo] = {
    # Topic action file to programing language info mapping.
    PATH_QUESTIONS_CURRENT_PYTHON: LanguageInfo(
        language=Language.PYTHON,
        action_file=PATH_QUESTIONS_CURRENT_PYTHON,
        full_archive=PATH_ARCHIVE_FULL_PYTHON,
        censored_archive=PATH_ARCHIVE_CENSORED_PYTHON,
        file_suffix=".py",
        template_file=PATH_TEMPLATE_PYTHON,
        re_element_extractor=re_question_elements_extractor_normal,
        re_answer_extractor=re_answer_code_python,
    ),
    PATH_QUESTIONS_CURRENT_HTML: LanguageInfo(
        language=Language.HTML_CSS,
        action_file=PATH_QUESTIONS_CURRENT_HTML,
        full_archive=PATH_ARCHIVE_FULL_HTML_CSS,
        censored_archive=PATH_ARCHIVE_CENSORED_HTML_CSS,
        file_suffix=".html",
        template_file=PATH_TEMPLATE_HTML,
        re_element_extractor=re_question_elements_extractor_html_css,
        re_answer_extractor=re_answer_code_html,
    ),
    PATH_QUESTIONS_CURRENT_CSS: LanguageInfo(
        language=Language.HTML_CSS,
        action_file=PATH_QUESTIONS_CURRENT_CSS,
        full_archive=PATH_ARCHIVE_FULL_HTML_CSS,
        censored_archive=PATH_ARCHIVE_CENSORED_HTML_CSS,
        file_suffix=".css",
        template_file=PATH_TEMPLATE_CSS,
        re_element_extractor=re_question_elements_extractor_html_css,
        re_answer_extractor=re_answer_code_css,
    ),
    PATH_QUESTIONS_CURRENT_JAVASCRIPT: LanguageInfo(
        language=Language.JAVASCRIPT,
        action_file=PATH_QUESTIONS_CURRENT_JAVASCRIPT,
        full_archive=PATH_ARCHIVE_FULL_JAVASCRIPT,
        censored_archive=PATH_ARCHIVE_CENSORED_JAVASCRIPT,
        file_suffix=".js",
        template_file=PATH_TEMPLATE_JAVASCRIPT,
        re_element_extractor=re_question_elements_extractor_normal,
        re_answer_extractor=re_answer_code_javascript,
    ),
}


# --------------------
# --CLASSES
# --------------------


# --------------------
# --FUNCTIONS
# --------------------
# == Initialize script ==
def main():
    # perform helper initialization procedures.
    init_helper()
    while True:
        time_0 = time.time()
        # Wait for an action request.
        if no_action_request():
            time.sleep(0.05)
            continue
        try:
            # Process action request.
            action_file, action = process_action()
            # Execute requested action.
            exec_action(action_file, action)
        except JBAHelperNonFatalError as error:
            print("JBA helper error occurred:", *error.args)
            continue
        else:
            print("Executed: {} in: {:.3f}sec on: {}".format(
                action.name, time.time() - time_0, action_file.as_posix()))


def init_helper():
    os.chdir(PATH_JBA_ROOT)


# == Start action request handling ==
def exec_action(action_file: Path, action: Action):
    if action is Action.IMPORT_QUESTION:
        exec_import_question(action_file)
    elif action is Action.EXPORT_ANSWER:
        exec_export_answer(action_file)


def no_action_request() -> bool:
    return not PATH_ACTIONS_REQUEST.exists()


def process_action() -> tuple[Path, Action]:
    PATH_ACTIONS_REQUEST.rename(PATH_ACTIONS_REQUEST_READING)
    action_request_text = PATH_ACTIONS_REQUEST_READING.read_text().split(";")
    PATH_ACTIONS_REQUEST_READING.unlink(missing_ok=True)
    action_file = Path(action_request_text[0].strip()).resolve()
    requested_action = action_request_text[1].strip().upper()
    for action in Action:
        if action.name == requested_action:
            return action_file, action
    raise JBAHelperNonFatalError("Not a supported JBA helper action: "
                                 f"{requested_action}")


# == Get language info ==
def get_language_info(action_file: Path) -> LanguageInfo:
    # CSS quickfix.
    if action_file.as_posix() == PATH_QUESTIONS_CURRENT_CSS.as_posix():
        return dict_action_file_to_language_info[PATH_QUESTIONS_CURRENT_HTML]
    #
    try:
        return dict_action_file_to_language_info[action_file]
    except KeyError:
        raise JBAHelperNonFatalError(f"File path '{action_file.as_posix()}' "
                                     "doesn't match any of the question_text "
                                     "solution editing file paths.")


# == Handle topic question_text archiving ==
def get_archive_names_from_text(
        question_text: str) -> tuple[str | None, str | None]:
    name_match = re_question_name_archive.search(question_text)
    topic_match = re_question_topic_archive.search(question_text)
    name = (name_match.group(1) if name_match else None)
    topic_name = (topic_match.group(1) if name_match else None)
    return name, topic_name


def normalize_name(name: str | None) -> str | None:
    """Change all non ascii alphanumeric characters to underscores."""
    if name is None:
        return None
    valid_chars = string.ascii_letters + string.digits
    name = "".join((char if char in valid_chars else "_" for char in name))
    if name.strip("_") == "":
        return None
    return name


def build_archive_dir(
        base_archive_dir: Path, topic_name: str | None) -> Path:
    topic_name = normalize_name(topic_name)
    if topic_name is None:
        topic_name = "unknown_topic"
    archive_dir = Path(base_archive_dir, topic_name)
    archive_dir.mkdir(parents=True, exist_ok=True)
    return archive_dir


def build_archive_file_path(
        archive_dir: Path, file_name: str | None, language_info: LanguageInfo
) -> Path:
    file_name = normalize_name(file_name)
    if file_name is None:
        next_nameless_question_id = 1 + len(
            [file.name for file in archive_dir.glob("question_*")])
        file_name = (
            f"question_{next_nameless_question_id:0>4}"
        )
    return archive_dir.joinpath(file_name + language_info.file_suffix)


def censor_question_text(question_text: str) -> str:
    return re_archive_censor.sub(r"\1Question text censored.\2", question_text)


def archive_previous_question(language_info: LanguageInfo):
    file_to_archive = language_info.action_file
    full_archive = language_info.full_archive
    censored_archive = language_info.censored_archive
    # Read the questions text from the action file to deduce from it
    # the name and topic subdirectory for the question_text's archive file.
    question_text = file_to_archive.read_text()
    # Handle edge case where the file was manually emptied
    # or is otherwise empty.
    if question_text.strip() == "":
        return
    # extract question_text and topic names from the question_text's text.
    name, topic_name = get_archive_names_from_text(question_text)
    # construct full archive path from question_text and topic names.
    full_archive = build_archive_dir(full_archive, topic_name)
    censored_archive = build_archive_dir(censored_archive, topic_name)
    full_archive = build_archive_file_path(full_archive, name, language_info)
    censored_archive = build_archive_file_path(
        censored_archive, name, language_info)
    # Archive full question_text.
    full_archive.write_text(question_text)
    # Censor and archive censored question_text.
    question_text = censor_question_text(question_text)
    censored_archive.write_text(question_text)


# == Communicate with X selection clipboard ==
def get_primary_x_selection_text() -> str:
    x_selection_pipe = subprocess.Popen(
        ["xsel", "--primary", "--output"], stdout=subprocess.PIPE)
    question_text = x_selection_pipe.stdout.read()
    # exit_status = x_selection_pipe.wait()
    x_selection_pipe.stdout.close()
    return question_text.decode()


def set_clipboard_x_selection_text(text: str):
    x_selection_pipe = subprocess.Popen(
        ["xsel", "--clipboard", "--input"], stdin=subprocess.PIPE)
    x_selection_pipe.stdin.write(text.encode())
    x_selection_pipe.stdin.close()
    # exit_status = x_selection_pipe.wait()


# == Handle import question_text action ==
def format_topic_category(substitution_dict: dict[str, str]) -> dict[str, str]:
    topic_category = substitution_dict["TOPIC_CATEGORY"]
    topic_category = re_topic_category_spliter.findall(topic_category)
    topic_category = " -> ".join(topic_category)
    substitution_dict["TOPIC_CATEGORY"] = topic_category
    return substitution_dict


def get_sub_dict(language_info: LanguageInfo) -> dict[str, str]:
    # Read the new question_text's text from the X primary selection.
    question_text = get_primary_x_selection_text()
    # Get the language's regex element extractor and use it
    # to extract the question_text elements.
    re_element_extractor = language_info.re_element_extractor
    match = re_element_extractor.match(question_text)
    # Fail in case the X primary selection didn't contain
    # a question_text for import.
    if not match:
        raise JBAHelperNonFatalError("Can't get base question_text elements "
                                     "from primary X selection.")
    # Turn the regex match object into a dictionary
    # and fix the category string.
    sub_dict = match.groupdict()
    post_proc_sub_dict(language_info, sub_dict)
    return sub_dict


def post_proc_sub_dict_python(sub_dict: dict[str, str]):
    indent = " " * 4
    sub_dict["ANSWER_CODE"] = "\n".join(
        (indent + line for line in sub_dict["ANSWER_CODE"].splitlines()))


def post_proc_sub_dict(language_info: LanguageInfo, sub_dict: dict[str, str]):
    # Reformat the topic category because it's path elements get all
    # glued up during import.
    format_topic_category(sub_dict)
    # Remove lots of extra empty lines.
    for element in sub_dict:
        sub_dict[element] = sub_dict[element].strip()
    # Hard wrap question_text body lines to be no longer than
    # 72 characters as per PEP-8.
    sub_dict["QUESTION_BODY"] = hard_wrap_question_body(
        sub_dict["QUESTION_BODY"])
    if language_info.language is Language.PYTHON:
        post_proc_sub_dict_python(sub_dict)


def hard_wrap_question_body(question_body: str) -> str:
    question_lines_raw = question_body.splitlines()
    question_lines_raw.reverse()
    question_lines_wrapped = []
    while question_lines_raw:
        raw_line = question_lines_raw.pop()
        if len(raw_line) <= 72:
            wrapped_line = raw_line
        else:
            raw_line_words = raw_line.split()
            raw_line_words.reverse()
            wrapped_line_words = []
            line_len = 0
            word = raw_line_words.pop()
            while raw_line_words:
                if len(word) + 1 > 72:
                    wrapped_line_words.append("\n")
                    wrapped_line_words.append(word)
                    wrapped_line_words.append("\n")
                    line_len = 0
                    word = raw_line_words.pop()
                    continue
                line_len += len(word) + 1
                if line_len > 72:
                    wrapped_line_words.append("\n")
                    line_len = 0
                else:
                    wrapped_line_words.append(word)
                    word = raw_line_words.pop()
            wrapped_line_words.append(word)
            wrapped_line = " ".join(wrapped_line_words)
            wrapped_line.replace(" \n ", "\n")
        question_lines_wrapped.append(wrapped_line)
    return "\n".join(question_lines_wrapped)


def get_question_template_text(language_info: LanguageInfo) -> str:
    return language_info.template_file.read_text()


def css_quickfix(substitution_dict: dict[str, str]):
    # Paste imported css code into separate css file.
    language_info = dict_action_file_to_language_info[
        PATH_QUESTIONS_CURRENT_CSS]
    question_text = get_question_template_text(language_info)
    question_text = string.Template(
        question_text).safe_substitute(substitution_dict)
    language_info.action_file.write_text(question_text)
    # Add link to the above css file into the html answer file
    # if it did not already contain a link to a css stylesheet.
    language_info = dict_action_file_to_language_info[
        PATH_QUESTIONS_CURRENT_HTML]
    html_text = language_info.action_file.read_text()
    if '<link rel="stylesheet' not in html_text:
        html_text = ('<link rel="stylesheet" href="current.css">\n'
                     + html_text)
        # html_text = re.sub(
        #     r'^(?P<INDENT>\s*)</head',
        #     r'\g<INDENT>  <link rel="stylesheet" href="current.css">\n'
        #     r'\g<INDENT> </head',
        #     html_text,
        #     flags=re.MULTILINE
        # )
        language_info.action_file.write_text(html_text)


def exec_import_question(action_file: Path):
    language_info = get_language_info(action_file)
    # def exec_import_question_python(language_info: LanguageInfo):
    # Archive the previously edited question_text.
    archive_previous_question(language_info)
    # Extract the question_text's elements from the question_text's text:
    substitution_dict = get_sub_dict(language_info)
    # Get base question_text text from the answer template
    # for the given programing language.
    question_text = get_question_template_text(language_info)
    # Format the question_text's text.
    question_text = string.Template(
        question_text).safe_substitute(substitution_dict)
    # overwrite the old questions text in the current action file
    # with the formatted text of the new question_text.
    language_info.action_file.write_text(question_text)
    # Apply CSS quickfix (Because I don't see the time it would take
    # to properly add css import handling as justified).
    css_quickfix(substitution_dict)


# == Handle export answer action ==
def exec_export_answer(action_file: Path):
    language_info = get_language_info(action_file)
    if language_info.language == Language.PYTHON:
        export_answer_python(language_info)
    elif language_info.language == Language.HTML_CSS:
        export_answer_html_css(language_info)
    elif language_info.language == Language.JAVASCRIPT:
        export_answer_javascript(language_info)


def export_answer_javascript(language_info: LanguageInfo):
    # Get base answer text from the current solution file.
    answer_text = language_info.re_answer_extractor.search(
        language_info.action_file.read_text()).group("ANSWER_CODE")
    # Copy the answer code to the X clipboard selection.
    set_clipboard_x_selection_text(answer_text)


def export_answer_html_css(language_info: LanguageInfo):
    # Get base answer text from the current solution file.
    match = language_info.re_answer_extractor.match(
        language_info.action_file.read_text())
    html_text = match.group("HTML")
    # CSS quickfix
    html_text = re.sub(r'^\s*<link.+"current.css".*\n', '', html_text,
                       flags=re.MULTILINE)
    language_info = dict_action_file_to_language_info[
        PATH_QUESTIONS_CURRENT_CSS]
    match = language_info.re_answer_extractor.match(
        language_info.action_file.read_text())
    css_text = match.group("CSS")
    # Copy the answer code to the X clipboard selection.
    # For the time being I'm just gluing together the html and css code,
    # might do something better latter on.
    combined_text = html_text + "\n" + css_text
    set_clipboard_x_selection_text(combined_text)
    # set_clipboard_x_selection_text(css_text)
    # set_clipboard_x_selection_text(html_text)


def export_answer_python(language_info: LanguageInfo):
    # Get base answer text from the current solution file.
    answer_text = language_info.re_answer_extractor.search(
        language_info.action_file.read_text()).group("ANSWER_CODE")
    # Remove the extra indent added due to the solution being placed
    # inside a function in the solution file.
    indent = " " * 4
    answer_lines = answer_text.splitlines()
    for i in range(len(answer_lines)):
        answer_lines[i] = answer_lines[i].removeprefix(indent)
    answer_text = "\n".join(answer_lines)
    # Copy the unindented answer code to the X clipboard selection.
    set_clipboard_x_selection_text(answer_text)


# --------------------
# --PROGRAM CODE
# --------------------
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit("0: Normal exit by Interrupt.")

# --------------------
# --UNUSED
# --------------------

# === unused start: arg parse code ===

# I initially planned to call an instance of this script
# for each action invocation but then decided to start the script
# for persistent running and communicate with it via a temp file or a pipe.

# def main():
#     # Set up argparse.
#     parser = init_parser()
#     # Get invocation info from argparse.
#     action_file, action = parse_args(parser)


# def init_parser() -> argparse.ArgumentParser:
#     parser = argparse.ArgumentParser(description=__doc__)
#     parser.add_argument(
#         "--file", required=True,
#         help="The path to the source/target file for the required action",
#     )
#     parser.add_argument(
#         "--action", required=True, choices=ACTION_CHOICES,
#         help="The required action.",
#     )
#     return parser


# def parse_args(parser: argparse.ArgumentParser) -> tuple[str, str]:
#     args = parser.parse_args()
#     return args.file, args.action


# === unused end: arg parse code ===

# === unused start: primary modes ===
# def execute_topic_mode(action_file: str, action: str):
#     # Use the file path to deduce the question_text's programing language.
#     language = get_language(action_file)
#     # Execute the selected action:
#     if action == ACTION_ANSWER_EXPORT:
#         pass
#     if action == ACTION_QUESTION_IMPORT:
#         execute_question_import(action_file, language)
#     else:
#         raise ValueError(f"Unsupported action '{action}'")


# def get_primary_execution_mode(action: str) -> str:
#     if action in PRIMARY_MODE_QUESTION_ACTIONS:
#         return PRIMARY_MODE_TOPIC
#     elif action in PRIMARY_MODE_PROJECT_ACTIONS:
#         return PRIMARY_MODE_PROJECT
#     else:
#         raise ValueError(f"Requested action '{action}' doesn't match "
#                          "any primary execution mode.")
#


# === unused end: primary modes ===

# === unused start: misc ===
# def get_question_archive_base_dir(language: str) -> str:
#     if language == LANGUAGE_PYTHON:
#         return PATH_ARCHIVE_FULL_PYTHON
#     else:
#         raise ValueError(f"Language '{language}' doesn't have "
#                          "a question_text archive directory.")


# def exec_import_question(action_file: Path):
#     language_info = get_language_info(action_file)
#     if language_info.language is Language.PYTHON:
#         exec_import_question_python(language_info)


# === unused end: misc ===
