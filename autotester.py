import subprocess
import os

subprocess.call(["g++", "quadtreetest.cpp"])

userinput = input("Enter user input file name ")

os.system("./a.out <" + userinput + ">output.txt")

filename = input("What is the file with the answers? ")

Counter = 0.0
lineCounter = 0.0

with open(filename) as f1, open("output.txt") as f2:
    for l1, l2 in zip(f1, f2):
        if l1.strip() != l2.strip():
            print("This is incorrect: " + l2)
        else:
            print("Correct: " + l2)
            Counter += 1
        lineCounter += 1

percentage = str((Counter/lineCounter)*100)
print ("Total Correct: " + percentage + "%")
