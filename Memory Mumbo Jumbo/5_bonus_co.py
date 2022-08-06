
import math

Dict = {'Bit addressable memory' : 2**0 ,'Nibble addressable memory' : 2**2, 'Byte addressable memory' : 2**3} 


def type1():
    instruction_length=int(input("Enter your Instruction Length: "))
    register_length=int(input("Enter Register Length: "))



    print("Enter your initial input:")
    input_mem=input("Input Memory Space: ")

    mem_unit = {"KB" : 2**10 , "MB" : 2**20 , "GB" : 2**30}
    input_mem=input_mem.split()
    bits=int(input_mem[0])*(2**10)                      
    x = math.log(bits) / math.log(2)                  

    print()
    print("1.Bit addressable memory")
    print("2.Byte addressable memory")
    print("3.Nibble addressable memory")
    print("4.Word addressable memory ")
    print()
    address_type=input("Enter Address Type option: ")
    if(address_type=="2"):
        address_pins=2**x/Dict["Byte addressable memory"]                        
        y=math.log(address_pins)/math.log(2)          

    elif(address_type=="3"):
        address_pins=2**x/Dict["Nibble addressable memory"] 
        y=math.log(address_pins)/math.log(2)

    elif(address_type=="1"):
        address_pins=2**x/2**1
        y=math.log(address_pins)/math.log(2)

    elif(address_type=="4"):
        address_pins=2**x/2**4
        y=math.log(address_pins)/math.log(2)




    print()
    print("The minimum bits needed for architecture: ", y)
    print("The number of bits need by opcode: ",instruction_length - y - register_length)
    print("The number of filler bits in Instruction type 2: ",instruction_length - (instruction_length - y - register_length) - register_length)
    print("Maximum numbers of instructions this ISA can support: ",2**(instruction_length-y-register_length))
    print("Maximum number of registers this ISA can support: ",2**register_length)
    print()

    print("Enter current input: ")
    bitCPU=int(input("Enter the number bits in CPU: "))
    print()
    print("1.Bit addressable memory")
    print("2.Byte addressable memory")
    print("3.Nibble addressable memory")
    print("4.Word addressable memory: ")
    print()
    address_type2=input("Enter the enhanced address type option: ")
    if(address_type2=="4"):
        g=math.log(bitCPU)/math.log(2)
        print()
        new_pins=2**x/2**g                  

    elif(address_type2=='2'):
        print()
        new_pins=2**x/Dict["Byte addressable memory"]

    elif(address_type2=='1'):
        print()
        new_pins=2**x/2

    elif(address_type2=='3'):
        print()
        new_pins=2**x/Dict["Nibble addressable memory"]

    z=math.log(new_pins)/math.log(2)                       
    output=y-z                                             
    if(y>z):
        print("Number of pins saved: -",int(output))

    else:
        print("Number of pins required: +",int(output))

    print()
    
    
def type2():
    
    print()
    bitCPU = input("Enter the number bits in CPU: ")
    bitCPU = bitCPU.split()
    address_pins = input("Enter the number of address pins: ") 
    address_pins = address_pins.split()
    print()
    print("1.Bit addressable memory")
    print("2.Byte addressable memory")
    print("3.Nibble addressable memory")
    print("4.Word addressable memory")
    print()
    address_memory = input("Enter the type of addressable memory: ") 

    number_address = 2**int(address_pins[0])  

    if(address_memory in Dict):
        a = number_address/8             
        b = a/1024                      
        b = b/1024                         
        b = b/1024                       

        print()
        final_output = Dict[address_memory]*b
        print("The size of main memory is: ",int(final_output),'GB')

    elif(address_memory == "Word addressable memory"):
        a = number_address/8             
        b = a/1024                      
        b = b/1024                        
        b = b/1024                       

        print()
        final_output = b*int(bitCPU[0])
        print("The size of main memory is: ",int(final_output),"GB")



    
    

x = int(input("Enter which Type(1/2):"))
    
if(x==1):
    type1()
elif(x==2):
    type2()
