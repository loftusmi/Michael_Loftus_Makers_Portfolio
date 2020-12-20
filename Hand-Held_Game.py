#! /usr/bin/ipython3
import graphics
from time import sleep
import random

from gpiozero import DistanceSensor

from pythonosc import osc_message_builder
from pythonosc import udp_client

#graphics defaults
WINDIMENX = 700
WINDIMENY = 440
CIRCDIAM = 20
msgtxt = "You Lose!"

def main_game():                                                          # define main method 
    keepplaying = True
    (win, circ, message, sensor) = initialize()
    keepplaying = playquery(win)
    while keepplaying == True:
        balloongame(win, circ, message, sensor)
        setdefaults(win, circ, message)
        keepplaying = playquery(win)
    endcleanup(win, circ, message, sensor)
    

def initialize():                                                                                 # Initializes graphics display
    (win, circ, message, sensor) = createobjects(WINDIMENX, WINDIMENY, CIRCDIAM)
    setdefaults(win, circ, message)
    return win, circ, message, sensor


def createobjects(WINDIMENX, WINDIMENY, CIRCDIAM):               #Creates graphics objects
    win = graphics.GraphWin("game", WINDIMENX, WINDIMENY)
    win.setCoords(0, 0, WINDIMENX, WINDIMENY)
    ctrpt = graphics.Point(WINDIMENX / 2, WINDIMENY / 2)
    circ = graphics.Circle(ctrpt, CIRCDIAM)
    circ.setFill("black")
    circ.setOutline("orange")
    circ.setWidth(3)
    message = graphics.Text(graphics.Point(WINDIMENX / 2, 0.219 * WINDIMENX), "")
    message.draw(win)
    sensor = DistanceSensor(echo = 17, trigger = 4)
    circ.draw(win)
    return win, circ, message, sensor


def setdefaults(win, circ, message):                       #Randomizes circle diameter, border color, and inner color
    message.setText("DO yU plAy? now\nYes  No")            #I now recognize that there are better ways to code this section, but this is what I came up with as I was first learning to code   
    winheight = win.getHeight()
    endctr = circ.getCenter()
    dy = (winheight / 2) - endctr.y
    circ.move(0, dy)
    colornumber1 = random.randint(1,20)
    colornumber2 = random.randint(1,20)
    colornumber3 = random.randint(1,20)
    randwidth = random.randint(1,20)
    if(colornumber1 == 1):
        color1 = "red"
    if(colornumber2 == 1):
        color2 = "red"
    if(colornumber3 == 1):
        color3 = "red"
    if(colornumber1 == 2):
        color1 = "black"
    if(colornumber2 == 2):
        color2 = "black"
    if(colornumber3 == 2):
        color3 = "white"
    if(colornumber1 == 3):
        color1 = "orange"
    if(colornumber2 == 3):
        color2 = "orange"
    if(colornumber3 == 3):
        color3 = "orange"
    if(colornumber1 == 4):
        color1 = "yellow"
    if(colornumber2 == 4):
        color2 = "yellow"
    if(colornumber3 == 4):
        color3 = "yellow"
    if(colornumber1 == 5):
        color1 = "purple"
    if(colornumber2 == 5):
        color2 = "purple"
    if(colornumber3 == 5):
        color3 = "purple"
    if(colornumber1 == 6):
        color1 = "tan"
    if(colornumber2 == 6):
        color2 = "tan"
    if(colornumber3 == 6):
        color3 = "tan"
    if(colornumber1 == 7):
        color1 = "pink"
    if(colornumber2 == 7):
        color2 = "pink"
    if(colornumber3 == 7):
        color3 = "pink"
    if(colornumber1 == 8):
        color1 = "violet"
    if(colornumber2 == 8):
        color2 = "violet"
    if(colornumber3 == 8):
        color3 = "violet"
    if(colornumber1 == 9):
        color1 = "teal"
    if(colornumber2 == 9):
        color2 = "teal"
    if(colornumber3 == 9):
        color3 = "teal"
    if(colornumber1 == 10):
        color1 = "turquoise"
    if(colornumber2 == 10):
        color2 = "turquoise"
    if(colornumber3 == 10):
        color3 = "turquoise"
    if(colornumber1 == 11):
        color1 = "brown"
    if(colornumber2 == 11):
        color2 = "brown"
    if(colornumber3 == 11):
        color3 = "white"
    if(colornumber1 == 12):
        color1 = "grey"
    if(colornumber2 == 12):
        color2 = "grey"
    if(colornumber3 == 12):
        color3 = "grey"
    if(colornumber1 == 13):
        color1 = "blue"
    if(colornumber2 == 13):
        color2 = "blue"
    if(colornumber3 == 13):
        color3 = "white"
    if(colornumber1 == 14):
        color1 = "light blue"
    if(colornumber2 == 14):
        color2 = "light blue"
    if(colornumber3 == 14):
        color3 = "light blue"
    if(colornumber1 == 15):
        color1 = "dark blue"
    if(colornumber2 == 15):
        color2 = "dark blue"
    if(colornumber3 == 15):
        color3 = "white"
    if(colornumber1 == 16):
        color1 = "green"
    if(colornumber2 == 16):
        color2 = "green"
    if(colornumber3 == 16):
        color3 = "white"
    if(colornumber1 == 17):
        color1 = "light green"
    if(colornumber2 == 17):
        color2 = "light green"
    if(colornumber3 == 17):
        color3 = "light green"
    if(colornumber1 == 18):
        color1 = "dark green"
    if(colornumber2 == 18):
        color2 = "dark green"
    if(colornumber3 == 18):
        color3 = "white"
    if(colornumber1 == 19):
        color1 = "white"
    if(colornumber2 == 19):
        color2 = "white"
    if(colornumber3 == 19):
        color3 = "white"
    if(colornumber1 == 20):
        color1 = "olive"
    if(colornumber2 == 20):
        color2 = "olive"
    if(colornumber3 == 20):
        color3 = "white"
    circ.setFill(color1)
    circ.setOutline(color2)
    circ.setWidth(randwidth)
    win.setBackground("black")
    message.setTextColor(color3)

