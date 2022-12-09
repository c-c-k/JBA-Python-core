#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Backend -> Django -> Forms
Topic name: Submitting data
Question name: Redirect or 404
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
    from django.shortcuts import redirect, Http404
    from django.views import View
    
    
    class TodoView(View):
        all_todos = []
    
        def delete(self, request, todo, *args, **kwargs):
            if todo in self.all_todos:
                self.all_todos.remove(todo)
            else:
                raise Http404
            return redirect("/")
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
