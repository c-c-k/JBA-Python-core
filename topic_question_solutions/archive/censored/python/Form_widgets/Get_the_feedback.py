#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Backend -> Django -> Forms
Topic name: Form widgets
Question name: Get the feedback
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    # -=- ANSWER CODE START -=-
    from django import forms
    
    FREQ = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]
    
    class CommentForm(forms.Form):
        name = forms.CharField()
        comment = forms.CharField(widget=forms.Textarea())
        email = forms.EmailField(widget=forms.EmailInput())
        frequency = forms.ChoiceField(
            widget=forms.RadioSelect(),
            label="How often should I send notifications?",
            choices=FREQ,
            required=False
        )
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

TEST

Sample Output 1:
"""
