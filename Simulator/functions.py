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

    return 0

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
    
    return 0

def TypeC(inst,reg1,reg2):
    mapping["PC"]+=1

    x=registers[reg1]
    y=registers[reg2]

    if(inst=="movC"):
        pass
    elif(inst=="div"):
        pass
    elif(inst=="not"):
        pass
    elif(inst=="cmp"):
        if(mapping[x]<mapping[y]):
            mapping["flags"]=4
        pass

    printing()
    return 0

def TypeD(inst,reg1,mem_addr):
    mapping["PC"]+=1

    x=registers[reg1]

    if(inst=="ld"):
        mem=int(mem_addr,2)
        mapping[x]=int(memory[mem],2)
    
    printing()
    return 0

def TypeE(inst,mem_addr):
    pass

def TypeF(inst):
    pass
