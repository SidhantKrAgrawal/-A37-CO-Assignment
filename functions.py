
from dictionaries import *

# def DecToBin(num):
#     if num >= 1:
#         Bin=DecToBin(num // 2)
#     else:
#         Bin=""
#     Bin=str(num%2)+Bin
#     return Bin

def DecToBin(num):
    num1=bin(num).replace("0b","")
    str1 = str(num1)
    length=len(str1)
    str2= "0"*(8-length)+str1
    return (str2)

def TypeA(instrn,output):
    Bin=""
    
    Opcode=instrnOpcode[instrn[0]]
    reg = registers[instrn[1]] + registers[instrn[2]] + registers[instrn[3]]

    Bin=Opcode +'00'+reg

    output.append(Bin)

def TypeB(instrn,output):
    Bin = ""

    Opcode=instrnOpcode[instrn[0]]
    reg=registers[instrn[1]]
    number=instrn[2].replace("$","")
    imm = DecToBin(int(number))

    Bin = Opcode + reg + imm

    output.append(Bin)

def TypeC(instrn,output):
    Bin = ""

    Opcode=instrnOpcode[instrn[0]]
    reg=registers[instrn[1]]  + registers[instrn[2]]  

    Bin = Opcode +"00000" +reg

    output.append(Bin)

def TypeD(instrn,output,instructions):
    Bin = ""

    Opcode =instrnOpcode[instrn[0]]
    reg=registers[instrn[1]]
    
   
    mem_addr=DecToBin(variables[instrn[2]]+instructions)
 
    Bin=Opcode+reg+mem_addr

    output.append(Bin)

def TypeE(instrn,output,instructions):
    Bin = ""

    Opcode =instrnOpcode[instrn[0]]

    mem_addr=DecToBin(labels[instrn[1]])

    Bin=Opcode+"000"+mem_addr

    output.append(Bin)

def TypeF(instrn,output):
    Bin=""
    
    Opcode =instrnOpcode[instrn[0]]
    Bin=Opcode+"00000000000"
    
    output.append(Bin)

def mov(instrn,output):
    
    if instrn[2] in registers:
        instrn[0]='movC'
        TypeC(instrn,output)
    else:
        instrn[0]='movB'
        TypeB(instrn,output)