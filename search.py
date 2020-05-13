#!/usr/local/bin/python
#coding: utf-8

import sys
import webbrowser
import os

name = sys.argv
head, tail = os.path.split(name[1])
final=''
var = True
temp = tail.split()
if (len(temp)==1):
    temp = tail.split('.')
i=0

def isNumber(s) :
    for i in range(len(s)) :
        if s[i].isdigit() != True :
            return False
    return True

while (var != False):
    if isNumber(temp[i]):
        temp[i] = int(temp[i])
    # if(temp[i].isnumeric()):
        if (i==0):
            final = final + '+' + str(temp[i])
        elif (1900 >= temp[i] <= 2100):
            final = final + '+' + str(temp[i])
        else:
            var = False
    elif(temp[i].isnumeric()==False):
        final = final + '+' + temp[i]
    i = i+1
print(final)


link = 'https://www.imdb.com/find?q='
link = link + final
webbrowser.open(link, new=2)
