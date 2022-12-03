#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question_text solution.

Topic category: Computer science -> Backend -> Django -> ORM
Topic name: Object modification with ORM
Question name: Create Object in the Database
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    from django.db import models
    class Task(models.Model):
        description = models.CharField(max_length=256)
        is_done = models.BooleanField()
        priority = models.IntegerField()
    # -=- ANSWER CODE START -=-
    task = Task(description="walk to the grocery", priority=5, is_done=False)
    task.save()
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
