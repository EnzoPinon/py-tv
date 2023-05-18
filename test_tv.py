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

# Demonstration of error message in setting channel/volume as string
tv01.set_channel("hello")

tv02.set_volume("hi")

# Demonstration of error message when setting volume to a number not within the range of 0-100

tv02.set_volume(-1)
tv01.set_volume(999)

# Demonstration of volume change and channel change with proof by calling get_channel and get_volume

tv01.set_channel(200)
tv01.get_channel()

tv02.set_volume(50)
tv02.get_volume()