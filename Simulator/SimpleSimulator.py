from declarations import *
from dictionaries import *
from functions import *
import matplotlib.pyplot as plt

def Input(instrn):
    instructions=-1
    # lines = sys.stdin.readlines()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        if line=="\n":
            break
        # print(line)
        line = line[:-1]
        instrn.append(line)
        instructions+=1
        memory[instructions]=str(line)
        if line == '0101000000000000':
            break
    return instructions


def func_Calling(arg,r_line,inst):

    if arg=='A':
        return TypeA(inst,r_line[7:10],r_line[10:13],r_line[13:16])
    elif arg=='B':
        return TypeB(inst,r_line[5:8],r_line[8:16])
    elif arg=='C':
        return TypeC(inst,r_line[10:13],r_line[13:16])
    elif arg=='D':
        return TypeD(inst,r_line[5:8],r_line[8:16])
    elif arg=='E':
        return TypeE(inst,r_line[8:16])
    elif arg=='F':
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


plt.scatter(xax,yax,c="blue")
plt.show()
