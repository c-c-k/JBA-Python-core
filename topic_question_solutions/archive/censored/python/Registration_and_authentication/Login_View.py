#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Backend -> Django -> Forms
Topic name: Registration and authentication
Question name: Login View
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
    from django.contrib.auth.views import LoginView
    
    
    class MyLoginView(LoginView):
        redirect_authenticated_user = False
        template_name = "customized_login.html"

        def __str__(self):
            return f"Template: {self.template_name}"
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
