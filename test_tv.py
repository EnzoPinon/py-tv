# import class TV from my class file:

from class_tv import TV

# Create 2 new TVs:

tv01 = TV("HirayaTV", 50, 120, False)

tv02 = TV("NieselTV", 30, 900, True)

# demonstrate viewing all stats of the TV

tv01.view()
tv02.view()

# demonstrate get_volume and get_channel methods

tv01.get_volume()
tv02.get_channel()

# Demonstration of error message in setting channel/volume as string or other variables
tv01.set_channel("hello")

tv02.set_volume(20.1)

tv01.set_channel(False)

# Demonstration of error message when setting volume to a number not within the range of 0-100

tv02.set_volume(-1)
tv01.set_volume(999)

# Demonstration of volume change and channel change with proof by calling get_channel and get_volume

tv01.set_channel(200)
tv01.get_channel()

tv02.set_volume(50)
tv02.get_volume()

# Demonstration of TV switched on and off

tv01.turn_on()
tv02.turn_off()

# Demonstration of error message when other variables are passed to the rename method

tv01.rename(2023)
tv02.rename(20.2)
tv01.rename(False)

# Demonstration of renaming the TV

tv01.rename("Lucario")

# Demonstration of increasing and decreasing the volume of the TV:

tv02.volume_down()
tv01.volume_up()

# Demonstration of switching channels forward and backward 

tv01.channel_down()
tv02.channel_up()

# Print with view again as final status of all TVs as proof that it has been modified with all methods:

tv01.view()
tv02.view()