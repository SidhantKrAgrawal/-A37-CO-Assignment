from declarations import *
from dictionaries import *
from functions import *

def DecToBin(num,x):
    num1=bin(num).replace("0b","")
    str1 = str(num1)
    length=len(str1)
    str2= "0"*(x-length)+str1
    return (str2)


def Input(instrn):
    instructions=-1
    while True:
        line = input()
        
        if line == '':
            break

        instrn.append(line)
        instructions+=1
        memory[instructions]=line

    return instructions


def func_Calling(arg,r_line):
    match arg:
        case "A":
            return TypeA()
        case "B":
            return TypeB(r_line[5:8],r_line[8:16])
        case "C":
            return TypeC()
        case "D":
            return TypeD()
        case "E":
            return TypeE()
        case "F":
            return TypeF()


def Running(instrn):
    for line in instrn:
        x=instrnType[instrnOpcode[line[:5]]]
        y=line[5:]
        print(func_Calling(x,y)) 

def Output():
    l=len(PC)
    for i in range(l):
        print(DecToBin(PC[i],8)+" "+DecToBin(R0[i],16)+" "+DecToBin(R1[i],16)+" "+DecToBin(R2[i],16)+" "+DecToBin(R3[i],16)+" "+DecToBin(R4[i],16)+" "+DecToBin(R5[i],16)+" "+DecToBin(R6[i],16)+" "+DecToBin(flags[i],16))


instructions = Input(instrn)
Running(instrn)
Output()
