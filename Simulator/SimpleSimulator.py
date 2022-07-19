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
        
        func_Calling(x,line)



instructions = Input(instrn)


printing()


Running(instrn)

