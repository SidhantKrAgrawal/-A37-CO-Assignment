from dictionaries import *
from functions import *
import sys


instrn=[]
output=[]

def Input(instrn):
    instructions=0
    Flag=True
    count =1
    # lines = sys.stdin.readlines()
    # print(lines)
    while True:
        line = sys.stdin.readline()
        
        if not line:
            break
        line =line.split()
        if len(line)==0:
            continue
        elif line[0]=='var' and Flag==True:
            if line[1] not in variables:
                variables[line[1]]=count
                count+=1
            else:
                sys.stdout.write("ERROR : Declaration of variable multiple times")
                break
        elif line[0]=='var' and Flag==False:
            sys.stdout.write("ERROR: Declaration of variable between the code")
            break

        elif line[0].endswith(":"):
            line[0]=line[0].replace(":","")
            if (line[0]) in variables:
                sys.stdout.write("ERROR: Naming of label and variable is same")
                break
            elif (line[0]) in labels:
                sys.stdout.write("ERROR : Use of label multiple times")
                break
            else:
                labels[line[0]]=instructions
                line=line[1:]
                instrn.append(line)
                instructions+=1
            Flag=False
        else:
            instrn.append(line)
            instructions+=1
            Flag=False
        if line[0]=="hlt":
            break
    return (instructions-1)

def Printing(output):
    for out in output:
        sys.stdout.write(out)
        sys.stdout.write("\n")

def Running(instrn,output,instructions):
    count=0
    for line in instrn:
            if line[0]=='mov':
                mov(line,output,count)
            elif instrnType[line[0]]=='A':
                TypeA(line,output,count)
            elif instrnType[line[0]]=='B':
                TypeB(line,output,count)
            elif instrnType[line[0]]=='C':
                TypeC(line,output,count)
            elif instrnType[line[0]]=='D':
                TypeD(line,output,instructions,count)
            elif instrnType[line[0]]=='E':
                TypeE(line,output,instructions,count)
            elif instrnType[line[0]]=='F':
                TypeF(line,output,count)
            else:
                sys.stdout.write("ERROR: Invalid Instruction syntax")
            count+=1
        
    

   
instructions=Input(instrn)

Running(instrn,output,instructions)

Printing(output)







