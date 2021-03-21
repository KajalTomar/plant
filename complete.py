from microbit import *

# in this level we take the code we have for the light sensor and move it into a method 
# why? this allows our code to be more organized and readable.
# this will be really useful as we add more functionality to our microbit

# emphasize the importance of comments 
# so you can come back to your code later and know what everything does

# explain global scope
# explain scope
DRY = 802
WET = 1020

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

def temp_sensor():
    difference = -3
    actualTemp = temperature() + (difference)
    
    display.scroll(actualTemp)
    sleep(1000)
    display.clear()
    
def soil_moisture_sensor():
    # constants are a type of variable whose value 
    # should never be changed
    # in python, we name constants in all caps so we know which values 
    # should never be reassigned
    # DRY = 802
    # WET = 1020
    num = pin1.read_analog()
    
    # display.scroll(num)
    
    # logic: explain and, or, and not 
    # why would (num<= DRY or num>=wet) be wrong? 
    while(not((num > DRY) and (num < WET))):
        if(accelerometer.was_gesture('shake')): # if we just wanted to check the 
               # moisture level and not water it right now
            break
        else:
            num = pin1.read_analog()
            display.show(Image.SKULL)

    if((num > DRY) and (num < WET)):
        display.show(Image.TARGET)
        sleep(1000)
    
    display.clear()
# main script. This is like the manager of our program. It will call the correct methods 
# depending on how we interact with the microbit

while True:
    # this fill loop forever
    
    
       # if button A is pressed then call the light sensor method. It knows what to do. 
    if(accelerometer.was_gesture('shake')):
        temp_sensor()
        
    if(button_a.is_pressed()):
        light_sensor()
        
    if(button_b.is_pressed()):
        soil_moisture_sensor()

        

  

    
        

