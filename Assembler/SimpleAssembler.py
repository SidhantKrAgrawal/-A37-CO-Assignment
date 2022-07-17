from dictionaries import *
from functions import *


instrn=[]
output=[]

def Input(instrn):
    instructions=0
    Flag=True
    count =1
    while True:
        line = input()
        
        if line == '':
            break
        line =line.split()
        # print(line)
        if line[0]=='var' and Flag==True:
            if line[1] not in variables:
                variables[line[1]]=count
                count+=1
            else:
                print("ERROR : Declaration of variable multiple times")
                break
        elif line[0]=='var' and Flag==False:
            print("ERROR: Declaration of variable between the code")
            break

        elif line[0].endswith(":"):
            line[0]=line[0].replace(":","")
            if (line[0]) in variables:
                print("ERROR: Naming of label and variable is same")
                break
            elif (line[0]) in labels:
                print("ERROR : Use of label multiple times")
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
        print(out)

def Running(instrn,output,instructions):
    for line in instrn:
            if line[0]=='mov':
                mov(line,output)
            elif instrnType[line[0]]=='A':
                TypeA(line,output)
            elif instrnType[line[0]]=='B':
                TypeB(line,output)
            elif instrnType[line[0]]=='C':
                TypeC(line,output)
            elif instrnType[line[0]]=='D':
                TypeD(line,output,instructions)
            elif instrnType[line[0]]=='E':
                TypeE(line,output,instructions)
            elif instrnType[line[0]]=='F':
                TypeF(line,output)
            else:
                print("ERROR: Invalid Instruction syntax")
       
        
    

try:       

    instructions=Input(instrn)

    Running(instrn,output,instructions)

    Printing(output)

except Exception as e:
    print("ERROR in: ",e)




