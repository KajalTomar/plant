from microbit import *

# ask them to come up with their own statement that is always true
# so that we can run the loop forever (ex: while True, while 5==5, while 4!=6, while not false)
while (1==1):
    if (accelerometer.was_gesture('shake')):
        microbitTemp = temperature() 
        offset = -3

        actualTemp = microbitTemp + offset

        display.scroll(actualTemp)
        display.clear()
        
# click on flash to upload this program to your microbit 
        

