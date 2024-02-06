#THANKS TO UWUFUFU
'''
Plan: First ask the user if the highest time segment is hours or minutes
'''
print("Is your largest time segment HOURS or MINS?")
getstarted = input()
if(getstarted == "HOURS"):
    while True:
        print("Enter the time in the correct format (HH:MM:SS)")
        oldtime2 = input()
        if any(char.isalpha() for char in oldtime2):
          print("NO LETTERS; Please use correct input format")
        else:
          index1=oldtime2.find(":")
          hours = oldtime2[:index1]
          print(hours)


          getmins = oldtime2[index1+1:]
          index2=getmins.find(":")
          mins = getmins[:index2] 
          print(mins)

          secs = getmins[index2+1:]
          print(secs)
          
          newtime = (int(hours)*3600) + (int(mins)*60) + secs
          print(str(newtime) + " seconds")
          
          
if getstarted=="MINS":
  while True:

    print("Enter the time in the correct format (MM:SS)")
    oldtime = input()
    if any(char.isalpha() for char in oldtime):
        print("NO LETTERS; Please use correct input format")

    else: 
        #print("HORMDCK")
        index=oldtime.find(':')

        if index!=-1:
            og_mins=oldtime[:index]
            newtime= (int(og_mins) * 60) + int(oldtime[index+1:])

            print(str(newtime) + " seconds")