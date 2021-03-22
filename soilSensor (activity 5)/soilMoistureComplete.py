from microbit import *

# fill out chart
#
# soil moisture level       reading 
# ------------------------------------
#       dry                 802
#       moist               1000
#       wet                 1014

# use this chart to inform what the micro bit shows in this example

# again, they can put any valid statement that will cause the while loop to run forever
while True:

    # constants are a type of variable whose value should never be changed
    # in python, we name constants in all caps so we know which values 
    # should never be reassigned

    # constant 
    DRY = 802
    MOIST = 1000
    WET = 1020

    # variable
    num = pin1.read_analog()
    
    # logic: explain and, or, and not 
    # why would (num<= DRY or num>=wet) be wrong? 
    while(not((num > DRY) and (num < WET))):
        if(accelerometer.was_gesture('shake')): # if we just wanted to check the 
               # moisture level and not water it right now
            break
        else:
            num = pin1.read_analog() # notice that num is changing (it's a variable)
            display.show(Image.SKULL)

    if((num > DRY) and (num < WET)):
        display.show(Image.TARGET)
        sleep(1000)
    
    display.clear()
    
# click on flash to upload this program to your microbit 
        

  

    
        

