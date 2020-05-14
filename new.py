# cv2.cvtColor takes a numpy ndarray as an argument
# import numpy as np
import pytesseract
import time
import cv2
import os
import pyautogui
import random
from PIL import ImageGrab, Image  # , ImageEnhance
from os import system, name
from datetime import datetime
import configparser
import re

pyautogui.PAUSE = .25


def converttostr(input_seq, seperator):
   # Join all the strings in list
   final_str = seperator.join(input_seq)
   return final_str


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def starting():
    print("Starting the script")
    print("v0.0.2")
    print("   - Psych O")
    # totalruns = 0
    # rundungs = True
    # runarena = True
    # rundhole =  False
    # rungiants = True
    # rundrags = True
    # runnecro = True
    # arenaruns = -1
    # dungeonruns = 250
    # giantsruns = random.randint(128,192)
    # dragsruns = random.randint(100,180)
    # necroruns = random.randint(100,150)
    # print(rundungeons)


def lookforpopups():
    directory = r'C:\swim\images'
    os.chdir(directory)
    print("Looking for popups")
    closewin = None
    xx = 0
    # look for an [X] in popup window, five times
    while closewin is None and xx < 5:
        closewin = pyautogui.locateOnScreen('exit1.png', confidence=.8)
        if closewin is not None:
            print("Found a popup")
            pyautogui.moveTo(closewin)
            pyautogui.moveRel(random.randint(0, 10), random.randint(0, 10), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # pyautogui.click()
            # print(pyautogui.position())
            time.sleep(random.randint(1, 3))
            closewin = None
        time.sleep(1)
#       print (xx)
        xx += 1


def cairos():
    directory = r'C:\swim\images'
    os.chdir(directory)
    clickbattle = None
    clickcairos = None
    xx = 0
    while clickbattle is None and clickcairos is None and xx < 5:
        clickbattle = pyautogui.locateOnScreen('battle.png', confidence=.8)
        if clickbattle is not None:
            # print("Going to map")
            pyautogui.moveTo(clickbattle)
            pyautogui.moveRel(random.randint(0, 25), random.randint(0, 25), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # pyautogui.click()
            # print(pyautogui.position())
            # pyautogui.click(clickbattle)
            time.sleep(random.randint(2, 4))
            # clickbattle = None
        clickcairos = pyautogui.locateOnScreen('cairos.png', confidence=.8)
        if clickcairos is not None:
            pyautogui.moveTo(clickcairos)
            pyautogui.moveRel(random.randint(-25, 25), random.randint(-25, 25), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # pyautogui.click()
            # print(pyautogui.position())
            # pyautogui.click(clickcairos)
            time.sleep(random.randint(2, 4))
#        clickbattle = None
        clickcairos = None
        time.sleep(1)
        xx += 1
    startbattle()


def startbattle():
    directory = r'C:\swim\images'
    os.chdir(directory)
    rundung = None
    clickb10 = None
    # print(str(whichdung))
    if whichdung == 1:
        rundung = pyautogui.locateOnScreen('giants.png', confidence=.8)
        currentdung = 1
    if whichdung == 2:
        rundung = pyautogui.locateOnScreen('drags.png', confidence =.8)
        currentdung = 2
    if whichdung == 3:
        rundung = pyautogui.locateOnScreen('necro.png', confidence=.8)
        currentdung = 3
    time.sleep(3)
    if rundung is not None:
        print("Gonna run dungeon:" + str(currentdung))
        # clickdung = pyautogui.locateOnScreen(rundung, confidence=.8)
        pyautogui.moveTo(rundung)
        pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        # pyautogui.click()
        # print(pyautogui.position())
        # pyautogui.click(rundung)
        time.sleep(2)
        clickb10 = pyautogui.locateOnScreen('b10.png', confidence=.8)
        if clickb10 is not None:
            # print(str(clickb10))
            pyautogui.moveTo(clickb10)
            pyautogui.moveRel(170, 0, 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # pyautogui.click()
            # print(pyautogui.position())
            time.sleep(random.randint(2, 5))
            pyautogui.moveRel(random.randint(0, 2), random.randint(0, 2), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # pyautogui.click()
            # print(pyautogui.position())
            # clickb10 = (clickb10.left+300, clickb10.top, clickb10.width, clickb10.height)
            # clickb10.left += 300
            # print(str(clickb10))
    autoormanual = None
    autoormanual = pyautogui.locateOnScreen('clickauto.png', confidence=.98)
    if autoormanual is not None:
        print("Starting auto battle")
        pyautogui.moveTo(autoormanual)
        pyautogui.moveRel(random.randint(0, 5), random.randint(0, 5), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        # print(pyautogui.position())
        # pyautogui.click()

        # pyautogui.click(autoormanual)
        time.sleep(.7)
        autoormanual = None


def rundungeons():
    directory = r'C:\swim\images'
    os.chdir(directory)
    global totalruns
    global howmanyruns
    global lootdrops
    global runedrops
    global runeskept
    global doublekill
    global refills
    global alltimeruns
    global alltimerunes
    global alltimerunessold
    global alltimeloot
    cfg = configparser.ConfigParser()
    cfg.read('stats.txt')
    # x = cfg.get('Stats', 'TotalRuns')
    # alltimeruns = int(x)
    # x = cfg.get('Stats', 'TotalRunes')
    # alltimerunes = int(x)
    # x = cfg.get('Stats', 'TotalRunesSold')
    # alltimerunessold = int(x)
    # x = cfg.get('Stats', 'TotalLoot')
    # alltimeloot = int(x)
    doublekill = 0
    x = 0
    lostbattle = None
    wonbattle = None
    totalruns = 0
    howmanyruns = random.randint(50, 180)
    while totalruns <= howmanyruns:
        lostbattle = pyautogui.locateOnScreen('revive.png', confidence=.9)
        if lostbattle is not None:
            print("Lost a run")
            time.sleep(random.randint(5, 50))
            pyautogui.moveTo(lostbattle)
            pyautogui.moveRel(170, 0, 1)
            time.sleep(random.randint(2, 5))
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # (pyautogui.position())
            # pyautogui.click()
            # print(pyautogui.position())
            time.sleep(random.randint(2, 5))
            pyautogui.moveRel(random.randint(-7, 7), random.randint(-7, 7), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # print(pyautogui.position())
            # pyautogui.click()
            # print(pyautogui.position())
            time.sleep(random.randint(2, 5))
            totalruns += 1
            cfg = configparser.ConfigParser()
            cfg.read('stats.txt')
            x = cfg.get('Stats', 'TotalRuns')
            # print("loaded: " + x)
            y = int(x)
            y += 1
            # print("changed: " + str(y))
            cfg.set('Stats', 'TotalRuns', str(y))
            with open('stats.txt', 'w') as conf:
                cfg.write(conf)

            print(str(x) + " alltimeruns")
            x = cfg.get('Stats', 'TotalRuns')
            # print("Reloaded: " + str(x))

            print(str(totalruns) + "/" + str(howmanyruns) + " runs completed")
            print("Total loot  : " + str(lootdrops))
            print("Total Runes : " + str(runedrops))
            print("Runes Kept  : " + str(runeskept))
            print("Refills     : " + str(refills))

        wonbattle = pyautogui.locateOnScreen('wonbattle.png', confidence=.9)
        sellrune = pyautogui.locateOnScreen('sellrune.png', confidence=.94)
        if wonbattle is not None and sellrune is None:
            # print("Finished a run")
            time.sleep(3)
            wonbattle = pyautogui.locateOnScreen('wonbattle.png', confidence=.95)
            # pyautogui.moveTo(wonbattle)
            # pyautogui.moveRel(random.randint(-100, 150), random.randint(-39, 150), 1)
            # pyautogui.click()
            if doublekill > 0 or doublekill is None:
                x = random.randint(1, 30)
            else:
                doublekill = 0
            if x < 20:
                y = random.randint(3, 8)
                # time.sleep(random.randint(3, 8))
            if 20 < x < 35:
                y = random.randint(5, 20)
                # time.sleep(random.randint(5, 20))
            if 35 < x < 45:
                y = random.randint(10, 30)
                # time.sleep(random.randint(10, 30))
            if 45 < x < 49:
                y = random.randint(20, 60)
                # time.sleep(random.randint(20, 60))
            if x == 50:
                y = random.randint(60, 480)
                # time.sleep(random.randint(60, 480))
            if y == 0 or y is None:
                y = 4
            print("Pausing for " + str(y) + " secs.")
            time.sleep(y)
            # time.sleep(random.randint(4, 120))
            pyautogui.moveTo(wonbattle)
            pyautogui.moveRel(random.randint(-100, 150), random.randint(-39, 150), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # pyautogui.click()
            # print(pyautogui.position())
            # pyautogui.click(wonbattle)
            x = random.randint(1, 10)
            pyautogui.moveRel(random.randint(-7, 7), random.randint(-7, 7), .2)
            time.sleep(x / 10)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # pyautogui.click()
            # print(pyautogui.position())
            # pyautogui.click(wonbattle)
            checkloot()
            wonbattle = None
        else:
            if sellrune is not None:
                checkloot()
            time.sleep(random.randint(2,10))
        prepare = pyautogui.locateOnScreen('prepare.png', confidence=.95)
        if prepare is not None:
            print("Starting over")
            pyautogui.moveTo(prepare)
            pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # print(pyautogui.position())
            # pyautogui.click()

            # pyautogui.click(prepare)
            time.sleep(random.randint(5, 13))
            indungbattle = pyautogui.locateOnScreen('indungbattle.png', confidence=.9)
            pyautogui.moveTo(indungbattle)
            pyautogui.moveRel(random.randint(-20, 35), random.randint(-10, 25), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # print(pyautogui.position())
            # pyautogui.click()

            # pyautogui.click(indungbattle)
            time.sleep(random.randint(1, 3))
        otherloot = pyautogui.locateOnScreen('otherloot.png', confidence=.96)
        if otherloot is not None:
            pyautogui.moveTo(otherloot)
            pyautogui.moveRel(random.randint(-10, 15), random.randint(-10, 15), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # print(pyautogui.position())
            # pyautogui.click()

            # (otherloot)
            time.sleep(random.randint(1, 3))
        replay = pyautogui.locateOnScreen('replay.png', confidence=.9)
        if replay is not None:
            # print("Lets do it again")
            pyautogui.moveTo(replay)
            pyautogui.moveRel(random.randint(-80, 173), random.randint(-18, 25), 0.5)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # pyautogui.click(replay)
            # print(pyautogui.position())
            # pyautogui.click(replay)
            totalruns += 1
            # x = cfg.get('Stats', 'TotalRuns')
            # alltimeruns = int(x)
            # alltimeruns += 1
            # cfg.set('Stats', 'TotalRuns', str(alltimeruns))
            # with open('stats.txt', 'w') as conf:
            #     cfg.write(conf)
            # print(str(alltimeruns) + " alltimeruns")
            cfg = configparser.ConfigParser()
            cfg.read('stats.txt')
            x = cfg.get('Stats', 'TotalRuns')
            # print("loaded2: " + str(x))
            y = int(x)
            y += 1
            # print("changed2: " + str(y))
            cfg.set('Stats', 'TotalRuns', str(y))
            with open('stats.txt', 'w') as conf:
                cfg.write(conf)

            print(str(y) + " alltimeruns2")
            x = cfg.get('Stats', 'TotalRuns')
            # print("Reloaded2: " + str(x))

            print(str(totalruns) + "/" + str(howmanyruns) + " runs completed")
            print("Total loot  : " + str(lootdrops))
            print("Total Runes : " + str(runedrops))
            print("Runes Kept  : " + str(runeskept))
            print("Refills     : " + str(refills))
            time.sleep(random.randint(1, 3))
        shoprefill = pyautogui.locateOnScreen('shop.png', confidence=.98)
        if shoprefill is not None:
            print("Need to refill")
            pyautogui.moveTo(shoprefill)
            pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # print(pyautogui.position())
            # pyautogui.click()

            # pyautogui.click(shoprefill)
            time.sleep(random.randint(1, 3))
            rechargeenergy = pyautogui.locateOnScreen('rechargeenergy.png', confidence=.98)
            pyautogui.moveTo(rechargeenergy)
            pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # print(pyautogui.position())
            # pyautogui.click()

            # pyautogui.click(rechargeenergy)
            time.sleep(random.randint(1, 3))
            quiz = pyautogui.locateOnScreen('quiz.png', confidence=.98)
            if quiz is not None:
                print("QUIZ!!!")
                im1 = pyautogui.screenshot()
                im1.save(r'c:\swim\images\quizes\quiz' + random.randint(10,10000) +'.png', )
                pyautogui.moveTo(quiz)
                pyautogui.moveRel(465, 440, 1)
                pyautogui.mouseDown()
                time.sleep(random.randrange(123, 357) / 1000)
                pyautogui.mouseUp()
                # print(pyautogui.position())
                # pyautogui.click()
                # sys.exit()
            yes = pyautogui.locateOnScreen('yes.png', confidence=.98)
            pyautogui.moveTo(yes)
            pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # print(pyautogui.position())
            # pyautogui.click()

            # pyautogui.click(yes)
            time.sleep(random.randint(1, 3))
            ok2 = pyautogui.locateOnScreen('ok2.png', confidence=.98)
            pyautogui.moveTo(ok2)
            pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # print(pyautogui.position())
            # pyautogui.click()

            # pyautogui.click(ok2)
            time.sleep(random.randint(1, 3))
            closewindow = pyautogui.locateOnScreen('closerefill.png', confidence=.98)
            pyautogui.moveTo(closewindow)
            pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # print(pyautogui.position())
            # pyautogui.click()

            # pyautogui.click(closewindow)
            time.sleep(random.randint(1, 3))
            refills += 1


def checkloot():
    directory = r'C:\swim\images'
    os.chdir(directory)
    global lootdrops
    global runedrops
    global runeskept
    global totalruns
    global howmanyrun
    global refills
    global doublekill
    global alltimeruns
    global alltimerunes
    global alltimerunessold
    global alltimeloot
    cfg = configparser.ConfigParser()
    cfg.read('stats.txt')
    # x = cfg.get('Stats', 'TotalRuns')
    # alltimeruns = int(x)
    # x = cfg.get('Stats', 'TotalRunes')
    # alltimerunes = int(x)
    # x = cfg.get('Stats', 'TotalRunesSold')
    # alltimerunessold = int(x)
    # x = cfg.get('Stats', 'TotalLoot')
    # alltimeloot = int(x)
    doublekill = 1
    # print("Checking loot")
    ok = pyautogui.locateOnScreen('ok.png', confidence=.98)
    sellrune = pyautogui.locateOnScreen('sellrune.png', confidence = .94)
    if sellrune is not None:
        ok = None
        # print("Rune Drop")
        # x = cfg.get('Stats', 'TotalRunes')
        # alltimerunes = int(x)
        # alltimerunes += 1
        # cfg.set('Stats', 'TotalRunes', str(alltimerunes))
        # with open('stats.txt', 'w') as conf:
        #     cfg.write(conf)

        # print(str(alltimerunes) + " alltimerunes")
        cfg = configparser.ConfigParser()
        cfg.read('stats.txt')
        x = cfg.get('Stats', 'TotalRunes')
        # print("loaded3: " + str(x))
        y = int(x)
        y += 1
        # print("changed3: " + str(y))
        cfg.set('Stats', 'TotalRunes', str(y))
        with open('stats.txt', 'w') as conf:
            cfg.write(conf)

        print(str(y) + " alltimerunes")
        x = cfg.get('Stats', 'TotalRunes')
        # print("Reloaded3: " + str(x))

        runedrops += 1
        evalrune()
    if ok is not None:
        # print("Dropped loot")
        cfg = configparser.ConfigParser()
        cfg.read('stats.txt')
        x = cfg.get('Stats', 'TotalLoot')
        # print("loaded4: " + str(x))
        y = int(x)
        y += 1
        # print("changed4: " + str(y))
        cfg.set('Stats', 'TotalLoot', str(y))
        with open('stats.txt', 'w') as conf:
            cfg.write(conf)

        print(str(y) + " alltimeloot")
        x = cfg.get('Stats', 'TotalLoot')
        # print("Reloaded4: " + str(x))

        # x = cfg.get('Stats', 'TotalLoot')
        # alltimeloot = int(x)
        # alltimeloot += 1
        # cfg.set('Stats', 'TotalLoot', str(alltimeloot))
        # with open('stats.txt', 'w') as conf:
        #     cfg.write(conf)

        # print(str(alltimeloot) + " alltimeloot")

        lootdrops += 1
        pyautogui.moveTo(ok)
        pyautogui.moveRel(random.randint(5, 15), random.randint(5, 15), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        # print(pyautogui.position())
        # pyautogui.click()

        # pyautogui.click(ok)
        time.sleep(3)
        # ok = None
    otherloot = pyautogui.locateOnScreen('otherloot.png', confidence=.95)
    if otherloot is not None:
        # print("Found some event loot")
        pyautogui.moveTo(otherloot)
        pyautogui.moveRel(random.randint(5, 15), random.randint(5, 15), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        # print(pyautogui.position())
        # pyautogui.click()

        # pyautogui.click(otherloot)
        cfg = configparser.ConfigParser()
        cfg.read('stats.txt')
        x = cfg.get('Stats', 'TotalLoot')
        # ("loaded5: " + str(x))
        y = int(x)
        y += 1
        # print("changed5: " + str(y))
        cfg.set('Stats', 'TotalLoot', str(y))
        with open('stats.txt', 'w') as conf:
            cfg.write(conf)

        print(str(y) + " alltimeloot")
        x = cfg.get('Stats', 'TotalLoot')
        # print("Reloaded5: " + str(x))

        # x = cfg.get('Stats', 'TotalLoot')
        # alltimeloot = int(x)
        # alltimeloot += 1
        # cfg.set('Stats', 'TotalLoot', str(alltimeloot))
        # with open('stats.txt', 'w') as conf:
        #     cfg.write(conf)

        # print(str(alltimeloot) + " alltimeloot")
        lootdrops += 1
        time.sleep(3)
    replay = pyautogui.locateOnScreen('replay.png', confidence=.9)
    if replay is not None:
        # print("Lets do it again")
        pyautogui.moveTo(replay)
        pyautogui.moveRel(random.randint(-80, 173), random.randint(-18, 25), 0.5)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        # pyautogui.click(replay)
        # print(pyautogui.position())
        # pyautogui.click(replay)
        totalruns += 1
        cfg = configparser.ConfigParser()
        cfg.read('stats.txt')
        x = cfg.get('Stats', 'TotalRuns')
        # print("loaded6: " + str(x))
        y = int(x)
        y += 1
        # print("changed6: " + str(y))
        cfg.set('Stats', 'TotalRuns', str(y))
        with open('stats.txt', 'w') as conf:
            cfg.write(conf)

        print(str(y) + " alltimeruns")
        x = cfg.get('Stats', 'TotalRuns')
        # print("Reloaded6: " + str(x))

        # x = cfg.get('Stats', 'TotalRuns')
        # alltimeruns = int(x)
        # alltimeruns += 1
        # cfg.set('Stats', 'TotalRuns', str(alltimeruns))
        # with open('stats.txt', 'w') as conf:
        #     cfg.write(conf)

        # print(str(alltimeruns) + " alltimeruns")

        print(str(totalruns) + "/" + str(howmanyruns) + " runs completed")
        print("Total loot  : " + str(lootdrops))
        print("Total Runes : " + str(runedrops))
        print("Runes Kept  : " + str(runeskept))
        print("Refills     : " + str(refills))
        time.sleep(3)
    shoprefill = pyautogui.locateOnScreen('shop.png', confidence=.98)
    if shoprefill is not None:
        print("Need to refill")
        pyautogui.moveTo(shoprefill)
        pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        # (pyautogui.position())
        # pyautogui.click()

        # pyautogui.click(shoprefill)
        time.sleep(random.randint(1, 3))
        rechargeenergy = pyautogui.locateOnScreen('rechargeenergy.png', confidence=.98)
        pyautogui.moveTo(rechargeenergy)
        pyautogui.moveRel(random.randint(0, 25), random.randint(0, 25), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        # print(pyautogui.position())
        # pyautogui.click()

        # pyautogui.click(rechargeenergy)
        time.sleep(random.randint(1, 3))
        quiz = pyautogui.locateOnScreen('quiz.png', confidence=.98)
        if quiz is not None:
            print("QUIZ!!!")
            im1 = pyautogui.screenshot()
            im1.save(r'c:\swim\images\quizes\quiz' + str(random.randint(10, 10000) + '.png', ))
            pyautogui.moveTo(quiz)
            pyautogui.moveRel(465, 440, 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # print(pyautogui.position())
            # pyautogui.click()
        yes = pyautogui.locateOnScreen('yes.png', confidence=.98)
        pyautogui.moveTo(yes)
        pyautogui.moveRel(random.randint(0, 20), random.randint(0, 20), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        # print(pyautogui.position())
        # pyautogui.click()

        # pyautogui.click(yes)
        time.sleep(random.randint(1, 3))
        ok2 = pyautogui.locateOnScreen('ok2.png', confidence=.98)
        pyautogui.moveTo(ok2)
        pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        # print(pyautogui.position())
        # pyautogui.click()

        # pyautogui.click(ok2)
        time.sleep(random.randint(1, 3))
        closewindow = pyautogui.locateOnScreen('closerefill.png', confidence=.98)
        pyautogui.moveTo(closewindow)
        pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        # print(pyautogui.position())
        # pyautogui.click()

        # pyautogui.click(closewindow)
        time.sleep(random.randint(1, 3))
        refills += 1


def get_concat_v_cut(im1, im2):
    dst = Image.new('RGB', (min(im1.width, im2.width), im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst


def get_concat_v_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst


def get_concat_v_multi_blank(im_list):
    _im = im_list.pop(0)
    for im in im_list:
        _im = get_concat_v_blank(_im, im)
    return _im


def evalrune():
    global lootdrops
    global runedrops
    global runeskept
    global alltimeruns
    global alltimerunes
    global alltimerunessold
    global alltimeloot
    cfg = configparser.ConfigParser()
    cfg.read('stats.txt')
    # x = cfg.get('Stats', 'TotalRuns')
    # alltimeruns = int(x)
    # x = cfg.get('Stats', 'TotalRunes')
    # alltimerunes = int(x)
    # x = cfg.get('Stats', 'TotalRunesSold')
    # alltimerunessold = int(x)
    # x = cfg.get('Stats', 'TotalLoot')
    # alltimeloot = int(x)

    directory = r'C:\swim\images'
    os.chdir(directory)
    time.sleep(2)
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
    sellrunecoord = pyautogui.locateOnScreen('sellrune.png', confidence = .96)
    coord = list(sellrunecoord)
    x1 = coord[0]
    y1 = coord[1]
    # print(str(coord))
    # print(str(x1) + " " + str(y1))
    # top part of rune
    # print(str(x1-47) + " " + str(y1-261) + " " + str(x1+148) + " " + str(y1-166))
    im1 = ImageGrab.grab(bbox=(x1-76, y1-255, x1+220, y1-221))
    im2 = ImageGrab.grab(bbox=(x1-47, y1-221, x1+148, y1-156))
    # stats of rune
    im3 = ImageGrab.grab(bbox=(x1-117, y1-157, x1+128, y1-62))
    # merge into one image
    # get_concat_v_cut(im1, im2, im3).save("conc.png", "png")
    # get_concat_v_cut(getconcat_v_cut(im1, im2), im3).save("conc.png", "png")
    get_concat_v_multi_blank([im1, im2, im3]).save("conc.png", "png")
    # pre processing
    image = cv2.imread('conc.png', 0)
    cv2.imwrite("gray.png", image)
    image = cv2.bitwise_not(image)
    cv2.imwrite("invert.png", image)
    runestr = pytesseract.image_to_string(image)
    # print(runestr)
    fivestar = pyautogui.locateOnScreen('fivestar.png', confidence=.99)
    sixstar = pyautogui.locateOnScreen('sixstar.png', confidence=.99)
    legend = pyautogui.locateOnScreen('legend.png', confidence=.99)
    hero = pyautogui.locateOnScreen('hero.png', confidence=.99)
    magic = pyautogui.locateOnScreen('magic.png', confidence=.99)
    defp = 0
    deff = 0
    atkp = 0
    atk = 0
    hpp = 0
    hp = 0
    cr = 0
    cd = 0
    res = 0
    acc = 0
    spd = 0
    selltherune = True
    runeinnate = None
    innate = ''
    innateis = 0
    if fivestar is not None:
        # print("Five Star Rune")
        runestar = 5
    if sixstar is not None:
        # print("Six Star Rune")
        runestar = 6
    if legend is not None:
        # print("Legend")
        runegrade = 4
        runeword = "Legend"
    if hero is not None:
        # print("Hero")
        runegrade = 3
        runeword = "Hero   "
    if magic is not None:
        # print("Magic")
        runegrade = 2
        runeword = "Magic  "
    # runesubs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # print(runestr)
    runesubs = runestr.split()
    runesubs.append('End')
    if 'Dmg' in runesubs:
        index = runesubs.index('Dmg')
        index = index - 1
        runesubs[index] = 'CD'
        runesubs.remove('Dmg')
    if 'Rate' in runesubs:
        index = runesubs.index('Rate')
        index = index - 1
        runesubs[index] = 'CR'
        runesubs.remove('Rate')
    # print(index)
    # print("Rune Drop:")
    # print(runesubs)
    if '|' in runesubs:
        index = runesubs.index('|')
        runesubs[index] = '1'
    leng = len(runesubs)
    # print(leng)
    # print(runesubs)
    #time.sleep(50)
    while leng >= 1:
        leng -= 1
        tempstr = runesubs[leng]
        # print(tempstr)
        # time.sleep(.5)
        if '+' in runesubs[leng][:1]:
            newstr = ''.join([tempstr[i] for i in range(len(tempstr)) if i != 0])
            runesubs[leng] = newstr
        # print(str(runesubs[leng]) + " " + str(leng))
    ress = []
    for ele in runesubs:
        sub = ele.split('+')
        ress.extend(sub)
    # print(runesubs)
    # print(res)
    runesubs = ress
    # time.sleep(50)
    if any(q in runesubs for q in ['Strong', 'Tenacious', 'Ferocious', 'Powerful', 'Sturdy', 'Durable', 'Quick', 'Mortal', 'Cruel', 'Resistant', 'Intricate']):
        # print("Innate stat")
        del runesubs[0]
        runeinnate = [runesubs[5], runesubs[6]]
        # del runesubs[6]
        # del runesubs[5]
        # print(runesubs)
    runetype = runesubs[0]
    runeslot = int(re.search(r'\d+', runesubs[2]).group())
    if 'Rune' in runesubs:
        index = runesubs.index('Rune')
        runesubs.remove('Rune')
        # print(runesubs)
    del runesubs[0]
    # print(runesubs)
    del runesubs[0]
    # print(runesubs)
    mainstat = runesubs[0]
    #print(mainstat)
    mainsub = runesubs[1]
    #print(mainsub)
    #print(runeslot)
    if '%' in mainsub:
        mainstat = mainstat + "%"
        # print(mainstat)
    if runeinnate is not None:
        innate = runesubs[2]
        innateis = int(re.search(r'\d+', runesubs[3]).group())
        del runesubs[3]
        del runesubs[2]
    # print(runesubs)
    del runesubs[1]
    del runesubs[0]
    # print(runesubs)
    while runesubs[0] != 'End':
        if 'DEF' in runesubs[0]:
            if '%' in runesubs[1]:
                defp = int(re.search(r'\d+', runesubs[1]).group())
            else:
                deff = int(runesubs[1])
            del runesubs[1]
            del runesubs[0]
        if 'ATK' in runesubs[0]:
            if '%' in runesubs[1]:
                atkp = int(re.search(r'\d+', runesubs[1]).group())
            else:
                # print(runesubs[0])
                # print(runesubs[1])
                # time.sleep(50)
                atk = int(runesubs[1])
            del runesubs[1]
            del runesubs[0]
        if 'HP' in runesubs[0]:
            if '%' in runesubs[1]:
                hpp = int(re.search(r'\d+', runesubs[1]).group())
            else:
                hp = int(runesubs[1])
            del runesubs[1]
            del runesubs[0]
        if 'CD' in runesubs[0]:
            cd = int(re.search(r'\d+', runesubs[1]).group())
            del runesubs[1]
            del runesubs[0]
        if 'CR' in runesubs[0]:
            cr = int(re.search(r'\d+', runesubs[1]).group())
            del runesubs[1]
            del runesubs[0]
        if 'Resistance' in runesubs[0]:
            res = int(re.search(r'\d+', runesubs[1]).group())
            print("wtf")
            del runesubs[1]
            del runesubs[0]
        if 'Accuracy' in runesubs[0]:
            acc = int(re.search(r'\d+', runesubs[1]).group())
            del runesubs[1]
            del runesubs[0]
        if 'SPD' in runesubs[0]:
            spd = runesubs[1]
            del runesubs[1]
            del runesubs[0]
    showsubs = True
    if showsubs == True:
        print("Rune type : " + runetype)
        print("Rune slot : " + str(runeslot))
        print("Main Stat : " + mainstat)
        print("Innate    : " + innate)
        print("            " + str(innateis))
        print("spd       : " + str(spd))
        print("atkp      : " + str(atkp))
        print("atk       : " + str(atk))
        print("defp      : " + str(defp))
        print("deff      : " + str(deff))
        print("hpp       : " + str(hpp))
        print("hp        : " + str(hp))
        print("cr        : " + str(cr))
        print("cd        : " + str(cd))
        print("res       : " + str(res))
        print("acc       : " + str(acc))
    # time.sleep(50)
    #    print("==========================")
#    print("= " + runetype + " " + runeslot + " " + runeword + " " + str(runestar) +"*")
#    print("= " + runesubs[3] + " " + runesubs[4] + " - Main")
#    if runeinnate is not None:
#        print("= " + runeinnate[0] + " " + runeinnate[1] + " - Innate")
#    print("= " + runesubs[5] + " " + runesubs[6])
#    print(len(runesubs))
#    if len(runesubs) >= 7:
#        print("= " + runesubs[7] + " " + runesubs[8])
#    if len(runesubs) > 9:
#        print("= " + runesubs[9] + " " + runesubs[10])
#    if len(runesubs) > 11:
#        print("= " + runesubs[11] + " " + runesubs[12])
    #keep or sell
    # print(runeslot)
    runesubs = runestr.split()
    runesubs.append('End')
    if 'Dmg' in runesubs:
        index = runesubs.index('Dmg')
        index = index - 1
        runesubs[index] = 'CD'
        runesubs.remove('Dmg')
    if 'Rate' in runesubs:
        index = runesubs.index('Rate')
        index = index - 1
        runesubs[index] = 'CR'
        runesubs.remove('Rate')
    if '|' in runesubs:
        index = runesubs.index('|')
        runesubs[index] = '1'
    if any(q in runesubs for q in ['Strong', 'Tenacious', 'Ferocious', 'Powerful', 'Sturdy', 'Durable', 'Quick', 'Mortal', 'Cruel', 'Resistant', 'Intricate']):
        # print("Innate stat")
        print(runesubs[0])
        del runesubs[0]
        runeinnate = [runesubs[5], runesubs[6]]
    if 'Rune' in runesubs:
        index = runesubs.index('Rune')
        runesubs.remove('Rune')
        # print(runesubs)
    # del runesubs[0]
    # print(runesubs)
    # del runesubs[0]

    if fivestar is not None:
        selltherune = True
        reason = "Five star rune"
    if sixstar is not None and runegrade > 2:
        selltherune = False
        reason = "Six star hero+"
    if sixstar is not None and runegrade == 2:
        selltherune = True
        reason = "Six star blue"
    if sixstar is not None and runegrade > 2:
        selltherune = False
        reason = "Six star hero+"
    if sixstar is not None and ('360' in runesubs[3] or '22' in runesubs[3]) and (runeslot == 2 or runeslot == 4 or runeslot == 6):
        selltherune = True
        reason = "Flat main stat"
        print("xxxxxxxxx")
    if fivestar is not None and 'Swift' in runesubs and 'SPD' in runesubs and runegrade > 2:
        selltherune = False
        reason = "swift with speed"
    # print(runesubs[0])
    # print(runesubs[1])
    # print(runesubs[2])
    # print(runesubs[3])
    # print(runesubs[4])
    # print(runeslot)
    # time.sleep(40)
    # print("==========================")
    # selltherune = True
    # print(selltherune)
    with open("c:\swim\images\pickit.txt", "r") as fp:
        line = fp.readline().strip()
        while line:
            ptype = None
            pslot = 0
            pdefp = 0
            pdeff = 0
            patkp = 0
            patk = 0
            phpp = 0
            php = 0
            pcr = 0
            pcd = 0
            pres = 0
            pacc = 0
            pspd = 0
            pgrade = 0
            pstar = 0
            pmain = None
            rightslot = False
            righttype = False
            rightmain = False
            ppslot = None
            sellorkeep = None
            # print(line)
            pickit = line.split()
            # print(pickit)
            pickit.append('END')
            cnt = 0
            while pickit[0] != 'END':
                if sellorkeep is not None:
                    fp.close()

                # print(pickit[0])
                pickit[0] = pickit[0].upper()
                pickit = [x.upper() for x in pickit]
                pickit = [x.strip() for x in pickit]
                # breaker = 0
                if '#' in pickit[0]:
                    # print('comment')
                    pickit[0] = 'END'
                    cnt += 1
                if 'SELLRUNES' in pickit[0]:
                    sellorkeep = True # sell if true
                    pickit[0] = 'END'
                    cnt += 1
                if 'KEEPRUNES' in pickit[0]:
                    sellorkeep = False # keep if false
                    pickit[0] = 'END'
                    cnt += 1
                if 'MAIN' in pickit:
                    index = pickit.index('MAIN')
                    pmain = pickit[index + 1]
                    del pickit[index + 1]
                    del pickit[index]
                    # print("pmain " + str(pmain))
                if 'STAR' in pickit:
                    index = pickit.index('STAR')
                    pstar = pickit[index + 1]
                    del pickit[index + 1]
                    del pickit[index]
                if 'GRADE' in pickit:
                    index = pickit.index('GRADE')
                    pgrade = pickit[index + 1]
                    del pickit[index + 1]
                    del pickit[index]
                if 'TYPE' in pickit:
                    index = pickit.index('TYPE')
                    ptype = pickit[index + 1]
                    # print(str(ptype) + " ptype")
                    del pickit[index + 1]
                    del pickit[index]
                    # print("ptype" + str(ptype))
                if 'SLOT' in pickit:
                    index = pickit.index('SLOT')
                    if pickit[index + 1] == 'ANY':
                        ppslot = 'ANY'
                    else:
                        pslot = int(pickit[index + 1])
                    # print("pslot " + str(pslot))
                    del pickit[index + 1]
                    del pickit[index]
                    # print("pslot" + str(pslot))
                if 'DEF%' in pickit:
                    index = pickit.index('DEF%')
                    pdefp = int(re.search(r'\d+', pickit[index + 1]).group())
                    del pickit[index + 1]
                    del pickit[index]
                if 'DEF' in pickit[0]:
                    index = pickit.index('DEF')
                    pdeff = int(pickit[index + 1])
                    del pickit[index + 1]
                    del pickit[index]
                    # print("pdefp" + str(pdefp))
                    # print("pdeff" + str(pdeff))
                if 'ATK%' in pickit:
                    index = pickit.index('ATK%')
                    patkp = int(re.search(r'\d+', pickit[index + 1]).group())
                    del pickit[index + 1]
                    del pickit[index]
                if 'ATK' in pickit[0]:
                    index = pickit.index('ATK')
                    patk = int(pickit[index + 1])
                    del pickit[index + 1]
                    del pickit[index]
                    # print("patkp" + str(patkp))
                    # print("patk" + str(patk))
                if 'HP%' in pickit:
                    index = pickit.index('HP%')
                    phpp = int(re.search(r'\d+', pickit[index + 1]).group())
                    del pickit[index + 1]
                    del pickit[index]
                if 'HP' in pickit:
                    index = pickit.index('HP')
                    php = int(pickit[index + 1])
                    del pickit[index + 1]
                    del pickit[index]
                    # print("phpp" + str(phpp))
                    # print("php" + str(php))
                if 'CD' in pickit:
                    index = pickit.index('CD')
                    pcd = int(re.search(r'\d+', pickit[index + 1]).group())
                    del pickit[index + 1]
                    del pickit[index]
                    # print("pcp" + str(pcp))
                if 'CR' in pickit:
                    index = pickit.index('CR')
                    pcr = int(re.search(r'\d+', pickit[index + 1]).group())
                    del pickit[index + 1]
                    del pickit[index]
                    # print("pcr" + str(pcr))
                if 'RES' in pickit:
                    index = pickit.index('RES')
                    pres = int(re.search(r'\d+', pickit[index + 1]).group())
                    del pickit[index + 1]
                    del pickit[index]
                    # print("pres" + str(pres))
                if 'ACC' in pickit:
                    index = pickit.index('ACC')
                    pacc = int(re.search(r'\d+', pickit[index + 1]).group())
                    del pickit[index + 1]
                    del pickit[index]
                    # print("pacc" + str(pacc))
                if 'SPD' in pickit:
                    index = pickit.index('SPD')
                    pspd = pickit[index + 1]
                    del pickit[index + 1]
                    del pickit[index]
                    # print("pspd" + str(pspd))
            # time.sleep(99)
            if str(runetype).upper() == str(ptype):
                righttype = True
                # print("right type ptype")
            if str(ptype) == str('ANY'):
                # print("ptype ANY")
                righttype = True
            if int(runeslot) == int(pslot):
                # print("right slot pslot")
                rightslot = True
            if ppslot == str('ANY'):
                # print("pslot ANY")
                rightslot = True
            if str(mainstat) == str(pmain):
                # print("mainstat pmain")
                rightmain = True
            if pmain == 'ANY':
                # print("pmain ANY")
                rightmain = True
            if righttype and rightslot and rightmain and defp >= pdefp and deff >= pdeff and atkp >= patkp and atk >= patk \
                and hpp >= phpp and hp >= php and cr >= pcr and cd >= pcd and res >= pres \
                and acc >= pacc and spd >= pspd and runegrade >= pgrade and runestar >= pstar:
                selltherune = sellorkeep
                reason = "Pickit"
                # breaker = 1
                print("found in pickit")
                # time.sleep(1)
            # print(selltherune)
            # print(str(runeslot) + " : " + str(pslot))
            # print(str(runetype) + " : " + str(ptype))
            # print(str(defp) + " : " + str(pdefp))
            # print(str(deff) + " : " + str(pdeff))
            # print(str(atkp) + " : " + str(patkp))
            # print(str(atk) + " : " + str(patk))
            # print(str(hpp) + " : " + str(phpp))
            # print(str(hp) + " : " + str(php))
            # print(str(cr) + " : " + str(pcr))
            # print(str(cd) + " : " + str(pcd))
            # print(str(res) + " : " + str(pres))
            # print(str(acc) + " : " + str(pacc))
            # print(str(spd) + " : " + str(pspd))
            # print(selltherune)
            # time.sleep(5)
            # if breaker == 1:
                # break
            line = fp.readline().strip()
            cnt += 1
            # print(str(cnt) + " : count")
    fp.close()
    print(selltherune)
    # time.sleep(40)
    if selltherune:

        print("Selling rune " + '\n' + str(reason))
        pyautogui.moveTo(sellrunecoord)
        pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        # print(pyautogui.position())
        # pyautogui.click()

        # pyautogui.click(sellrunecoord)
        time.sleep(random.randint(1, 3))
        pyautogui.moveRel(random.randint(-15, 15), random.randint(-110, -90), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        file = open("runelogsold.txt", "a")
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        seperator = '\t'
        runesubs = runestr.split()
        file.write(dt_string + " " + str(runeword) + " " + str(runestar) + "* " + converttostr(runesubs, seperator) + "   " + reason + "\n")
        file.close()
        # print(pyautogui.position())
        # pyautogui.click()
        time.sleep(random.randint(1, 3))
    else:
        # ok = pyautogui.locateOnScreen('ok.png', confidence=.98)
        print("Keeping rune " + '\n' + str(reason))
        pyautogui.moveTo(sellrunecoord)
        pyautogui.moveRel(150, 0, 1)
        time.sleep(random.randint(1, 3))
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        # print(pyautogui.position())
        file = open("runelog.txt", "a")
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        seperator = '\t'
        runesubs = runestr.split()
        file.write(dt_string + " " + str(runeword) + " " + str(runestar) + "* " + converttostr(runesubs, seperator) + "   " + reason + "\n")
        file.close()
        # pyautogui.click()
        runeskept += 1
        cfg = configparser.ConfigParser()
        cfg.read('stats.txt')
        x = cfg.get('Stats', 'TotalRunesSold')
        # print("loaded: " + str(x))
        y = int(x)
        y += 1
        # print("changed: " + str(y))
        cfg.set('Stats', 'TotalRunesSold', str(y))
        with open('stats.txt', 'w') as conf:
            cfg.write(conf)

        print(str(y) + " alltimeruns")

        x = cfg.get('Stats', 'TotalRunesSold')
        # print("Reloaded: " + str(x))

        # x = cfg.get('Stats', 'TotalRunesSold')
        # alltimerunessold = int(x)
        # alltimerunessold += 1
        # cfg.set('Stats', 'TotalRunesSold', str(alltimerunessold))
        # with open('stats.txt', 'w') as conf:
        #     cfg.write(conf)

        # print(str(alltimerunessold) + " alltimerunessold")

def imToString():
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
    while (True):
        # ImageGrab-To capture the screen image in a loop.
        # Bbox used to capture a specific area.
        im1 = ImageGrab.grab(bbox=(85, 340, 270, 400))
        im2 = ImageGrab.grab(bbox=(15, 440, 200, 520))
        get_concat_v_cut(im1, im2).save("conc.png", "png")
        # Read in image as grayscale
        image = cv2.imread('conc.png', 0)
        # Threshold to obtain binary image
        thresh = cv2.threshold(image, 20, 25, cv2.THRESH_BINARY)[1]

        directory = r'C:\swim'
        os.chdir(directory)
        cv2.imwrite("gray.png", image)
        image = cv2.bitwise_not(image)
        cv2.imwrite("invert.png", image)
#        cv2.imshow('thresh', thresh)
#        cv2.imshow('result', result)

        # Throw image into tesseract
        print("fixed:")
        print(pytesseract.image_to_string(image) + "\n")
        runestr = pytesseract.image_to_string(image)
        time.sleep(2)
        if "Focus" in runestr:
            print("Focus Rune")
            pyautogui.click(x = random.randint(430, 700), y = random.randint(360, 470))
            runeloc = pyautogui.locateOnScreen('sixstarrune.png')
        else:
            print("Something Else")

    # Calling the function


def mainloop():
    directory = r'C:\swim\images'
    os.chdir(directory)
    global totalruns
    global lootdrops
    global runedrops
    global runeskept
    global currentdung
    global whichdung
    global howmanyruns
    global refills
    global alltimeruns
    global alltimerunes
    global alltimerunessold
    global alltimeloot
    cfg = configparser.ConfigParser()
    cfg.read('stats.txt')
    # x = cfg.get('Stats', 'TotalRuns')
    # alltimeruns = int(x)
    # x = cfg.get('Stats', 'TotalRunes')
    # alltimerunes = int(x)
    # x = cfg.get('Stats', 'TotalRunesSold')
    # alltimerunessold = int(x)
    # get('Stats', 'TotalLoot')
    # alltimeloot = int(x)
   # print(str(alltimeruns))
    # time.sleep(100)
    refills = 0
    totalruns = 0
    lootdrops = 0
    runedrops = 0
    runeskept = 0
    currentdung = 0
    whichdung = random.randint(1, 3)
    # time.sleep(4)
    # evalrune()
    starting()
    lookforpopups()
#   islandstuff()
    cairos()
    startbattle()
    # should be in a dungeon by now
    rundungeons()
    evalrune()


mainloop()

# imToString()
