#!/usr/bin/python3

print("content-type:text/html\n")

import cgi
import subprocess

form=cgi.FieldStorage()
cmd=form.getvalue("c")

if "date" in cmd:
  print(subprocess.getoutput('date'))
elif (("ip" in cmd) or ("address" in cmd) or ("configuration" in cmd) or ("ifconfig" in cmd)):
  print(subprocess.getoutput('ifconfig'))
elif (("name" in cmd) or ("log" in cmd) or ("logged" in cmd) or ("whoami" in cmd)):
  print(subprocess.getoutput('whoami'))
elif (("directory" in cmd) or ("work" in cmd) or ("working" in cmd) or ("pwd" in cmd)):
  print(subprocess.getoutput('pwd'))
elif (("calendar" in cmd) or ("cal" in cmd)):
  print(subprocess.getoutput('cmd'))
else:
  print("Hello user! Try again with the following basic linux commands </br>")
  print("1. pwd : Shows the current working directory </br>")
  print("2. whoami : Shows the name by which you are currently logged in </br>")
  print("3. date : Displays today's date </br>")
  print("4. cal : Displays calendar </br>")
  print("5. ifconfig : Shows ip-configuration </br>")
