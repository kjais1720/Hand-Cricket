# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 20:38:00 2021

@author: kjais
"""

target=0

import random

play=''

def toss(t,p,n):
    e=[]
    if (p+n)%2==0:
        e=['odd','Odd','ODD']
    else:
        e=['even','Even','EVEN']
    if t in e:
        bb=input("You won the toss. What do you choose, Batting or Bowling?")
    else:
        print ("Computer won the toss and decided to ",end='')
        w=random.randrange(1,3,1)
        if w==1:
            print('Bat first')
            bb='bowl'
        elif w==2:
            print("Bowl first")
            bb='bat'
    return bb

def playerbat(p,c,play):
    score=0
    
    while(p!=c):
        score+=p
        p=int(input("score"))
        if p<1 or p>6:
            print("You can only score between 1 and 6")
            continue
        c=random.randrange(1,7,1)
        print("computer bowled ",c)
        if play=='chase':
            global target
            if score>target:
                print("You won")
                return play
            
    print("Bowldennn!!!! Your score is",score)
    if play=='bat':
        #global target
        target=score
        play='defend'
    elif play=='chase':
        if score>target:
            print("You won")
        elif score==target:
            print("match tied")
        else:
            print('You lost')
    return play
def compbat(p,c,play):
    score=0
    while(p!=c):
        score+=c
        p=int(input("Bowl"))
        if p<1 or p>6:
            print("You can only bowl between 1 and 6")
            continue
        c=random.randrange(1,7,1)
        print ("Computer hit",c)
        if play=='defend':
            global target
            if score>target:
                print("You lost. Computer scored",score)
                return play
            
    print("Bowldennnn!!! Computer's score is ",score)
    if play=='bowl':
        #global target
        target=score
        play='chase'
    elif play=='defend':    
        if score>target:
            print("You lost")
        elif score==target:
            print('match tied')
        else:
            print('You won')
    return play
print("Welcome")
print("Jaiswal Arts")
print('H A N D   C R I C K E T')
ch=input("Choose odd or even")
p=int(input('call'))
n=random.randrange(0,10,1)
play=toss(ch,p,n)
if play=='bat':
    p=int(input("score"))
    if p<1 or p>6:
            print("You can only score between 1 and 6")
            p=0
    c=random.randrange(1,7,1)
    print("computer bowled ",c)
    play=playerbat(p,c,play)
    
    p=int(input('bowl'))
    if p<1 or p>6:
            print("You can only bowl between 1 and 6")
            p=0
    c=random.randrange(1,7,1)
    print("computer hit ",c)
    if p!=c and p>target:
        print("You Won")
    else:
        compbat(p,c,play)
elif play=='bowl':
    p=int(input("Bowl"))
    if p<1 or p>=6:
            print("You can only bowl between 1 and 6")
            p=0
    c=random.randrange(1,7,1)
    print("computer hit ",c)
    play=compbat(p,c,play)
    p=int(input('score'))
    if p<1 or p>6:
            print("You can only score between 1 and 6")
            p=0
    c=random.randrange(1,7,1)
    print("computer bowled ",c)
    if p!=c and c>target:
        print("You lost😞😞")
    else:
        playerbat(p,c,play)