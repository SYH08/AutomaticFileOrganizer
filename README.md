# Automatic File Organizer
## Overview

This project is for Computer and Information Class's Subject Detail Report

(Subject Detail Report is a portion of School Life Detail Report in S.Korea.)

## Algorithm

1. Enter path of target directory and directory for organized files(Organized Directory)
2. Check if input(in 1) is empty or not and follow these steps:
	1. If the input is empty, ```targetDir``` has a default value of ```"./target"```.
	2. If the input is empty, ```organizedDir``` has a default value of ```"{targetDir}/Organized"```.
3. To prevent cases which the Organized directory is included in target direcotry, separate Folder name form path.(```split```)
4. Import contents of target directory in type of list.
5. To prevent case of process 3, If target directory has 1 content and it's name is Folder name(Process 3), returns to the loop without executing the content below.
6. Repeat the following as the length of the directory contents list.
	1. Import the file extension into ```fileExt```, convert it to lowercase, and save it.
	2. To skip files without an extension, if the extension is ```""```, display the file name in the console and move on.
	3. If there is a ```fileExt``` in ```fileExtList```, move it to the path ```"{organizedDir}/{fileExt}"```.
	4. If there is no ```fileExt``` in ```fileExtList```, add ```fileExt```, create a folder with that name in the organization directory, and then move the file.
7. If an error occurs during step 6, follow the steps below.
	1. Prints an error message (```{e}```)
	2. It asks whether to restart and follows the other procedure. (```isRestart```)
		1. If ```isRestart``` is ```y```, the console is cleared and restarted according to the OS type.
		2. If ```isRestart``` is ```n```, it terminates.




Since I'm from S.Korea, Sorry for my bad grammar.



ひかる。