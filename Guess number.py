# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:25:07 2020

@author: Marek
"""
import random

def shots():
    
    while True:
        try:
            num = int(input('How many shots?\n'))
            break
        except:
            print('Not a number!')
    return num        

def enter_num():

    while True:
        try:
            choice = int(input('What number in range from 1 to 100 do you choose?\n'))
            break
        except:
            print('Not a number!')
    return choice

def correct_num():
    
    return(random.randrange(1, 101))


def game():
        
    ans_num = correct_num()
    shot_num = shots()
    winner = False
    
    while shot_num > 0:
        
        shot_num -= 1
        chosen_num = enter_num()
        if chosen_num == ans_num:
            print('You win!')
            winner = True
            break
        elif chosen_num < ans_num:
            print('Too low!')
        else:
            print('Too high!')
    if not winner:
       print('You loose!') 
game()        
        
        
        
        
        
        
        
        