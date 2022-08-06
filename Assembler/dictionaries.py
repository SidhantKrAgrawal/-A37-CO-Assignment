instrnOpcode={"add":"10000" , "sub":"10001" , "movB":"10010","movC":"10011", "ld":"10100" , "st":"10101" , "mul":"10110" , "div":"10111" , "rs":"11000" ,"ls":"11001" ,"xor":"11010" ,"or":"11011","and":"11100" , "not":"11101" ,"cmp":"11110" ,"jmp":"11111" ,"jlt":"01100" ,"jgt":"01101" ,"je":"01111" ,"hlt":"01010","addf":"00000","subf":"00001","movf":"00010"}

instrnType = {"add":"A" , "sub":"A", "ld":"D" , "st":"D" , "mul":"A" , "div":"C" , "rs":"B" ,"ls":"B" ,"xor":"A" ,"or":"A","and":"A" , "not":"C" ,"cmp":"C" ,"jmp":"E" ,"jlt":"E" ,"jgt":"E" ,"je":"E" ,"hlt":"F","addf":"A","subf":"A","movf":"B"}

variables ={ }

labels ={ }

registers = {
    'R0' : '000',
    'R1' : '001',
    'R2' : '010',
    'R3' : '011',
    'R4' : '100',
    'R5' : '101',
    'R6' : '110',
}

flag = {
    'FLAGS' : '111'
}