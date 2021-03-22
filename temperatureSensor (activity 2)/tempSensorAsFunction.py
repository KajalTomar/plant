from microbit import *

# in this level we take the code we have for the temperature sensor and move it into a method 
# why? this allows our code to be more organized and readable.
# this will be really useful as we add more functionality to our microbit

# emphasize the importance of comments 
# so you can come back to your code later and know what everything does

# the temp sensor function.
def temp_sensor():
    microbitTemp = temperature() 
    offset = -3

    actualTemp = microbitTemp + offset

    display.scroll(actualTemp)
    display.clear()

# -------------------------------------------------------------------------------------------
# main loop

# main script. This is like the manager of our program. It will call the correct methods 
# depending on how we interact with the microbit

# again, they can put any valid statement that will cause the while loop to run forever
while (1==1):

    # if the microbit is shook then call the temp sensor method. It knows what to do. 
    if(accelerometer.was_gesture('shake')):
        temp_sensor()

# click on flash to upload this program to your microbit 