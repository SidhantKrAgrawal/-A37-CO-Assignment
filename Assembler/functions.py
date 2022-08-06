
from dictionaries import *
import sys

def DecToBin(num):
    num1=bin(num).replace("0b","")
    str1 = str(num1)
    length=len(str1)
    str2= "0"*(8-length)+str1
    return (str2)

def TypeA(instrn,output,count):
    if len(instrn) != 4:
        sys.stdout.write("SyntaxError: Not all required paramters provided for Type A command in line no: "+str(count))
        quit()
    for i in range(1,4):
        if instrn[i] not in registers:
            sys.stdout.write("Syntax error: The given input does not have the type of instructon! in line no: "+str(count))
            quit()
    Bin=""

    Opcode=instrnOpcode[instrn[0]]
    reg = registers[instrn[1]] + registers[instrn[2]] + registers[instrn[3]]

    Bin=Opcode +'00'+reg

    output.append(Bin)

def TypeB(instrn,output,count):
    if len(instrn) != 3:
        sys.stdout.write("SyntaxError: Not all required paramters provided for Type B command in line no: "+str(count))
        quit()
    if instrn[2][0] != "$" and instrn[1][0] == "R":
        TypeC(instrn,output)
    elif instrn[1][0] != "R":
        sys.stdout.write("Syntax Error in line no: "+str(count))
        quit()
    else:
        x=int(instrn[-1][1:])
        if x<0 or x>255:
            sys.stdout.write("Syntax error: Illegal Immediate values in line no: "+str(count))
            quit()
        
        if instrn[1] not in registers:
            sys.stdout.write("Invalid register used in line no: "+str(count))
            quit()
    Bin = ""

    Opcode=instrnOpcode[instrn[0]]
    reg=registers[instrn[1]]
    number=instrn[2].replace("$","")
    imm = DecToBin(int(number))

    Bin = Opcode + reg + imm

    output.append(Bin)

def TypeC(instrn,output,count):
    if len(instrn) != 3:
        sys.stdout.write("SyntaxError: Not all required paramters provided for Type C command in line no: "+str(count))
        quit()
    Bin = ""

    Opcode=instrnOpcode[instrn[0]]
    if instrn[1]=="FLAGS":
        if instrn[2] not in registers:
            sys.stdout.write("Syntax error: The given input does not have the type of instructon!  in line no: "+str(count))
            quit()
        reg=flag[instrn[1]] + registers[instrn[2]]  
    else:
        if instrn[1] not in registers:
            sys.stdout.write("Syntax error: The given input does not have the type of instructon! in line no: "+str(count))
            quit()
        if instrn[2] not in registers:
            sys.stdout.write("Syntax error: The given input does not have the type of instructon! in line no: "+str(count))
            quit()
        reg=registers[instrn[1]]  + registers[instrn[2]]  

    Bin = Opcode +"00000" +reg

    output.append(Bin)

def TypeD(instrn,output,instructions,count):
    if len(instrn)!=3:
        sys.stdout.write("SyntaxError: Not all required parametrs provided for Type D command in line no: "+str(count))
        quit()
    if instrn[1] not in registers:
        sys.stdout.write("Invalid register used in line no: "+str(count))
        quit()    
    Bin = ""

    Opcode =instrnOpcode[instrn[0]]
    reg=registers[instrn[1]]
    if instrn[-1] not in variables:
        sys.stdout.write("SytaxError: Misuse of variables in line no: "+str(count))
        quit()
   
    mem_addr=DecToBin(variables[instrn[2]]+instructions)
 
    Bin=Opcode+reg+mem_addr

    output.append(Bin)

def TypeE(instrn,output,instructions,count):
    if len(instrn)!=2:
        sys.stdout.write("SyntaxError : Wrong syntax used for instructions in line no: "+str(count))
    Bin = ""

    Opcode =instrnOpcode[instrn[0]]
    if instrn[1] in labels:
        mem_addr=DecToBin(labels[instrn[1]])
    elif instrn[1] in variables:
        mem_addr=DecToBin(variables[instrn[1]]+instructions)
    else:
        sys.stdout.write("ERROR: Memory address of Type E not defined in line no: "+str(count))

    Bin=Opcode+"000"+mem_addr

    output.append(Bin)

def TypeF(instrn,output,count):
    Bin=""
    
    Opcode =instrnOpcode[instrn[0]]
    Bin=Opcode+"00000000000"
    
    output.append(Bin)

def mov(instrn,output,count):
    
    if instrn[2] in registers:
        instrn[0]='movC'
        TypeC(instrn,output,count)
    else:
        instrn[0]='movB'
        TypeB(instrn,output,count)