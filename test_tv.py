from class_tv import TV

# Create 2 new TVs:

tv01 = TV("HirayaTV", 50, 120, False)

tv02 = TV("NieselTV", 30, 900, True)

# demonstrate viewing all stats of the TV

tv01.view()
tv02.view()

# Demonstration of error message in setting channel/volume as string
tv01.set_channel("hello")

tv02.set_volume("hi")
