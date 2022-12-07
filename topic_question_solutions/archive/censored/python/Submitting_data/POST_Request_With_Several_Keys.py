#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Backend -> Django -> Forms
Topic name: Submitting data
Question name: POST Request With Several Keys
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    # -=- ANSWER CODE START -=-
    from django.shortcuts import redirect
    from django.views import View
    
    
    class TodoView(View):
        all_todos = []
    
        def post(self, request, *args, **kwargs):
            task = request.POST["todo"]
            important = request.POST["important"]
            todo_list = self.all_todos
            if task and task not in todo_list:
                if important:
                    todo_list.insert(0, task)
                else:
                    todo_list.append(task)
            return redirect("/")
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
