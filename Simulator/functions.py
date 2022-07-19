from declarations import *
from dictionaries import *


def TypeA():
    pass

def TypeB(inst,reg,imm):
    mapping["PC"]+=1
    
    x=registers[reg]
    
    if (inst=="movB"):
        mapping[x]=int(imm,2)
    elif(inst=="rs"):
        mapping[x]=mapping[x]>>int(imm,2)
    elif(inst=="ls"):
        mapping[x]=mapping[x]<<int(imm,2)
    printing()
    
def TypeC():
    pass

def TypeD():
    pass

def TypeE():
    pass

def TypeF():
    pass
