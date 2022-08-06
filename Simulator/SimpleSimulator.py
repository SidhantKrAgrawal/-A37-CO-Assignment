from declarations import *
from dictionaries import *
from functions import *


def Input(instrn):
    instructions=-1
    while True:
        line = input()
        
        if line == '':
            break

        instrn.append(line)
        instructions+=1
        memory[instructions]=str(line)

    return instructions


def func_Calling(arg,r_line,inst):
    match arg:
        case "A":
            return TypeA(inst,r_line[7:10],r_line[10:13],r_line[13:16])
        case "B":           
            return TypeB(inst,r_line[5:8],r_line[8:16])
        case "C":
            return TypeC(inst,r_line[10:13],r_line[13:16])
        case "D":
            return TypeD(inst,r_line[5:8],r_line[8:16])
        case "E":
            return TypeE(inst,r_line[8:16])
        case "F":
            return TypeF(inst)


def Running(instrn):

    while(True):
        line=instrn[mapping['PC']]
        y=instrnOpcode[line[:5]]
        x=instrnType[y]
        
        h=func_Calling(x,line,y)

        if h==1:
            break


instructions = Input(instrn)


Running(instrn)

