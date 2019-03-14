#FALLING BLOCKS (SIDE GAME)
from turtle import Turtle, Screen
from random import randint
from colorsys import hsv_to_rgb
from time import sleep
import os, winsound as wav

def DEFINE():
    global player, bStamp, ANIMATE_TIMER, canDamage, animCount, playerHealth, BACHI, ST_HEALTH1, ST_HEALTH2, ST_HEALTH3, PHEALTH, FONT, t, COUNT_DIVISOR, sc, count, s, pStamp, movingBlocks, FALL_TIMER, CREATE_TIMER, CREATE_MAX, DEF_SPEED, SCORE_TIMER, DIED, StartStamp, RESTART_BOOLEAN, RESTART_TIMER, hasShot, ALL_MUSIC, shot, BOSS_TIMER, shotStamp, HEALTH, DAMAGE, bar, barStamp, CANSHOOT
    
    os.chdir(os.path.dirname(__file__))
    
    RESTART_BOOLEAN = True
    FONT = 'Fixedsys'
    
    t = Turtle('square')
    t.color('red')
    t.pu()
    t.ht()
    t.shapesize(2)
    
    shot = Turtle('triangle')
    shot.color('green')
    shot.pu()
    shot.ht()
    shot.shapesize(0.5)
    
    sc = Turtle()
    sc.ht()
    sc.pu()
    sc.goto(-300, 325)
    sc.color('yellow')
    
    bar = Turtle('square')
    bar.ht()
    bar.pu()
    
    
    ALL_MUSIC = ['MEGALOVANIA.wav', 'mus_dummybattle.wav', 'mus_spider.wav', 'mus_vsasgore.wav', 'mus_x_undyne.wav', 'mus_mettaton_ex.wav']
    count = 0
    HEALTH = 100
    DAMAGE = 3.3334
    CANSHOOT = True
    hasShot = 0
    DEF_SPEED = 6
    COUNT_DIVISOR = 70
    PHEALTH = 3
    canDamage = True
    
    s = Screen()
    s.tracer(False)
    s.screensize(400,400)
    s.bgcolor('black')
    s.listen()
    for x in ["HEART.gif", "oof.gif", "empty.gif", 'BACHI.gif', 'BACHI3.gif', 'BACHI2.gif']:
        s.addshape(x)
    
    playerHealth = Turtle("HEART.gif")
    playerHealth.pu()
    playerHealth.ht()
    
    BACHI = Turtle('BACHI.gif')
    
    player = Turtle('HEART.gif')
    player.color('blue')
    player.pu()
    player.ht()
    
    RANDINT = randint(0, 5)

    wav.PlaySound(ALL_MUSIC[RANDINT], wav.SND_LOOP | wav.SND_ASYNC)
    pStamp = None
    shotStamp = False
    barStamp = False
    movingBlocks = []
    FALL_TIMER = 10
    CREATE_TIMER = 400
    SCORE_TIMER = 1000
    RESTART_TIMER = 5000
    BOSS_TIMER = 10000 
    CREATE_MAX = CREATE_TIMER
    ANIMATE_TIMER = 300
    DIED = 0
    animCount = 0
    bStamp = BACHI.stamp()
    
    
    
    StartStamp = None
    Start()

def Move(x, y):
    global StartStamp
    H = 0
    t.goto(x, y)
    if t.xcor() < 100 and t.xcor() > -100 and t.ycor() < 52 and t.ycor() > -52:
        s.onscreenclick(None)
        
        while H < 266/360:
            t.goto(0, 0)
            H += 1.2/360 
            t.color(hsv_to_rgb(H, 1, 1))
            t.clearstamp(StartStamp)
            StartStamp = t.stamp()
            t.color('white')
            t.goto(0, -20)
            t.write("Start", False, align = 'center', font = (FONT, 25, 'bold'))
            sleep(0.00001)
        Setup()

def Start():
    global StartStamp
    
    t.goto(0, 0)
    t.shapesize(5, 10)
    StartStamp = t.stamp()
    t.color('white')
    t.goto(0, -20)
    t.write("Start", False, align = 'center', font = (FONT, 25, 'bold'))
    t.goto(700, 700)
    s.onscreenclick(Move)

