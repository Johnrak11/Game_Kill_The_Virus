# ================================improt=========================================
from tkinter import *
from random import randrange
import winsound
from tkinter.font import BOLD 
# ==================================CONSTAN=======================================
WINDOWS_WIDTH = 1200
WINDOWS_HIGHT = 700
FONT_FAMILY = 'Arail'
HERO = 1
WALL = 7
VIRUS = 2
DENGER_VIRUS0 = 10
DENGER_VIRUS1 = 11
DENGER_VIRUS2 = 12
DENGER_VIRUS3 = 13
DENGER_VIRUS4 = 14
DENGER_VIRUS5 = 15
DENGER_VIRUS6 = 16
DOOR = 8
MASK = 9
ALCOHOL = 6
PARADUL = 5
# ==================================variable======================================
level = []
#-----------grid element---------------
#-------------reload-----
isReload = [False, False, False]
# -------------nextlevel--------
isNext=[False, False, False]
#------------hero--------------
isHeroLeft = False
#-----------rules game-------------
health = 3
maskSum = 0
alcoholSum = 0
virusSum = 0
scoreSum = 0
totalCoinSave= 0
#----------------enemyMove----------
isVirusMove=[True,True,True,True,True,True,True]
virusProcess=True
#unlock
totalEnemy = 0
isLock = True
isWin = True
isClick= True
# ==================================FURNCTION======================================
#----------------start-------------

def startGame(event):
    draw.delete('all')
    sound('startGame')
    draw.create_image(600, 350, image = bgStart)
    draw.create_image(600, 350, image = btnStart, tags = 'start')
    draw.create_text(600, 348, text = 'START', fill = 'white', font = (FONT_FAMILY, 22, BOLD), tags = 'start')
    draw.create_image(600, 450, image = btnStart, tags = 'instrution')
    draw.create_text(600, 448, text = 'INSTRUTION', fill = 'white', font = (FONT_FAMILY, 18, BOLD), tags = 'instrutions')

#-------------------menu--------------

def menuGame(event):
    sound('chooesLevel')
    draw.delete('all')
    draw.create_image(600, 350, image = bgChoose)
    # -------------level----------
    draw.create_image(350, 350, image = btnlevel,tags='level')
    draw.create_text(350, 350, text = 'Level 1', fill = 'white', font = (FONT_FAMILY, 20, BOLD), tags = 'level')
    draw.create_image(600, 350, image = btnlevel, tags = 'level2')
    draw.create_text(600, 350, text = 'Level 2', fill = 'white', font = (FONT_FAMILY, 20, BOLD), tags = 'level2')
    draw.create_image(850, 350, image = btnlevel, tags = 'level3')
    draw.create_text(850, 350, text = 'Level 3', fill = 'white', font = (FONT_FAMILY, 20, BOLD), tags = 'level3')
    draw.create_image(1100, 640 ,image = btnlevel, tags = 'Charater') 
    draw.create_text(1100, 638, text = 'Charater', fill = 'white', font = (FONT_FAMILY,15,BOLD), tags = 'Charater')
    #-------------back-----------
    draw.create_image(50, 50, image = btnBack, tags = 'back1')

#-----------------buy Hero----------------
#read------file
def readCoin():
    global totalCoinSave
    f = open("files/coins.txt", "r")
    totalCoinSave = int(f.read())
    f.close()

#write------file
def writeCoin():  
    global totalCoinSave,scoreSum
    w = open("files/coins.txt", "w")
    w.write(str(totalCoinSave))
    w.close()

#chooes------hero
def chooesHero(event):
    draw.delete('all')
    draw.create_image(600, 350, image = bgChoose)
    draw.create_image(50, 50, image = btnBack, tags = 'back3')
    draw.create_image(600, 50, image = btnlevel)
    draw.create_image(550, 50, image = totalCoin)
    draw.create_text(610, 50, text =totalCoinSave, fill = 'white', font = (FONT_FAMILY, 20, BOLD))
    # --------------charater----2
    draw.create_image(900, 340, image = instrutionWins,tags = 'Hero3')
    draw.create_image(900, 340, image = amongHero,tags = 'Hero3')
    draw.create_text(900, 400, text ='1000', fill = 'white', font = (FONT_FAMILY, 20, BOLD))
    # ---------------charater--1
    draw.create_image(300, 340, image = instrutionWins,tags = 'Hero2')
    draw.create_image(300, 330, image = jeryHero,tags = 'Hero2')
    draw.create_text(300, 400, text ='500', fill = 'white', font = (FONT_FAMILY, 20, BOLD))
