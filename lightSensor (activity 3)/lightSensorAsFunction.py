from microbit import *

# emphasize the importance of comments 
# so you can come back to your code later and know what everything does

# -------------------------------------------------------------------------------------------
# the temp sensor function.
def temp_sensor():
    microbitTemp = temperature() 
    offset = -3

    actualTemp = microbitTemp + offset

    display.scroll(actualTemp)
    display.clear()

# -------------------------------------------------------------------------------------------
# the light sensor function.
def light_sensor():
    
    while(not(accelerometer.was_gesture('shake'))):
        lightLevel = display.read_light_level()
        if (lightLevel <= 40):
            # range: 0 - 40
            # too dark for my plant 
            # will show sad face
            display.show(Image.MEH)
        elif (lightLevel <= 100):
            # range: 41 - 100
            # good range of light for my plant
            display.show(Image.HAPPY)
        else:
            # range: 101 - 255
            # too bright for my plant
            display.show(Image.SAD)
          
    display.clear()

# -------------------------------------------------------------------------------------------
# main loop

# main script. This is like the manager of our program. It will call the correct methods 
# depending on how we interact with the microbit

# again, they can put any valid statement that will cause the while loop to run forever
while True:

    # if the microbit is shook then call the temp sensor method. It knows what to do. 
    if(accelerometer.was_gesture('shake')):
        temp_sensor()
        
    # if button A is pressed then call the light sensor method. It knows what to do.         
    if(button_a.is_pressed()):
        light_sensor()

# click on flash to upload this program to your microbit 