#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Backend -> Django -> Launching server
Topic name: Processing requests
Question name: Urlpatterns
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
    from django.urls import path
    from django.views import View
    
    
    class CatView(View):
        description = "This is a cat view class"

        def __str__(self):
            return self.description

    
    class DogView(View):
        description = "This is a dog view class"

        def __str__(self):
            return self.description

    
    urlpatterns = [
        path('cat/', CatView.as_view()),
        path('dog/', DogView.as_view()),
    ]
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
