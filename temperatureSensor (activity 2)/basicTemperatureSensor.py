from microbit import *

while (1==1):
    
    if (accelerometer.was_gesture('shake')):
        temp = temperature() 
        display.scroll(temp)
        
    display.clear()
        
        
# click on flash to upload this program to your microbit 
        
    