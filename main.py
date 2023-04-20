import os

sudoPass = "admin" # Enter your password here which you want to set
command = "create_ap wlo1 wlo1 Anonymous admin" # "create_ap wlo1 wlo1" this command stays as it is and Other two parameters Name and Password will change accordingly 

os.system('echo %s|sudo -S %s' % (sudoPass, command))