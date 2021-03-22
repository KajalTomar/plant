from microbit import *


# indentations in the right place are important. You always indent once for all the lines that are inside a function. 

# ask them to come up with their own statement that is always true
# so that we can run the loop forever (ex: while True, while 5==5, while 4!=6, while not false)
while (1==1):
    
    # we have declared a variable called num and set it's value to 5 (for now)
    num = 5; 

    if(button_a.is_pressed()):
        break
    elif(num == 5): 
        display.show(Image.SILLY)
    elif(num >= 10):
        display.show(Image.PACMAN)
    else:
        display.show(Image.BUTTERFLY)

# click on flash to upload this program to your microbit 
# change the value of num and predict what will happen 
# change the condition statements