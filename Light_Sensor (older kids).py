# Add your Python code here. E.g.
from microbit import *

# write down troubleshooting steps

## LEVEL ONE 

# while True:
#    lightLevel = display.read_light_level()
#    display.scroll(lightLevel)
#    sleep(2000)
        
## LEVEL TWO 

#while True:
#    if(button_a.is_pressed()):
#        lightLevel = display.read_light_level()
#        display.scroll(lightLevel)
#        sleep(2000)
    
## LEVEL THREE
# go around house and note down the light levels for different brightness:
# ex: condition                               lightLevel
# -----------------------------------------------------------
#    direct sunlight                            255
#  light from north-facing window
#  light from south-facing window
#  light from east-facing window
#  light from west-facing window
#  under my desk lamp
#  in my room

# this level will vary for each person
# use your findings to create nested if statements to:
# show a happy face when the sunlight is the desired level for your plant 
# show an image of your choice when the spot is alright (but not ideal)
# lastly a sad face for a bad spot 

# for this example I'm going to pretend I have seeds for Dracaena fragrans (Corn Plant)
# this plant requires low light, intense dark sunlight is bad for it. 

# while True:
#    if(button_a.is_pressed()):
#        lightLevel = display.read_light_level()
#        if (lightLevel <= 40):
#            # range: 0 - 40
#            # too dark for my plant 
#            # will show sad face
#            display.show(Image.MEH)
#        elif (lightLevel <= 100):
#            # range: 41 - 100
#            # good range of light for my plant
#            display.show(Image.HAPPY)
#        else:
#            # range: 101 - 255
#            # too bright for my plant
#            display.show(Image.SAD)
#        sleep(2000)
#        display.clear()

# LEVEL 4

# in this level we take the code we have for the light sensor and move it into a method 
# why? this allows our code to be more organized and readable.
# this will be really useful as we add more functionality to our microbit

# emphasize the importance of comments 
# so you can come back to your code later and know what everything does


def light_sensor():
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
    sleep(2000)
    display.clear()

# main script. This is like the manager of our program. It will call the correct methods 
# depending on how we interact with the microbit

while True:
    # this fill loop forever
    
    # if button A is pressed then call the light sensor method. It knows what to do. 
    if(button_a.is_pressed()):
        light_sensor() 
        




    
