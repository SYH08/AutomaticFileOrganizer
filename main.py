import os
import shutil
import sys
import platform

targetDir = input("Input Target Directory :")
organizedDir = input("Input Organized Directory (Default is {targetDir}/Orgainized) :") ## *

if targetDir == '':
    targetDir = "./target"
if organizedDir == '':
    organizedDir = f"{targetDir}/Organized"

organizedDirName = organizedDir.split("/")
fileExtList = []

try :
    while True:
        dirContent = os.listdir(targetDir)
        if not len(dirContent) == 1 and dirContent[0] != organizedDirName[-1]:
            for i in range(len(dirContent)):
                fileExt = os.path.splitext(dirContent[i])[1].lower()
                print(dirContent[i])
                if fileExt == "":
                    print(f"{dirContent[i]} has no extention.")
                elif fileExt in fileExtList:
                    shutil.move(os.path.join(f"{targetDir}", dirContent[i]),
                                os.path.join(f"{organizedDir}/{fileExt}", dirContent[i]))
                else:
                    fileExtList.append(fileExt)
                    os.mkdir(f"{organizedDir}/{fileExt}")
                    shutil.move(os.path.join(f"{targetDir}", dirContent[i]),
                                os.path.join(f"{organizedDir}/{fileExt}", dirContent[i]))
except Exception as e:
    print(">>>>>>>>>>>>>>>>>>>>>>\n")
    print(f'Error Occurred. {e}.')
    isRestart = input('Restart? (y/n) ')
    print("\n>>>>>>>>>>>>>>>>>>>>>>\n")
    if isRestart == 'y':
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        sys.exit(0)