def Setup():
    global pStamp, barStamp, ST_HEALTH1, ST_HEALTH2, ST_HEALTH3
    
    sc.write("Score: " + str(count), False, align = 'right', font = (FONT, 25, 'bold'))
    bar.color('red')
    bar.goto(25, 200)
    bar.shapesize(2, 25)
    bar.stamp()
    bar.color('green')
    barStamp = bar.stamp()
    
    BACHI.goto(400, 0)
    
    s.update()
    t.color('white')
    t.shapesize(12.2, 100)
    t.goto(-400, 0)
    t.stamp()
    
    playerHealth.goto(60, 150)
    ST_HEALTH1 = playerHealth.stamp()
    playerHealth.goto(playerHealth.xcor() - 50, playerHealth.ycor())
    ST_HEALTH2 = playerHealth.stamp()
    playerHealth.goto(playerHealth.xcor() - 50, playerHealth.ycor())
    ST_HEALTH3 = playerHealth.stamp()
    
    t.color('black')
    t.shapesize(.2, 100)
    
    for x in range(-3, 3):
        t.goto(-400, 25 + 50 * x)
        t.stamp()
        
    t.shapesize(2)
    t.color('red')
    s.onkey(Up, "Up")
    s.onkey(Down, "Down")
    s.onkey(Shoot, "z")
    RAND = (400, 0 + randint(-2, 2) * 50)
    t.goto(RAND)
    movingBlocks.append((RAND, t.stamp(), DEF_SPEED))
    player.goto(-400, 0)
    pStamp = player.stamp()
    s.update()
    s.ontimer(Fall, FALL_TIMER)
    s.ontimer(Boss, BOSS_TIMER)
    s.ontimer(Create, CREATE_TIMER)
    s.ontimer(Score, SCORE_TIMER)
    Animate()

def Animate():
    global animCount, bStamp
    temp = ['BACHI.gif', 'BACHI2.gif', 'BACHI3.gif', 'BACHI2.gif', 'BACHI.gif']
    BACHI.shape(temp[animCount])
    BACHI.goto(400, 0)
    BACHI.clearstamp(bStamp)
    bStamp = BACHI.stamp()
    animCount = (animCount + 1) % 5
    s.ontimer(Animate, ANIMATE_TIMER)

def LoseHealth():
    global ST_HEALTH1, ST_HEALTH2, ST_HEALTH3, PHEALTH, playerHealth, canDamage
    temp = [ST_HEALTH3, ST_HEALTH2, ST_HEALTH1]
    playerHealth.clearstamp(temp[PHEALTH])
    canDamage = False
    s.ontimer(Activate, 3000)
    BlinkOn()
    
def BlinkOn():
    global pStamp
    if not canDamage:
        player.clearstamp(pStamp)
        player.shape("empty.gif")
        pStamp = player.stamp()
        s.ontimer(BlinkOff, 300)

def BlinkOff():
    global pStamp
    player.clearstamp(pStamp)
    player.shape("HEART.gif")
    pStamp = player.stamp()
    s.ontimer(BlinkOn, 300)
    
def Activate():
    global canDamage
    canDamage = True    
   
def Shoot():
    global shotStamp, HEALTH, count, barStamp
    s.onkey(None, "z")
    
   # print('shot')
    
    if not shotStamp:
        shot.goto(player.pos())
        shotStamp = shot.stamp()
        
    shot.clearstamp(shotStamp)
    shot.goto(shot.xcor() + 10, shot.ycor())
    shotStamp = shot.stamp()
    
    for x in movingBlocks:
        if shot.distance(x[0]) < 25:
            shot.clearstamp(shotStamp)
            shotStamp = False
    
    if shot.xcor() > 500:
        HEALTH -= DAMAGE
        count += 7
        bar.clearstamp(barStamp)
        try:
            bar.shapesize(2, 25 - (100 - HEALTH) / 4)
        except:
            bar.shapesize(2, 1)
        bar.goto(bar.xcor() - 25/(10 / DAMAGE), bar.ycor())
        barStamp = bar.stamp()
        
        if HEALTH <= 0:
            WINMUSIC()
            WIN()
        
        shot.clearstamp(shotStamp)
        shotStamp = False
    
    if shotStamp:
        s.ontimer(Shoot, FALL_TIMER)
    else:
        s.onkey(Shoot, "z")
    
                
def Up():
    global pStamp
    s.onkey(None, "Up")
    if player.ycor() < 100:
        player.clearstamp(pStamp)
        player.goto(-400, player.ycor() + 50)
        pStamp = player.stamp()
        s.update()
    s.onkey(Up, "Up")
    
def Down():
    global pStamp
    s.onkey(None, "Down")
    if player.ycor() > -100:
        player.clearstamp(pStamp)
        player.goto(-400, player.ycor() - 50)
        pStamp = player.stamp()
        s.update()
        
    s.onkey(Down, "Down")

def die():
    global DIED
    DIED = 1   
    s.clear()
    s.onkey(None, "Down")
    s.onkey(None, "Up")       
    s.update()
    wav.PlaySound('mus_kingdescription.wav', wav.SND_LOOP | wav.SND_ASYNC)
    
