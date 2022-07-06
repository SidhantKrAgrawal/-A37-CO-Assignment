
from dictionaries import *


def DecToBin(num):
    num1=bin(num).replace("0b","")
    str1 = str(num1)
    length=len(str1)
    str2= "0"*(8-length)+str1
    return (str2)

def TypeA(instrn,output):
    for i in range(1,4):
        if instrn[i] not in registers:
            print("Syntax error: The given input does not have the type of instructon!")
            quit()
    Bin=""

    Opcode=instrnOpcode[instrn[0]]
    reg = registers[instrn[1]] + registers[instrn[2]] + registers[instrn[3]]

    Bin=Opcode +'00'+reg

    output.append(Bin)

def TypeB(instrn,output):
    if instrn[2][0] != "$" and instrn[1][0] == "R":
        TypeC(instrn,output)
    elif instrn[1][0] != "R":
        print("Syntax Error")
        quit()
    else:
        x=int(instrn[-1][1:])
        if x<0 or x>255:
            print('Syntax error: Illegal Immediate values')
            quit()
        
        if instrn[1] not in registers:
            print("Invalid register used")
            quit()
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
    if instrn[2]=="FLAGS":
        if instrn[1] not in registers:
            print("Syntax error: The given input does not have the type of instructon!")
            quit()
        reg=registers[instrn[1]]  + flag[instrn[2]]
    else:
        if instrn[1] not in registers:
            print("Syntax error: The given input does not have the type of instructon!")
            quit()
        if instrn[2] not in registers:
            print("Syntax error: The given input does not have the type of instructon!")
            quit()
        reg=registers[instrn[1]]  + registers[instrn[2]]  

    Bin = Opcode +"00000" +reg

    output.append(Bin)

def TypeD(instrn,output,instructions):
    if instrn[1] not in registers:
        print("Invalid register used")
        quit()    
    Bin = ""

    Opcode =instrnOpcode[instrn[0]]
    reg=registers[instrn[1]]
    if instrn[-1] not in variables:
        print('SytaxError: Misuse of variables')
        quit()
   
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