#chooes-----codition
def chooesHeroCheck(heroChange):
    global heroRight,heroleft,totalCoinSave
    if heroChange == 'charater2' and totalCoinSave >= 500:
        heroleft = PhotoImage(file = 'image/chariter3.png')
        heroRight = PhotoImage(file = 'image/chariter4.png')
        totalCoinSave-= 500
        writeCoin()
    if heroChange == 'charater3' and totalCoinSave >= 1000:
        heroleft = PhotoImage(file = 'image/chariter2.png')
        heroRight = PhotoImage(file = 'image/charier1.png')
        totalCoinSave-= 1000
        writeCoin()
#chooes-----hero1
def charaterOne(event):
    chooesHeroCheck('charater2')
    menuGame(event)
#chooes-----hero2
def charaterTwo(event):
    chooesHeroCheck('charater3')
    menuGame(event)

#-----------------instrution----------------

def instrution(event):
    draw.delete('all')
    sound('click')
    #----------------bg----------------------
    draw.create_image(600, 350, image = bgRule)
    #---------------instrution----------
    draw.create_image(300, 350, image = instrution1)
    # draw.create_image(600, 350, image = instrut)
    draw.create_image(900, 350, image = instrution2)
    #---------------back------------
    draw.create_image(50, 50, image = btnBack, tags = 'back2')

#------------------------draw grid--------------------------
def displayGrid(grid):
    global isHeroLeft, virusEnemy
    draw.delete('all')
    navBar()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # wall
            if grid[row][col] == WALL: 
                draw.create_image((col*41) + 70, (row*41) + 70, image = wallpic)
            # door
            elif grid[row][col] == DOOR and isLock:
                draw.create_image((col*41) + 70, (row*41) + 70, image = wallpic)
                draw.create_image((col*41) + 70, (row*41) + 70, image = lockDoor)
            elif grid[row][col] == DOOR and not isLock:
                draw.create_image((col*41) + 70, (row*41) + 70, image = wallpic)
                draw.create_image((col*41) + 70, (row*41) + 70, image = unlockDoor)
            # isHeroLeft
            elif grid[row][col] == HERO and isHeroLeft:
                draw.create_image((col*41) + 70, (row*41) + 70, image = floorPic)
                draw.create_image((col*41) + 70, (row*41) + 70, image = heroleft)
            #isHeroLeft
            elif grid[row][col] == HERO and not isHeroLeft:
                draw.create_image((col*41) + 70, (row*41) + 70, image = floorPic)
                draw.create_image((col*41) + 70, (row*41) + 70, image = heroRight)
            #virus
            elif grid[row][col] == VIRUS :
                draw.create_image((col*41) + 70, (row*41) + 70, image = floorPic)
                draw.create_image((col*41) + 70,(row*41) + 70, image = virusHero)
            #mask
            elif grid[row][col] == MASK :
                draw.create_image((col*41) + 70, (row*41) + 70, image = floorPic)
                draw.create_image((col*41) + 70, (row*41) + 70, image = maskpic)
            # ALCOHOL
            elif grid[row][col] == ALCOHOL :
                draw.create_image((col*41) + 70, (row*41) + 70, image = floorPic)
                draw.create_image((col*41) + 70, (row*41) + 70, image = alcoholpic)
            # PARADUL
            elif grid[row][col] == PARADUL:
                draw.create_image((col*41) + 70, (row*41) + 70, image = floorPic)
                draw.create_image((col*41) + 70, (row*41) + 70, image = paradolpic)
            #denger virus
            elif (grid[row][col] == DENGER_VIRUS0) or (grid[row][col] == DENGER_VIRUS1) or (grid[row][col] == DENGER_VIRUS2) or (grid[row][col] == DENGER_VIRUS3) or (grid[row][col] == DENGER_VIRUS4) or (grid[row][col] == DENGER_VIRUS5) or (grid[row][col] == DENGER_VIRUS6):
                draw.create_image((col*41) + 70, (row*41) + 70, image = floorPic)
                draw.create_image((col*41) + 70, (row*41) + 70, image = virusDenger)
            # Floor
            elif grid[row][col] == 0:
                draw.create_image((col*41) + 70, (row*41) + 70, image = floorPic)
    endGameContain()

# ------------------navbar----------

def navBar():
    draw.create_image(600, 350, image = bglevel1)
    healthHero()
    navbarContainer()

#------------------------------health--------------------

