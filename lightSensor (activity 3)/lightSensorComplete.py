from microbit import *

# this is a function 
# this line means "I am defining this function and it's called light_sensor" 
# a function needs to have () after it. If light sensor needed information we would sent it in the brackets
def light_sensor():
    
    # do everything in this loop while microbit is steady
    # stops if someone shakes the microbit
    while(not(accelerometer.was_gesture('shake'))):
        
        ## read the light level and store it in a variable 
        ## called lightLevel
        
        lightLevel = display.read_light_level() 
        
        # note: display.read_light_level() is a function that someone else wrote from microbit
        # our program can use this function because we imported it from the microbit (first line of code)
        
        # show the right display depending on how much light is recieved 
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
        
    # clear the screen
    display.clear()


while True:
    # this will loop forever
        
    # if button a is pressed then call the light_sensor() function. 
    # it knows what to do
    if(button_a.is_pressed()):
        light_sensor()


# click on flash to upload this program to your microbit         

  


