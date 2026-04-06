import pymem

pm = pymem.Pymem("GAMENAMEFROMCHEATENGINE")

address = ADDRESSFROMCHEATENGINE (Format: 0xnumbers)

suns = pm.read_int(address)

print("Current suns:", suns)

user_input = int(input("how many of this item do you want?"))

pm.write_int(address,user_input)

print ("Successfully hacked the game!")
