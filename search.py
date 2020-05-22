#!/usr/local/bin/python
#coding: utf-8

import sys
import webbrowser
import os

def remove_symbols(word):
    temp_word = ""
    for letter in word:
        if letter.isalnum():
            temp_word += letter

    return temp_word

def isNumber(s) :
    for i in range(len(s)) :
        if s[i].isdigit() != True :
            return False
    return True

name = sys.argv
head, tail = os.path.split(name[1])
final=''
var = True
temp = tail.split()
if (len(temp)==1):
    temp = tail.split('.')

temp = [remove_symbols(word) for word in temp]

for word in temp:
    if isNumber(word):
        if temp.index(word) == 0:
            final += '+' + word
        elif 1900 <= int(word) <= 2100:
            final += '+' + word
            break
    else:
        final += '+' + word

link = 'https://www.imdb.com/find?q='
link = link + final

# print("Opening {} in browser.".format(link))

webbrowser.open(link, new=2)
