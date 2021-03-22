from microbit import *


# indentations in the right place are important. You always indent once for all the lines that are inside a function. 

# ask them to come up with their own statement that is always true
# so that we can run the loop forever (ex: while True, while 5==5, while 4!=6, while not false)
while (1==1):
    
    # we have declared a variable called num and set it's value to 5 (for now)
    num = 5; 
    
    # ways to compare to numbers
    # (number 1) == (number 2) // numbers are the same
    # (number 1) <= (number 2) // number 1 is smaller than or equal to number 2 
    # (number 1) >= (number 2) // number 1 is bigger than or equal to number 2 
    
    # they can choose which image they would like to display 
    # the following link has a list of images that are included in the microbit libary
    # https://microbit-micropython.readthedocs.io/en/v1.0.1/tutorials/images.html
    if(num == 5): 
        display.show(Image.SILLY)
    elif(num >= 10):
        display.show(Image.PACMAN)
    else:
        display.show(Image.BUTTERFLY)

# click on flash to upload this program to your microbit 
# change the value of num and predict what will happen 
# change the condition statements