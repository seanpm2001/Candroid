# Start of script
def apiLevel_guide():
  	print ("Android API level guide")
	print ("Android 1.0 (API Level: 1)")
	print ("Android 1.1 (API Level: 2)")
	print ("Android 1.5 Cupcake (API Level: 3)")
	print ("Android 1.6 Donut (API Level: 4)")
	print ("Android 2.0 Eclair (API Level: 5)")
	print ("Android 2.2 Froyo (API Level: 8)")
	print ("Android 2.3 Gingerbread (API Level: 9)")
	print ("Android 3.0 Honeycomb (API Level: 11)")
	print ("Android 4.0 Ice Cream Sandwich (API Level: 14)")
	print ("Android 4.1 Jelly Bean (API Level: 16)")
 	print ("Android 4.4 KitKat (API Level: 19)")
 	print ("Android 5.0 Lollipop (API Level: 21)")
 	print ("Android 6.0 Marshmallow (API Level: 23)")
	print ("Android 7.0 Nougat (API Level: 24)")
	print ("Android 8.0 Oreo (API Level: 26)")
	print ("Android 9 Pie (API Level: 28)")
	print ("Android 10 (API Level: 29)")
	print ("Android 11 (API Level: 30)")
def apiLevel_parameters():
  minAPILvl = int(1)
  maxAPILvl = int(30)
  currentAPILvl = int(9)
  # API Level identifier (string for the Android version tied to the API level)
  currentAPILvlIdentifier = str("Undefined")
  if (currentAPILvl == 1):
    currentAPILvlIdentifier == str("Android 1.0")
  if (currentAPILvl == 2):
    currentAPILvlIdentifier == str("Android 1.1")
  if (currentAPILvl == 3):
    currentAPILvlIdentifier == str("Android 1.5 (cupcake)")
  if (currentAPILvl == 4):
    currentAPILvlIdentifier == str("Android 1.6 (Donut)")
  if (currentAPILvl == [5, 7]): # This syntax needs to be checked
    currentAPILvlIdentiier == str("Android 2.x (Eclair)")
  if (currentAPILvl == 8):
    currentAPILvlIdentiier == str("Android 2.2 (Froyo)")
  if (currentAPILvl == [9, 10]): # This syntax needs to be checked
    currentAPILvlIdentiier == str("Android 2.3 (Gingerbread)")
  if (currentAPILvl == [11, 13]): # This syntax needs to be checked
    currentAPILvlIdentiier == str("Android 3.0 (Honeycomb)")
  if (currentAPILvl == [14, 15]): # This syntax needs to be checked
    currentAPILvlIdentiier == str("Android 4.0 (Ice Cream Sandwich)")
  if (currentAPILvl == [16, 18]): # This syntax needs to be checked
    currentAPILvlIdentiier == str("Android 4.1 (Jelly Bean)")
  if (currentAPILvl == [19, 20]): # This syntax needs to be checked
    currentAPILvlIdentiier == str("Android 4.4 (KitKat)")
  if (currentAPILvl == [21, 22]): # This syntax needs to be checked
    currentAPILvlIdentiier == str("Android 5.0 (Lollipop)")
  if (currentAPILvl == 23): # This syntax needs to be checked
    currentAPILvlIdentiier == str("Android 6.0 (Marshmallow)")
  if (currentAPILvl == [24, 25]): # This syntax needs to be checked
    currentAPILvlIdentiier == str("Android 7.0 (Nougat)")
  if (currentAPILvl == [26, 27]): # This syntax needs to be checked
    currentAPILvlIdentiier == str("Android 8.0 (Oreo)")
  if (currentAPILvl == 28):
    currentAPILvlIdentiier == str("Android 9.0 (Pie)")
  if (currentAPILvl == 29):
    currentAPILvlIdentiier == str("Android 10.0")
  if (currentAPILvl == 30):
    currentAPILvlIdentiier == str("Android 11.0")
# TOP - Output starts here
print ("Compatibility settings > API Level")
print ("Change the API level for Android programs")
print (apiLevel_guide())
return (apiLevel_parameters()) # Return but don't print/output
startProgramIfTrue = input("Do you want to change the API level for Android? (y/N)")
startProgramIfTrue == startProgramIfTrue.upper()
if (startProgramIfTrue == "Y"):
  print ("Change the API level for Android programs")
  print ("The current API level is " + str(currentAPILvl) + " | " + str(currentAPILvlIdentifier))
  apiChangeLvl = int(input("Enter a new API level (minimum: 1 | maximum: 30)")
  try:
    apiChangeLvl = int(number)
  except ValueError:
    print("ERROR: You must enter a valid number. Strings are not allowed here.")
  # Check API level
  if (apiChangeLvl > 0 & apiChangeLvl < 31): # I forgot how to do statements with 2 checks. I don't think this is valid syntax. I don't have a good python interpreter at the moment, so I am just going to leave this here.
    currentAPILvl == apiChangeLvl
    print ("The API level has been changed to " + str(currentAPILvl))
    print ("Programs are now in " + str(currentAPILvlIdentifier) + " compatibility mode")
    continue1 = input("Press [ENTER] key to continue")
elif (startProgramIfTrue == "N"):
  print ("API level settings remain unchanged")
else:
  print ("API level settings have passed.")
noMore = input("Press [ENTER] key to quit")
print ("The program should now be closed. If the program is still running, try closing the window. If that doesn't work, kill the program with a task/resource manager")
"""
File info
File version: 1 (Sunday, January 17th 2021 at 3:19 pm)
File type: Python 3 source file (*.py)
Line count (including blank lines and compiler line): 98
"""
# End of script
