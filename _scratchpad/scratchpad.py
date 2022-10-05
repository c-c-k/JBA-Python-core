# # !/usr/bin/env python3.10
# # -*- coding: utf-8 -*-
# 
# """Scratch pad for Jet Brains Academy topic questions.
# 
# Properly formatting and saving the solutions for the topic practice
# questions
# feels like a waste of time, so instead I decided to use this script for
# copying and pasting and editing the script and then copying the solution to
# solutions_dump.
# 

# Beautify both output and code
# Medium
# 10759 users solved this problem. Latest completion was about 3 hours ago.
# 
# The output should be user-friendly, but the code part is also important.
# Well-structured and readable code is very important for being a good
# programmer. Now it's up to you to decide, which formatting method to
# choose.
# 
# Imagine you need to compose a dynamic URL for every certain user with
# user-specific details. Suppose, you want to send different URLs for every
# user, depending on their name and profession. The base would be something
# like
# 
# "http://example.com/*nickname*/desirable/*profession*/profile", where
# nickname and profession are prompts from a user and are dynamic.
# 
# Read the nickname and profession of the user from the input and print a
# user-specific URL. Don't bother about any rules of composing the URLs and
# just use raw input to accomplish the task.

# ---- code start ----
URL_FORMAT = "http://example.com/{NICKNAME}/desirable/{PROFESSION}/profile"
nickname = input()
profession = input()
print(URL_FORMAT.format(NICKNAME=nickname, PROFESSION=profession))
