from microbit import *

# the miro:bit's temperature sensor checks how how the CPU is. 
# the tempature sensor has high precision, but isn't accurate. 
# What this means is that the temperature given is very precise, the microbit
# can sense changes in the teprature really well. It's not perfectectly accurate,
# beacuse the a base line offset. (So on my micro:bit it returns 28 degrees when it's
# actually 25 degrees, and it returns 12 degrees when it's actually 9 degrees. 
# Again, this is because the micro:bit is measure the temperature of it
# cpu not the air temperature. Since the offset is consistent we can account for it whe
# calculating and displaying the temprature. 

# if you have a thermometer in the house:
#   compare microbit's temperature to the thermostat. Write does the difference (is it + or -)? 

# check the temperature outside 
#   compare it to the microbit 

# check you fridge temperature
#   compare it to the microbit 

# come up with a general constant different 

while True:
    if (accelerometer.was_gesture('shake')):
        display.scroll(temperature()-3)
        display.clear()
        
        

        

