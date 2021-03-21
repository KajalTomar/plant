from microbit import *
# https://microbit-micropython.readthedocs.io/en/v1.0.1/tutorials/images.html

# everything in the while loop keeps happening over and over again
# as long as the while condition is true

# what will this condition do? 
while (1==1):
    
    # we have declared a variable called num and set it's value to 5
    num = 0; 
    
    # ways to compare to numbers
    # (number 1) == (number 2) // numbers are the same
    # (number 1) <= (number 2) // number 1 is smaller than or equal to number 2 
    # (number 1) >= (number 2) // number 1 is bigger than or equal to number 2 
    
    if(num == 5): 
        display.show(Image.SILLY)
    elif(num >= 10):
        display.show(Image.PACMAN)
    else:
        display.show(Image.BUTTERFLY)

  


