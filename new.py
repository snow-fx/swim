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
    print("v0.0.1")
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
            print(pyautogui.position())
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
            print(pyautogui.position())
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
            print(pyautogui.position())
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
    print(str(whichdung))
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
        print(pyautogui.position())
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
            print(pyautogui.position())
            time.sleep(random.randint(2, 5))
            pyautogui.moveRel(random.randint(0, 2), random.randint(0, 2), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # pyautogui.click()
            print(pyautogui.position())
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
        print(pyautogui.position())
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
    doublekill = 0
    x = 0
    lostbattle = None
    wonbattle = None
    totalruns = 0
    howmanyruns = random.randint(30, 80)
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
            print(pyautogui.position())
            # pyautogui.click()
            # print(pyautogui.position())
            time.sleep(random.randint(2, 5))
            pyautogui.moveRel(random.randint(-7, 7), random.randint(-7, 7), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            print(pyautogui.position())
            # pyautogui.click()
            # print(pyautogui.position())
            time.sleep(random.randint(2, 5))
            totalruns += 1
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
                x = random.randint(1, 50)
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
            print(pyautogui.position())
            # pyautogui.click(wonbattle)
            x = random.randint(1, 10)
            pyautogui.moveRel(random.randint(-7, 7), random.randint(-7, 7), .2)
            time.sleep(x / 10)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            # pyautogui.click()
            print(pyautogui.position())
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
            print(pyautogui.position())
            # pyautogui.click()

            # pyautogui.click(prepare)
            time.sleep(random.randint(5, 13))
            indungbattle = pyautogui.locateOnScreen('indungbattle.png', confidence=.9)
            pyautogui.moveTo(indungbattle)
            pyautogui.moveRel(random.randint(-20, 35), random.randint(-10, 25), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            print(pyautogui.position())
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
            print(pyautogui.position())
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
            print(pyautogui.position())
            # pyautogui.click(replay)
            totalruns += 1
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
            print(pyautogui.position())
            # pyautogui.click()

            # pyautogui.click(shoprefill)
            time.sleep(random.randint(1, 3))
            rechargeenergy = pyautogui.locateOnScreen('rechargeenergy.png', confidence=.98)
            pyautogui.moveTo(rechargeenergy)
            pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            print(pyautogui.position())
            # pyautogui.click()

            # pyautogui.click(rechargeenergy)
            time.sleep(random.randint(1, 3))
            quiz = pyautogui.locateOnScreen('quiz.png', confidence=.98)
            if quiz is not None:
                print("QUIZ!!!")
                pyautogui.moveTo(quix)
                pyautogui.moveRel(350, 0, 1)
                pyautogui.mouseDown()
                time.sleep(random.randrange(123, 357) / 1000)
                pyautogui.mouseUp()
                print(pyautogui.position())
                # pyautogui.click()
                sys.exit()
            yes = pyautogui.locateOnScreen('yes.png', confidence=.98)
            pyautogui.moveTo(yes)
            pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            print(pyautogui.position())
            # pyautogui.click()

            # pyautogui.click(yes)
            time.sleep(random.randint(1, 3))
            ok2 = pyautogui.locateOnScreen('ok2.png', confidence=.98)
            pyautogui.moveTo(ok2)
            pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            print(pyautogui.position())
            # pyautogui.click()

            # pyautogui.click(ok2)
            time.sleep(random.randint(1, 3))
            closewindow = pyautogui.locateOnScreen('closerefill.png', confidence=.98)
            pyautogui.moveTo(closewindow)
            pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            print(pyautogui.position())
            # pyautogui.click()

            # pyautogui.click(closewindow)
            time.sleep(random.randint(1, 3))
            refills += 1


def checkloot():
    global lootdrops
    global runedrops
    global runeskept
    global totalruns
    global howmanyrun
    global refills
    global doublekill
    doublekill = 1
    directory = r'C:\swim\images'
    os.chdir(directory)
    # print("Checking loot")
    ok = pyautogui.locateOnScreen('ok.png', confidence=.98)
    sellrune = pyautogui.locateOnScreen('sellrune.png', confidence = .94)
    if sellrune is not None:
        ok = None
        # print("Rune Drop")
        runedrops += 1
        evalrune()
    if ok is not None:
        # print("Dropped loot")
        lootdrops += 1
        pyautogui.moveTo(ok)
        pyautogui.moveRel(random.randint(5, 15), random.randint(5, 15), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        print(pyautogui.position())
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
        print(pyautogui.position())
        # pyautogui.click()

        # pyautogui.click(otherloot)
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
        print(pyautogui.position())
        # pyautogui.click(replay)
        totalruns += 1
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
        print(pyautogui.position())
        # pyautogui.click()

        # pyautogui.click(shoprefill)
        time.sleep(random.randint(1, 3))
        rechargeenergy = pyautogui.locateOnScreen('rechargeenergy.png', confidence=.98)
        pyautogui.moveTo(rechargeenergy)
        pyautogui.moveRel(random.randint(0, 25), random.randint(0, 25), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        print(pyautogui.position())
        # pyautogui.click()

        # pyautogui.click(rechargeenergy)
        time.sleep(random.randint(1, 3))
        quiz = pyautogui.locateOnScreen('quiz.png', confidence=.98)
        if quiz is not None:
            print("QUIZ!!!")
            pyautogui.moveTo(quiz)
            pyautogui.moveRel(350, 0, 1)
            pyautogui.mouseDown()
            time.sleep(random.randrange(123, 357) / 1000)
            pyautogui.mouseUp()
            print(pyautogui.position())
            # pyautogui.click()
            sys.exit()
        yes = pyautogui.locateOnScreen('yes.png', confidence=.98)
        pyautogui.moveTo(yes)
        pyautogui.moveRel(random.randint(0, 20), random.randint(0, 20), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        print(pyautogui.position())
        # pyautogui.click()

        # pyautogui.click(yes)
        time.sleep(random.randint(1, 3))
        ok2 = pyautogui.locateOnScreen('ok2.png', confidence=.98)
        pyautogui.moveTo(ok2)
        pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        print(pyautogui.position())
        # pyautogui.click()

        # pyautogui.click(ok2)
        time.sleep(random.randint(1, 3))
        closewindow = pyautogui.locateOnScreen('closerefill.png', confidence=.98)
        pyautogui.moveTo(closewindow)
        pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        print(pyautogui.position())
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

    directory = r'C:\swim\images'
    os.chdir(directory)
    time.sleep(5)
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
    runesubs = runestr.split()
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
    print("Rune Drop:")
    print(runesubs)
    if '|' in runesubs:
        index = runesubs.index('|')
        runesubs[index] = '1'
    if any(q in runesubs for q in ['Strong', 'Tenacious', 'Ferocious', 'Powerful', 'Sturdy', 'Durable', 'Quick', 'Mortal', 'Cruel', 'Resistant', 'Intricate']):
        # print("Innate stat")
        del runesubs[0]
        runeinnate = [runesubs[5], runesubs[6]]
        del runesubs[6]
        del runesubs[5]
        # print(runesubs)
    runetype = runesubs[0]
    runeslot = runesubs[2]

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
    print(runeslot)
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
    if sixstar is not None and ('360' in runesubs[4] or '22' in runesubs[4]) and (runeslot == '(2)' or runeslot == '(4)' or runeslot == '(6)'):
        selltherune = True
        reason = "Flat main stat"
    if fivestar is not None and 'Swift' in runesubs and 'SPD' in runesubs and runegrade > 2:
        selltherune = False
        reason = "swift with speed"
    # print("==========================")
    if selltherune:
        print("Selling rune " + '\n' + str(reason))
        pyautogui.moveTo(sellrunecoord)
        pyautogui.moveRel(random.randint(0, 15), random.randint(0, 15), 1)
        pyautogui.mouseDown()
        time.sleep(random.randrange(123, 357) / 1000)
        pyautogui.mouseUp()
        print(pyautogui.position())
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
        file.write(dt_string + " " + str(runeword) + " " + str(runestar) + "* " + converttostr(runesubs, seperator) + "\n")
        file.close()
        print(pyautogui.position())
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
        print(pyautogui.position())
        file = open("runelog.txt", "a")
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        seperator = '\t'
        file.write(dt_string + " " + str(runeword) + " " + str(runestar) + "* " + converttostr(runesubs, seperator) + "\n")
        file.close()
        # pyautogui.click()
        runeskept += 1


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
    global totalruns
    global lootdrops
    global runedrops
    global runeskept
    global currentdung
    global whichdung
    global howmanyruns
    global refills
    refills = 0
    totalruns = 0
    lootdrops = 0
    runedrops = 0
    runeskept = 0
    currentdung = 0
    whichdung = random.randint(1, 3)
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
