#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Backend -> Django -> ORM
Topic name: Django ORM
Question name: Coach Model
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
    from django.db import models
    
    
    class Team(models.Model):
        name = models.CharField(max_length=64)
    
        class Meta:
            app_label = 'tournament'
    
    
    class Coach(models.Model):
        name = models.CharField(max_length=48)
        experience = models.IntegerField()
        team = models.ForeignKey(
            Team, on_delete=models.CASCADE, related_name='coach_team')
    
        class Meta:
            app_label = 'tournament'
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
