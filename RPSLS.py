#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 21:07:41 2018

@author: joey
"""
import random

option = 1

while option != 0:
    
    option = input('play game 1/0')
    
    options = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    l = len(options)
    print(options)

    winlst = [-3,-2,1,5,7,9,11,14,18,20]

    human = input('Enter an option\t')
    hlow = human.lower()

    if hlow in options:
        num1 = options.index(hlow)
        
    rand = random.randint(0,4)        
    com = options[rand]
    total = (num1*l)-rand

    print('human: ' + hlow + '\tcomputer: ' + com)

    if num1 == rand:
        print('draw')
    else:
        if total in winlst:
            print('win')
        else:
            print('loss')    