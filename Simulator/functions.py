from declarations import *
from dictionaries import *


def TypeA(inst,reg1,reg2,reg3):
    mapping["PC"]+=1
    x=registers[reg1]
    y=registers[reg2]
    z=registers[reg3]

    if (inst=="add"):
        mapping[z]=mapping[y]+mapping[x]
    elif(inst=="sub"):
        mapping[z]=mapping[x]-mapping[y]
    elif(inst=="mul"):
        mapping[z]=mapping[y]*mapping[x]
    elif(inst=="xor"):
        mapping[z]=mapping[y]^mapping[x]
    elif(inst=="or"):
        mapping[z]=mapping[y]|mapping[x]
    elif(inst=="and"):
        mapping[z]=mapping[y]&mapping[x]
    
    printing()

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
