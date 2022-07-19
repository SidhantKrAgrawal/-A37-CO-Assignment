from declarations import *
from dictionaries import *


def TypeA():
    pass

def TypeB(reg,imm):
    mapping["PC"]+=1
    
    x=registers[reg]

    mapping[x]=int(imm)

    printing()
    
def TypeC():
    pass

def TypeD():
    pass

def TypeE():
    pass

def TypeF():
    pass