def playquery(win):                                                                   # Reads whether the user selected yes or no
    keepplaying = False
    clickpt = win.getMouse()
    #yes
    if((clickpt.x <= WINDIMENX / 2) and (clickpt.y <= WINDIMENY/2)):
        keepplaying = True
    return keepplaying
    

def endcleanup(win, circ, message, sensor):               # What to do if the user selects "No"
    sensor.close()
    del sensor
    circ.undraw()
    del circ
    win.close()
    del win
    del message


def balloongame(win, circ, message, sensor):              # Defines motion of the circle and what to do when the circle touches the top or bottom of the screen
    radius = circ.getRadius()
    repetitions = 10000
    gravity = 100
    win_top = win.getHeight()
    vi = 0.
    t = 0.01
    dx = 0
    a = -1.0*gravity
    for i in range(repetitions):

        distancechange = gethandmotion(sensor)
        print(distancechange)

        message.setText("Score: %s" % (i / 100.))
 
        #circle velocity
        vf = vi + a * t
        dy = (vf * t)# / 0.00043333 this is m/pixel
        vi = vf + (distancechange * 500)
        
        circ.move(dx, dy + distancechange)

        #touching top and bottom borders
        ctr = circ.getCenter()
        
        #at window bottom
        if(ctr.y - radius <= 0):
            message.setText("You Lose!\nScore: %s" % (i / 100))
            sleep(3)
            return
        #at window top
        if(ctr.y + radius >= win_top):
            message.setText("You Lose!\nScore: %s" % (i / 100))
            sleep(3)
            return
        if(i == repetitions):
            message.setText("You Win!\nScore: %s" % (i / 100))
            sleep(3)
            return

def gethandmotion(sensor):                # Used by main method to read the motion in front of the ultrasonic sensor
    i = True
    while i == True:
        sensordistance1 = sensor.distance
        sleep(0.01)
        sensordistance2 = sensor.distance
        distancechange = sensordistance2 - sensordistance1
        if(distancechange > 0.01):
            return distancechange
        else:
            return 0.0


main_game()                #call main function


