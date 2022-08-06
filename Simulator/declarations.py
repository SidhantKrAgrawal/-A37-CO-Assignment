from dictionaries import *
import sys
instrn=[]
memory=["0000000000000000"]*256
# global cycle
xax = []
yax = []

def DecToBin(num,x):
    num1=bin(num).replace("0b","")
    str1 = str(num1)
    length=len(str1)
    str2= "0"*(x-length)+str1
    return (str2)

def printing():
    sys.stdout.write(DecToBin(mapping["PC"],8)+" "+DecToBin(mapping["R0"],16)+" "+DecToBin(mapping["R1"],16)+" "+DecToBin(mapping["R2"],16)+" "+DecToBin(mapping["R3"],16)+" "+DecToBin(mapping["R4"],16)+" "+DecToBin(mapping["R5"],16)+" "+DecToBin(mapping["R6"],16)+" "+DecToBin(mapping["flags"],16))
    sys.stdout.write("\n")