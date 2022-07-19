from declarations import *
from dictionaries import *

def reg_Calling(arg):
    match arg:
        case "R0":
            return R0.append(mapping[arg])
        case "R1":
            return R1.append(mapping[arg])
        case "R2":
            return R2.append(mapping[arg])
        case "R3":
            return R3.append(mapping[arg])
        case "R4":
            return R4.append(mapping[arg])
        case "R5":
            return R5.append(mapping[arg])
        case "R6":
            return R6.append(mapping[arg])
        case "flags":
            return flags.append(mapping[arg])

def TypeA():
    pass

def TypeB(reg,imm):
    mapping["PC"]+=1
    PC.append(mapping["PC"])

    x=registers[reg]

    mapping[x]=int(imm)
    
    reg_Calling(x)

def TypeC():
    pass

def TypeD():
    pass

def TypeE():
    pass

def TypeF():
    pass
