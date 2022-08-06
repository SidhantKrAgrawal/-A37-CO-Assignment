import math

space_mem = input("Enter the space in memory : ")
space_mem_list= space_mem.split()

if(space_mem_list[1][-1]=='b'):
    x=1
elif space_mem_list[1][-1]=='B':
    x=8
else:
    x=1
if space_mem_list[1][0].lower()=='k':
    y=2**10
elif space_mem_list[1][0].lower()=='m':
    y=2**20
elif space_mem_list[1][0].lower()=='g':
    y=2**30
else:
    y=1

space=int(space_mem_list[0])*x*y

print()
print("4 TYPES OF MEMORY")
print()
print("1. Bit Addressable Memory - Cell Size = 1 bit")
print("2. Nibble Addressable Memory - Cell Size = 4 bit")
print("3. Byte Addressable Memory - Cell Size = 8 bits(Standard)")
print("4. Word Addressable Memory - Cell Size =  Word Size (depends on CPU)")
print()

type = int(input("How is the memory addressed as mentioned above? "))
if type==1:
    type_mem =1
elif type==2:
    type_mem =4
elif type==3:
    type_mem=8

print()

len_inst = int(input("Enter the length of one instruction in bits: "))
reg_inst = int((input("Enter the length of register in bits: ")))
# reg_inst=7

addr_bits = math.log((space/type_mem),2)
opcode_bits = len_inst-addr_bits-reg_inst
filler_bits = len_inst-opcode_bits-(2*reg_inst)
max_inst = 2**(opcode_bits)
max_reg = 2**(reg_inst)

print("Minimum bits needed to represent an address in this architecture is:",addr_bits)
print("Bits needed by opcode is:",opcode_bits)
print("Filler bits in instruction type 2 is:",filler_bits)
print("Maximum number of instructions this ISA can support:",max_inst)
print("Maximum number of registers this ISA can support:",max_reg)



