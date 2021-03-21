from microbit import *


# fill out chart
#
# soil moisture level       reading 
# ------------------------------------
#       dry                 802
#       moist               1000
#       wet                 1014

# use this chart to inform what the micro bit shows

while True:
    # constants are a type of variable whose value 
    # should never be changed
    # in python, we name constants in all caps so we know which values 
    # should never be reassigned
    DRY = 802
    MOIST = 1000
    WET = 1020
    num = pin1.read_analog()
    
    # display.scroll(num)
    
    # logic: explain and, or, and not 
    # why would (num<= DRY or num>=wet) be wrong? 
    while(not((num > DRY) and (num < WET))):
        num = pin1.read_analog()
        display.show(Image.SKULL)
        sleep(1000)
        display.clear()
        sleep(1000)
        
    display.show(Image.TARGET)
    

        

  

    
        

