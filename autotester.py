import subprocess
import os

fileC = input("What is the name of your C++ file? ")
subprocess.call(["g++", fileC])

userinput = input("Enter user input file name ")

os.system("./a.out <" + userinput + ">output.txt")

filename = input("What is the file with the answers? ")

f1 = open(filename, "r")
f2 = open("output.txt", "r")

while True:
    line = f1.readline().strip()
    line2 = f2.readline().strip()
    if line2 == '':
        # either end of file or just a blank line.....
        # we'll assume EOF, because we don't have a choice with the while loop!
        break
    if(line2 != line):
        print ("This is incorrect: " + line2)
    else:
        print("Correct")