def healthHero():
    draw.create_image(70, 25, image =hearlthpic)
    if health == 2:
        draw.create_image(168, 25, image = meduimHealth)
    elif health == 1:
        draw.create_image(168, 25, image = lowHealth)
    else:
        draw.create_image(168, 25, image = fulHealth)

def navbarContainer():
    # ---------mask--------------
    draw.create_image(330,25,image = navMask)
    draw.create_text(345,25,text = maskSum, font = (FONT_FAMILY, 15, BOLD), fill = 'white')
    # ----------alcohol-----------
    draw.create_image(450,25,image = navAlkohol)
    draw.create_text(465,25,text = alcoholSum, font = (FONT_FAMILY, 15, BOLD), fill = 'white')
    # ------------setscore-------------
    draw.create_image(685,25,image = navCoins)
    draw.create_text(700,25,text = scoreSum, font = (FONT_FAMILY, 15, BOLD), fill = 'white')
    # ----------------numberOfKillEnemy------------
    draw.create_image(570, 25, image = navEnemy)
    draw.create_text(585, 25, text = virusSum, font = (FONT_FAMILY, 15, BOLD), fill = 'white')
    # -----------------------------back--------
    draw.create_image(1140,27, image = gameBack, tags='stopGame')

# ---------------win and loes----------------------

def endGameContain():
    global isWin,isClick,virusProcess,totalCoinSave, scoreSum
    if health == 0:
        virusProcess = False
        totalCoinSave += scoreSum
        gameLost()
    elif not isWin:
        isWin = True
        isClick = False
        totalCoinSave += scoreSum
        gameWin()

# ---------------loes------------

def gameLost():
    draw.delete('all')
    sound('loss')
    draw.create_image(600, 350, image = lostBackground)
    draw.create_image(600, 200, image = lost, tags = 'again')
    draw.create_image(550, 400, image = reloads, tags = 'reload')
    draw.create_image(650, 400, image = backHome, tags = 'backHome')
    draw.create_image(1100, 640 ,image = exits, tags = 'exit')
    draw.create_text(1100, 638, text = 'Exit', fill = 'white', font = (FONT_FAMILY, 15, BOLD), tags = 'exit')
    writeCoin()

# ---------------loes------------

def gameWin():
    draw.delete('all')
    sound('win')
    draw.create_image(600, 350, image = winBackground)
    draw.create_image(600, 340, image = instrutionWins)
    draw.create_image(570, 340 ,image = totalCoin)
    draw.create_text(620, 340, text = scoreSum, fill = 'white', font = (FONT_FAMILY, 20, BOLD))
    draw.create_image(570, 390 ,image = totalKill)
    draw.create_text(620, 390, text = virusSum, fill = 'white', font = (FONT_FAMILY, 20, BOLD))
    draw.create_image(600, 150, image = win)
    draw.create_image(470, 540, image = reloads, tags = 'reload')
    draw.create_image(600, 540, image = backHome, tags = 'backHome')
    draw.create_image(730, 540, image = btnNext, tags = 'next')
    draw.create_image(1100, 640 ,image = exits, tags = 'exit') 
    draw.create_text(1100, 638, text = 'Exit', fill = 'white', font = (FONT_FAMILY,15,BOLD), tags = 'exit')
    playerStar()
    writeCoin()

# ------------star------------------

def playerStar():
    if health == 1:
        draw.create_image(600, 275, image = star1)
    elif health == 2:
        draw.create_image(600, 275, image = star2)
    else:
        draw.create_image(600, 275, image = star3)

#-----------------Enemy-----------------------------------------
# --positionEnemy-------

def positionEnemy(grid, virusData):
    pos = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
           if grid[row][col] == virusData:
                pos.append(row)
                pos.append(col)
    return pos

# ---------Enemy Conatiner-----------

