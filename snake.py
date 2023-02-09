import curses
from copy import copy
from random import randint
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

curses.initscr()
window=curses.newwin(30,60,0,0)
window.keypad(True)
window.border(0)
window.timeout(10)
snake=[[15,13],[15,12],[15,11]]
food=[5,35]
view=KEY_DOWN
punti=0
window.addch(food[0], food[1], '0')
movement = 0

while True:
    window.addstr(0,18, 'Punteggio: '+str(punti)+' ')
    tasto=window.getch()
    if tasto!=-1:
        view=tasto
    Head=copy(snake[0])
    if view == KEY_DOWN:
        if movement != 1:
            Head[0]+=1
            movement=0
    elif view == KEY_UP:
        if movement !=0:
            Head[0]-=1
            movement=1
    elif view == KEY_RIGHT:
        if movement !=3:
            Head[1]+=1
            movement=2
    elif view == KEY_LEFT:
        if movement !=2:
            Head[1]-=1
            movement =3
    
    snake.insert(0,Head)
    if snake[0][0]==0 or snake[0][0]==29 or snake[0][1]==0 or snake[0][1]==59:
        break
    if snake[0] in snake[1:]:
        break
    if snake[0]==food:
        food=[]
        punti +=1
        while food == []:
            food=[randint(1,28),randint(1,58)]
            if food in snake:
                food=[]
        window.addch(food[0], food [1], '0')
    else:
        lastPart=snake.pop()
        window.addch(lastPart[0], lastPart[1], ' ')

    window.addch(snake[0][0], snake[0][1], 'o')
curses.endwin()
print("\n HAI PERSO! Punteggio finale: "+str(punti))