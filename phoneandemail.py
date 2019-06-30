#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:27:01 2019

@author: davidguo
"""
import pyperclip, re

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?
        (\s|-|\.)?
        \d{3}
        (\s|-|\.)
        \d{4}
        (\s*(ext|x|ext.)\s*\d{2,5})?
        )''', re.VERBOSE)




emailRegex = re.compile(r'''(
        ((\d|\w)+) #match anything
        @  #then match @
        ((\d|\w)+) #match anything
        (.com|.org|.net|.edu)#then match addresses
        )'''
        ,re.VERBOSE)


text = pyperclip.paste()

phone = phoneRegex.findall(text)

if len(phone) != 0:
    for i in range(len(phone)):
        for j in range(len(phone[i])):
            if j == 0:
                print(phone[i][j])

email = emailRegex.findall(text)

if len(email) != 0:
    for i in range(len(email)):
        for j in range(len(email[i])):
            if j == 0:
                print(email[i][j])