def enemyContainer():
    global isVirusMove, level
    # ------virus1------
    posVirus1= positionEnemy(level,DENGER_VIRUS0)
    if posVirus1 != [] :
        dengerVirus1=enemyMoveUp(0,posVirus1[0],posVirus1[1],DENGER_VIRUS0)
    # ------virus2------
    posVirus2= positionEnemy(level, DENGER_VIRUS1)
    if posVirus2 != []:
        dengerVirus2=enemyMoveUp(1, posVirus2[0], posVirus2[1], DENGER_VIRUS1)
    # ------virus3------
    posVirus3= positionEnemy(level, DENGER_VIRUS2)
    if posVirus3 != []:
        dengerVirus3=enemyMoveUp(2, posVirus3[0], posVirus3[1], DENGER_VIRUS2)
    # ------virus4------
    posVirus4= positionEnemy(level, DENGER_VIRUS3)
    if posVirus4 != []:
        dengerVirus4 = enemyMoveUp(3, posVirus4[0], posVirus4[1], DENGER_VIRUS3)
    # ------virus5------
    posVirus5= positionEnemy(level, DENGER_VIRUS4)
    if posVirus5 != []:
        dengerVirus5 = enemyMoveLeft(4, posVirus5[0], posVirus5[1], DENGER_VIRUS4)
    # ------virus6------
    posVirus6= positionEnemy(level, DENGER_VIRUS5)
    if posVirus6 != []:
        dengerVirus6 = enemyMoveLeft(5, posVirus6[0], posVirus6[1], DENGER_VIRUS5)
    # ------virus7------
    posVirus7= positionEnemy(level, DENGER_VIRUS6)
    if posVirus7 != []:
        dengerVirus7 = enemyMoveLeft(6, posVirus7[0], posVirus7[1], DENGER_VIRUS6)
    # -----------process----loading--------
    if virusProcess:
        draw.after(150, enemyContainer)

# ------------virusCondition or virus rules--------------

def virusCondition():
    global health, isVirusMove, maskSum, alcoholSum, scoreSum, virusSum
    if maskSum == 0 and alcoholSum == 0:
        health -= 1
        sound('lowhealth')
    elif maskSum > 0 and alcoholSum == 0:
        health += -1
        maskSum += -1
        sound('lowhealth')
    elif maskSum == 0 and alcoholSum > 0:
        health += -1
        alcoholSum += -1
        sound('lowhealth')
    elif maskSum > 0 and alcoholSum > 0:
        scoreSum += randrange(10, 20)
        alcoholSum += -1
        maskSum += -1
        virusSum += 1
        sound('coin')

# --------------virusMove-------------------------

def virusMove(row, col, moveRow, moveCol, charaterVirus, value, isFound):
    global level, isVirusMove
    if level[moveRow][moveCol] != WALL and level[moveRow][moveCol] != HERO:
        level[moveRow][moveCol] = charaterVirus
        level[row][col] = 0
    elif level[moveRow][moveCol] == HERO:
        level[moveRow][moveCol] = HERO
        level[row][col] = 0
        virusCondition()
    else:
        isVirusMove[value]=isFound

# -----------------virus Move Left and Right--------------

def enemyMoveLeft(value, row, col, charaterVirus):
    global level, isVirusMove
    if isVirusMove[value]:
        virusMove(row, col, row, col - 1, charaterVirus, value, False)
    elif not isVirusMove[value]:
        virusMove(row, col, row, col + 1, charaterVirus, value, True)
    displayGrid(level)

# -----------------virus Move Up and Down--------------

def enemyMoveUp(value, row, col, charaterVirus):
    global level, isVirusMove
    if isVirusMove[value]:
        virusMove(row, col, row-1, col, charaterVirus, value, False)
    elif not isVirusMove[value]:
        virusMove(row, col, row+1, col, charaterVirus, value, True)
    displayGrid(level)

