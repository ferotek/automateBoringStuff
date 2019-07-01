#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 17:53:29 2019

@author: davidguo
"""

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')


if sys.argv[1] == "save" and len(sys.argv) == 3:
    keyword = sys.argv[2] 
    text = pyperclip.paste()
    mcbShelf[keyword] = text
    
    
elif sys.argv[1] == "list" and len(sys.argv) == 3 :
    copyText = ""
    for i in range(0, len(mcbShelf.keys())):
        copyText += list(mcbShelf.keys())[i]
    pyperclip.copy(copyText)
elif len(sys.argv) == 2:
    pyperclip.copy(mcbShelf[sys.argv[1]])
    
    

   # TODO: Save clipboard content.

   # TODO: List keywords and load content.

#mcbShelf.close()