
from declarations import *
from dictionaries import *


def TypeA(inst,reg1,reg2,reg3):
    
    xax.append(mapping["cycle"])
    yax.append(mapping["PC"])
    mapping["cycle"]+=1

    mapping["flags"]=0
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
    mapping["PC"]+=1
    return 0

def TypeB(inst,reg,imm):
    
    xax.append(mapping["cycle"])
    # print(xax)
    yax.append(mapping["PC"])

    mapping["cycle"]=mapping["cycle"] + 1

    mapping["flags"]=0
    x=registers[reg]
    
    if (inst=="movB"):
        mapping[x]=int(imm,2)
    elif(inst=="rs"):
        mapping[x]=mapping[x]>>int(imm,2)
    elif(inst=="ls"):
        mapping[x]=mapping[x]<<int(imm,2)
    printing()
    mapping["PC"]+=1
    return 0

def TypeC(inst,reg1,reg2):
    
    xax.append(mapping["cycle"])
    yax.append(mapping["PC"])
    mapping["cycle"]+=1

    mapping["flags"]=0
    x=registers[reg1]
    y=registers[reg2]

    if(inst=="movC"):
        mapping[y]=mapping[x]
    elif(inst=="div"):
        pass              # Doubt
    elif(inst=="not"):
        mapping[y]= ~mapping[x]
    elif(inst=="cmp"):
        if mapping[x]<mapping[y]:
            mapping["flags"]=4
        elif mapping[x]>mapping[y]:
            mapping["flags"]=2
        elif mapping[x]==mapping[y]:
            mapping["flags"]=1

    printing()
    mapping["PC"]+=1
    return 0

def TypeD(inst,reg1,mem_addr):
    
    xax.append(mapping["cycle"])
    yax.append(mapping["PC"])
    

    mapping["flags"]=0
    x=registers[reg1]
    
    if(inst=="ld"):
        mem=int(mem_addr,2)
        mapping[x]=int(memory[mem],2)
    elif(inst=='st'):
        mem=int(mem_addr,2)
        memory[mem]=str(DecToBin(mapping[x],16))

    xax.append(mapping["cycle"])
    yax.append(mem)
    mapping["cycle"]+=1

    printing()
    mapping["PC"]+=1
    return 0

def TypeE(inst,mem_addr):
    
    xax.append(mapping["cycle"])
    yax.append(mapping["PC"])
    mapping["cycle"]+=1

    printing()
    if(inst=='jmp'):
        mem=int(mem_addr,2)
        mapping["PC"]=mem
    elif(inst=='jlt'):
        if(mapping["flags"]==4):
            mem=int(mem_addr,2)
            mapping["PC"]=mem
        else:
            mapping["PC"]+=1
    elif(inst=='jgt'):
        if(mapping["flags"]==2):
            mem=int(mem_addr,2)
            mapping["PC"]=mem
        else:
            mapping["PC"]+=1
    elif(inst=='je'):
        if(mapping["flags"]==1):
            mem=int(mem_addr,2)
            mapping["PC"]=mem
        else:
            mapping["PC"]+=1

    
    mapping["flags"]=0
    return 0

def TypeF(inst):
    printing()
    for i in memory:
        sys.stdout.write(i)
        sys.stdout.write("\n")
    return 1