# -----------------Rules---------------------------------------------
# ---condition
def conditionGamePlay(row, col):
    global health, maskSum, alcoholSum, scoreSum, virusSum,isWin
    if (level[row][col] == VIRUS and maskSum == 0 and alcoholSum == 0) or (level[row][col] == DENGER_VIRUS0 and maskSum == 0 and alcoholSum == 0) or (level[row][col] == DENGER_VIRUS1 and maskSum == 0 and alcoholSum == 0) or (level[row][col] == DENGER_VIRUS2 and maskSum == 0 and alcoholSum == 0) or (level[row][col] == DENGER_VIRUS3 and maskSum == 0 and alcoholSum == 0) or (level[row][col] == DENGER_VIRUS4 and maskSum == 0 and alcoholSum == 0) or (level[row][col] == DENGER_VIRUS5 and maskSum == 0 and alcoholSum == 0) or (level[row][col] == DENGER_VIRUS6 and maskSum == 0 and alcoholSum == 0):
        health += -1
        sound('lowhealth')
    elif (level[row][col] == VIRUS and maskSum > 0 and alcoholSum == 0) or (level[row][col] == DENGER_VIRUS0 and maskSum > 0 and alcoholSum == 0) or (level[row][col] == DENGER_VIRUS1 and maskSum > 0 and alcoholSum == 0) or (level[row][col] == DENGER_VIRUS2 and maskSum > 0 and alcoholSum == 0) or (level[row][col] == DENGER_VIRUS3 and maskSum > 0 and alcoholSum == 0) or (level[row][col] == DENGER_VIRUS4 and maskSum > 0 and alcoholSum == 0) or (level[row][col] == DENGER_VIRUS5 and maskSum > 0 and alcoholSum == 0) or (level[row][col] == DENGER_VIRUS6 and maskSum > 0 and alcoholSum == 0):
        health += -1
        maskSum += -1
        sound('lowhealth')
    elif (level[row][col] == VIRUS and maskSum == 0 and alcoholSum > 0) or (level[row][col] == DENGER_VIRUS0 and maskSum == 0 and alcoholSum > 0) or (level[row][col] == DENGER_VIRUS1 and maskSum == 0 and alcoholSum > 0) or (level[row][col] == DENGER_VIRUS2 and maskSum == 0 and alcoholSum > 0) or (level[row][col] == DENGER_VIRUS3 and maskSum == 0 and alcoholSum > 0) or (level[row][col] == DENGER_VIRUS4 and maskSum == 0 and alcoholSum > 0) or (level[row][col] == DENGER_VIRUS5 and maskSum == 0 and alcoholSum > 0) or (level[row][col] == DENGER_VIRUS6 and maskSum == 0 and alcoholSum > 0):
        health += -1
        alcoholSum += -1
        sound('lowhealth')
    elif (level[row][col] == VIRUS and maskSum > 0 and alcoholSum > 0) or (level[row][col] == DENGER_VIRUS0 and maskSum > 0 and alcoholSum > 0) or (level[row][col] == DENGER_VIRUS1 and maskSum > 0 and alcoholSum > 0) or (level[row][col] == DENGER_VIRUS2 and maskSum > 0 and alcoholSum > 0) or (level[row][col] == DENGER_VIRUS3 and maskSum > 0 and alcoholSum > 0) or (level[row][col] == DENGER_VIRUS4 and maskSum > 0 and alcoholSum > 0) or (level[row][col] == DENGER_VIRUS5 and maskSum > 0 and alcoholSum > 0) or (level[row][col] == DENGER_VIRUS6 and maskSum > 0 and alcoholSum > 0):
        scoreSum += randrange(10, 20)
        alcoholSum += -1
        maskSum += -1
        virusSum += 1
        sound('coin')
    elif level[row][col] == MASK:
        maskSum += 1
        sound('colect')
    elif level[row][col] == ALCOHOL:
        alcoholSum += 1
        sound('colect')
    elif level[row][col] == PARADUL and health < 3:
        health += 1
        sound('upHealth')
    elif level[row][col] == DOOR and not isLock:
        isWin = False
        
#-----destroy-------

def WinDestroy(event):
    root.destroy()

#------Reload-menu--------

def backMenu(event):
    resetItem()
    menuGame(event)

# -------resetItem--------

def resetItem():
    global health, maskSum, alcoholSum, isLock, virusSum, scoreSum
    isLock = True
    health = 3
    maskSum = 0
    alcoholSum = 0
    virusSum = 0
    virusSum = 0 
    scoreSum = 0

#------Reload---------

def reloadGame(event):
    global isReload,virusProcess
    virusProcess= False
    sound('click')
    resetItem()
    if isReload[0]:
        isReload[0] = False
        low(event)
    elif isReload[1]:
        isReload[1] = False
        meduim(event)
    elif isReload[2]:
        isReload[2] = False
        hight(event) 

# -------stopGame----

def stopProcess(event):
    global virusProcess
    virusProcess = False
    displayGrid(level)
    resetItem()
    draw.after(150, lambda:menuGame(event))

#---------next-level

def nextLevel(event):
    global isNext
    sound('click')
    resetItem()
    if isNext[1]:
        isNext[1] = False
        meduim(event)
    elif isNext[2]:
        isNext[2] = False
        hight(event)

#------------------move Hero---------------------
#---get position hero and unlock door

def positionHero(grid, charater):
    global isLock, virusProcess
    pos = []
    numVirus = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == charater:
                pos.append(row)
                pos.append(col)
            if (grid[row][col] == VIRUS) or (grid[row][col] == DENGER_VIRUS0) or (grid[row][col] == DENGER_VIRUS1) or (grid[row][col] == DENGER_VIRUS2) or (grid[row][col] == DENGER_VIRUS3) or (grid[row][col] == DENGER_VIRUS4) or (grid[row][col] == DENGER_VIRUS5) or (grid[row][col] == DENGER_VIRUS6):
                numVirus += 1
    if numVirus == 0:
        isLock = False
        virusProcess= False
    return pos

