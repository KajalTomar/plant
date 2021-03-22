from microbit import *

# ask them to come up with their own statement that is always true
# so that we can run the loop forever (ex: while True, while 5==5, while 4!=6, while not false)
while (1==1):

    if(button_b.is_pressed()):
        # reads in the moisture level in the pin 
        moistureLvl = pin0.read_analog()
        display.scroll(moistureLvl)

# click on flash to upload this program to your microbit 
# try covering the microbit with your hand and then press A,
# shine a light on the microbit 