def Fall():
    global PHEALTH, canDamage
    t.shape("oof.gif")
    if movingBlocks:
        for x in movingBlocks:
            if x[0][0] > -500:
                t.goto((x[0][0] - x[2], x[0][1]))
                t.clearstamp(x[1])
                movingBlocks.append((t.pos(), t.stamp(), DEF_SPEED))
                
                if t.distance(player.pos()) <= 15 and canDamage:
                    PHEALTH -= 1
                    LoseHealth()
                    if PHEALTH == 0:
                        die()
                else:
                    try:
                        movingBlocks.pop(movingBlocks.index(x))
                    except:
                        print("User must have restarted, aborting action...")
                 
            else:
                movingBlocks.pop(movingBlocks.index(x))
    t.shape("square")      
    if DIED != 1:
        if HEALTH > 0:
            s.ontimer(Fall, FALL_TIMER)
        else:
            WIN()
    else:
        REMOVE()
   
def Create():
    global CREATE_TIMER
    t.shape("oof.gif")
    RAND = (400, 0 + (randint(-2, 2) * 50))
    t.goto(RAND)
    movingBlocks.append((RAND, t.stamp(), DEF_SPEED))
    t.shape("square")
    if CANSHOOT:
        CREATE_TIMER = CREATE_MAX - count // 5
    if DIED != 1:
        if HEALTH > 0:
            s.ontimer(Create, CREATE_TIMER)
        else:
            WIN()
    else:
        REMOVE()
   
def Score():
    global count
    
    count += 1
    sc.clear()
    sc.write("Score: " + str(count), False, align = 'right', font = (FONT, 25, 'bold'))
    if DIED != 1:
        if HEALTH > 0:
            s.ontimer(Score, SCORE_TIMER)
        else:
            WIN()
    else:
        REMOVE()
        
def REMOVE():
    global RESTART_TIMER, bStamp, ANIMATE_TIMER, FALL_TIMER, CREATE_TIMER
    s.clear()
    ANIMATE_TIMER = 99999999
    FALL_TIMER = 999999999
    CREATE_TIMER = 9999999999
    player.goto(0,0)
    player.color('red')
    player.write(" YOU DIED ", False, align = 'center', font = (FONT, 50, 'bold'))
    player.goto(0, 50)
    player.write(" SCORE: " + str(count), False, align = 'center', font = (FONT, 25, 'bold'))
    s.ontimer(RESTART, RESTART_TIMER)
    s.ontimer(Animate, ANIMATE_TIMER)
    s.ontimer(Create, CREATE_TIMER)
    s.ontimer(Fall, FALL_TIMER)

def WINMUSIC():
    wav.PlaySound('Basshunter - DotA (HQ).wav', wav.SND_LOOP | wav.SND_ASYNC)

def WIN():
    global RESTART_TIMER
    s.clear()
    player.goto(0,0)
    player.color('red')
    player.write(" YOU WON ", False, align = 'center', font = (FONT, 50, 'bold'))
    player.goto(0, 50)
    player.write(" SCORE: " + str(count), False, align = 'center', font = (FONT, 25, 'bold'))
    
    
def RESTART():
    global RESTART_BOOLEAN
    #MAY NEED TO REMOVE RESTART_BOOLEAN
    if RESTART_BOOLEAN == True:
        RESTART_BOOLEAN = False
    s.onscreenclick(CONT)
        
    t.goto(0, -30)
    t.write("Restart?", False, align = 'center', font = (FONT, 25, 'bold'))
    t.goto(700, 700)
        
        
    
def CONT(x, y):
    #s.onscreenclick(None)
    if x < 70 and x > -130 and y < 22 and y > -82:
        s.reset()
        s.clearscreen()
        wav.PlaySound(None, wav.SND_LOOP | wav.SND_ASYNC)
        DEFINE()
    
def Boss():
    global CREATE_TIMER, CANSHOOT, RANDSELECT
    CANSHOOT = False
    CREATE_TIMER = 99999999
    RANDSELECT = randint(-2, 2)
    if DIED != 1:
        if HEALTH > 0:
            s.ontimer(Create, CREATE_TIMER)
            s.ontimer(BossAttack1, 1)
        else:
            WIN()
    else:
        REMOVE()

def BossAttack1():
    global CANSHOOT, CREATE_TIMER, hasShot, RANDSELECT
    #print('spawning')
    #s.ontimer(Boss, 40)
    if not movingBlocks and hasShot == 0: 
        hasShot = 1
        print('movingLbocks done')
        for x in range(-2, 3):
            t.goto(400, 50 * x)
            if x != RANDSELECT:
                movingBlocks.append((t.pos(), t.stamp(), DEF_SPEED))
            print(movingBlocks)
       # Fall()
   
    if not movingBlocks:
        print('done')
        hasShot = 0
        CANSHOOT = True 
        Create()       
        if DIED != 1:
            if HEALTH > 0:
                s.ontimer(Boss, BOSS_TIMER)
            else:
                WIN()
        else:
            REMOVE()
    else:        
        s.ontimer(Boss, 40)    

DEFINE()



s.mainloop()