#-----move contain---

def movePositionHero(row, col, moveCol, moveRow):
    conditionGamePlay(moveRow, moveCol)
    if level[moveRow][moveCol] != WALL and level[moveRow][moveCol] != DOOR:
            level[moveRow][moveCol] = 1
            level[row][col] = 0
            
#-----move hero------D

def moveHero(grid, move):
    global isHeroLeft
    position = positionHero(grid, HERO)
    row = position[0]
    col = position[1]
    if health > 0 and isClick:
        if move =='left':
            movePositionHero(row, col, col-1, row)
            isHeroLeft = True
        elif move == 'right':
            movePositionHero(row, col, col+1, row)
            isHeroLeft = False
        elif move == 'up':
            movePositionHero(row, col, col, row-1)
        elif move == 'down':
            movePositionHero(row, col, col, row+1)
        displayGrid(level)

def moveLeft(event):
    moveHero(level, 'left')  

def moveRght(event):  
    moveHero(level, 'right') 

def moveUp(event):
    moveHero(level,'up')  

def moveDown(event):
    moveHero(level, 'down')  
    
# -----Choose-level----------

def low(event):
    global level, isReload, isNext, isClick, virusProcess
    isClick = True
    isNext[0] = False
    isNext[1] = True
    isNext[2] = False 
    isReload[0] = True
    virusProcess = True
    level =[
        [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
        [7,1,0,0,0,0,0,0,0,10,0,0,0,0,0,7,0,0,0,7,6,0,0,0,0,0,7],
        [7,0,7,7,7,0,7,0,7,0,7,7,7,7,7,7,0,7,0,7,7,7,7,0,7,0,7],
        [7,0,7,0,7,7,7,0,7,0,7,9,0,0,0,7,0,7,0,7,0,0,0,2,7,7,7],
        [7,0,7,0,0,0,0,0,7,0,7,7,0,0,0,7,0,7,7,7,0,0,0,0,0,0,7],
        [7,0,0,7,7,7,7,7,7,0,2,0,0,7,0,0,0,0,0,0,0,0,7,7,7,0,7],
        [7,0,7,9,0,0,0,0,7,0,7,7,7,7,0,0,7,7,7,7,0,7,0,7,9,0,7],
        [7,0,7,0,0,7,0,0,0,0,7,9,0,0,0,0,7,9,0,7,0,7,0,7,0,0,7],
        [7,0,0,0,7,7,7,7,7,0,7,0,7,6,7,0,7,7,0,7,0,7,0,0,2,0,7],
        [7,0,0,0,6,7,0,0,0,0,0,0,7,7,7,0,0,7,0,0,11,0,0,0,7,0,7],
        [7,7,7,7,7,7,0,7,0,7,0,7,0,0,0,14,7,7,0,0,7,0,7,0,7,0,7],
        [7,0,2,0,0,0,0,0,6,7,2,7,0,0,6,0,0,0,0,0,7,0,0,9,7,0,7],
        [7,7,7,7,7,7,7,7,7,7,0,7,0,7,7,7,7,7,7,0,7,7,7,7,7,7,7],
        [7,9,0,0,0,0,0,0,0,0,6,7,6,7,5,0,0,0,0,0,0,0,0,0,0,0,8],
        [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
    ]
    enemyContainer()
    displayGrid(level)

def meduim(event):
    global level, isReload, isNext, isClick, virusProcess
    isClick = True
    isNext[0] = False
    isNext[1] = False
    isNext[2] = True 
    isReload[1] = True
    virusProcess= True
    level = [
        [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
        [7,1,0,0,0,0,7,0,6,0,0,0,0,0,2,0,9,0,0,9,0,6,0,2,9,0,8],
        [7,7,7,7,7,0,7,0,7,0,7,6,7,0,7,0,7,0,7,0,7,0,7,7,7,0,7],
        [7,9,7,2,0,0,7,0,0,0,0,0,0,15,0,0,0,0,0,0,0,0,0,0,7,0,7],
        [7,0,7,0,7,0,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,9,7,0,7,0,7],
        [7,0,0,6,7,0,0,0,5,0,7,14,0,0,0,0,0,0,0,0,0,0,7,0,7,0,7],
        [7,0,7,7,7,0,7,7,7,0,7,7,6,0,7,7,7,7,0,7,7,7,7,0,7,0,7],
        [7,0,0,0,0,0,0,6,0,0,7,0,7,0,0,0,0,2,0,0,0,0,9,0,0,0,7],
        [7,7,7,7,7,0,7,7,7,0,9,0,7,10,7,7,6,7,0,7,7,7,7,7,7,0,7],
        [7,6,0,2,0,13,0,2,7,0,0,0,0,0,9,0,0,0,2,0,0,0,0,2,7,0,7],
        [7,0,7,0,7,7,7,0,7,0,7,5,7,0,7,7,7,7,7,7,7,9,7,0,7,0,7],
        [7,0,9,0,0,0,5,0,7,0,0,0,0,0,6,0,2,0,0,0,0,0,0,0,7,0,7],
        [7,2,7,7,7,7,0,0,7,12,7,0,7,0,7,9,7,0,7,0,7,0,7,0,7,11,7],
        [7,0,9,0,0,0,0,6,0,0,0,6,0,0,0,0,0,2,0,0,0,0,6,0,0,0,7],
        [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
    ]
    enemyContainer()
    displayGrid(level)

def hight(event):
    global level, isReload, isClick, virusProcess
    isClick = True
    isReload[2] = True
    virusProcess= True
    level = [
        [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
        [7,6,7,1,7,5,7,0,0,0,0,2,0,6,7,9,7,7,6,7,9,7,6,0,0,2,7],
        [7,0,7,0,7,0,7,7,7,0,7,7,7,0,7,0,0,7,0,7,0,7,0,7,7,7,7],
        [7,0,9,0,7,6,0,0,0,0,0,7,2,0,7,16,0,0,0,7,0,7,0,0,0,6,7],
        [7,2,7,7,7,7,7,7,7,7,7,7,0,7,7,7,7,7,0,7,2,7,0,7,7,7,7],
        [7,0,7,9,0,0,2,0,0,0,9,7,0,7,6,0,0,0,6,7,0,0,2,0,0,9,7],
        [7,0,0,0,6,7,0,0,0,7,0,7,0,0,14,7,7,7,7,8,7,7,0,7,7,7,7],
        [7,7,7,7,7,7,0,7,0,7,0,0,0,7,9,0,0,0,0,0,7,0,0,7,9,0,7],
        [7,9,0,0,0,0,6,7,0,0,7,7,7,7,7,7,7,6,7,5,7,0,10,0,0,0,7],
        [7,0,7,7,7,7,7,7,0,0,0,6,7,15,0,0,0,0,0,0,7,0,7,7,7,7,7],
        [7,2,7,6,0,2,0,0,11,0,7,7,7,0,7,7,7,7,7,7,7,0,0,0,0,9,7],
        [7,0,7,7,7,7,7,0,7,0,0,7,0,0,7,9,0,0,0,0,0,7,0,7,7,7,7],
        [7,0,7,9,0,6,7,0,7,0,2,7,0,0,7,7,0,7,7,0,0,7,0,0,7,9,7],
        [7,0,0,0,0,0,7,9,7,12,0,5,7,0,9,0,0,7,6,2,0,0,13,0,0,0,7],
        [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
    ]
    enemyContainer()
    displayGrid(level)
# ==================================MAIN======================================

root = Tk()
root.geometry(str(WINDOWS_WIDTH) + 'x' + str(WINDOWS_HIGHT))
frame = Frame()
frame.master.title('KILL THE VIRUS')
draw = Canvas(frame)

# ==================================SOUND======================================

def sound(name):
    if name == 'click':
        name = winsound.PlaySound("sound/click.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif name == 'win':
        name = winsound.PlaySound("sound/win.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif name == 'loss':
        name = winsound.PlaySound("sound/loes.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif name == 'chooesLevel':
        name = winsound.PlaySound("sound/choose-level.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif name == 'startGame':
        name = winsound.PlaySound("sound/startGame.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif name == 'coin':
        name = winsound.PlaySound("sound/coin.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif name == 'colect':
        name = winsound.PlaySound("sound/colectItem.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif name == 'upHealth':
        name = winsound.PlaySound("sound/upHealth.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif name == 'lowhealth':
        name = winsound.PlaySound("sound/lowHealth.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    return name
# ==================================IMAGE======================================
# -----background--------
bglevel1 = PhotoImage(file = 'image/backgroundLevel2.png')
bgRule = PhotoImage(file = 'image/bg-rules.png')
bgChoose = PhotoImage(file = 'image/bgChooseLevel.png')
bgStart = PhotoImage(file = 'image/backgroundLevel1.png')
winBackground = PhotoImage(file = 'image/backgroundWin2.png')
lostBackground  = PhotoImage(file = 'image/bg-start.png')
# --------button----------
btnlevel = PhotoImage(file = 'image/button1.png')
btnBack = PhotoImage(file = 'image/buttonreturn.png')
gameBack = PhotoImage(file = 'image/backgame.png')
btnNext = PhotoImage(file = 'image/buttonNext.png')
btnStart = PhotoImage(file = 'image/button-start1.png')
instrution1 = PhotoImage(file = 'image/game-control.png')
instrution2 = PhotoImage(file = 'image/game-rule.png')
instrutionWins = PhotoImage(file = 'image/instrutionwin.png')
reloads = PhotoImage(file = 'image/reload.png')
backHome = PhotoImage(file = 'image/backHome.png')
exits = PhotoImage(file = 'image/exit.png')
# ----------hero-----------
heroleft = PhotoImage(file = 'image/heroLeft.png')
heroRight = PhotoImage(file = 'image/heroRight.png')
wallpic = PhotoImage(file = 'image/wall.png')
floorPic = PhotoImage(file = 'image/floor.png')
virusHero = PhotoImage(file = 'image/virus1.png')
virusDenger = PhotoImage(file = 'image/virus.png')
# --------------health---------
fulHealth = PhotoImage(file = 'image/health3.png')
meduimHealth = PhotoImage(file = 'image/health2.png')
lowHealth = PhotoImage(file = 'image/health1.png')
lowHealth = PhotoImage(file = 'image/health1.png')
# ----------------item-----------
paradolpic = PhotoImage(file = 'image/Oralmedicine.png')
maskpic = PhotoImage(file = 'image/mask.png')
alcoholpic = PhotoImage(file = 'image/syringe.png')
# -------------door--------
lockDoor = PhotoImage(file = 'image/doorclose.png')
unlockDoor = PhotoImage(file = 'image/dooropen.png')
# ---------------lose and win------
lost= PhotoImage(file = 'image/bglost.png')
win = PhotoImage(file = 'image/bgwin.png')
# ------------navBar-----------
navMask = PhotoImage(file = 'image/icon-navMask.png')
navCoins = PhotoImage(file = 'image/icon-navCoin.png')
navEnemy = PhotoImage(file = 'image/icon-navCovid.png')
navAlkohol = PhotoImage(file = 'image/icon-navAlcohol.png')
hearlthpic = PhotoImage(file = 'image/hearth.png')
# -------------star-and total point-------------
star1 = PhotoImage(file = 'image/star1.png')
star2 = PhotoImage(file = 'image/star2.png')
star3 = PhotoImage(file = 'image/star3.png')
totalKill = PhotoImage(file = 'image/total-enemy.png')
totalCoin = PhotoImage(file = 'image/total_coin.png')
# -------charater----
amongHero=PhotoImage(file = 'image/among-charater.png')
jeryHero=PhotoImage(file = 'image/jery-charater.png')
# ==================================PROCESS======================================
startGame('start')
readCoin()
# -------control------------------------------------
#interface
draw.tag_bind('start', '<Button-1>' ,menuGame)
draw.tag_bind('back1', '<Button-1>', startGame)
draw.tag_bind('back2', '<Button-1>', startGame)
draw.tag_bind('back3', '<Button-1>', menuGame)
draw.tag_bind('instrutions', '<Button-1>', instrution)
draw.tag_bind('exit', '<Button-1>', WinDestroy)
draw.tag_bind('backHome', '<Button-1>', backMenu)
draw.tag_bind('reload', '<Button-1>', reloadGame)
draw.tag_bind('next', '<Button-1>',nextLevel)
draw.tag_bind('stopGame', '<Button-1>',stopProcess)
draw.tag_bind('Charater', '<Button-1>',chooesHero)
draw.tag_bind('Hero2', '<Button-1>',charaterOne)
draw.tag_bind('Hero3', '<Button-1>',charaterTwo)
#choose--level-----

draw.tag_bind('level', '<Button-1>', low)
draw.tag_bind('level2', '<Button-1>', meduim)
draw.tag_bind('level3', '<Button-1>', hight)

# ---move control------

root.bind('<Left>', moveLeft)
root.bind('<Right>', moveRght)
root.bind('<Up>', moveUp)
root.bind('<Down>', moveDown)
root.bind('<a>', moveLeft)
root.bind('<d>', moveRght)
root.bind('<w>', moveUp)
root.bind('<s>', moveDown)

# ==================================End======================================
draw.pack(expand = True,fill = 'both')
frame.pack(expand = True,fill = 'both')
root.mainloop()