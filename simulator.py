import ctypes
import sys

global r0
global r1
global r2
global r3
global r4
global r5
global r6

addr0="000"
addr1="001"
addr2="010"
addr3="011"
addr4="100"
addr5="101"
addr6="110"
flag=0
addrflag="111"
stdout=open("OUTPUT.txt","w")



def lenbal(string,bit):
    string.reverse()
    while(len(string)!=bit):
        string.append("0")
    string.reverse()
    charstr=""
    for i in string:
        charstr=charstr+str(i)
    return charstr
        


def conv_binary(decimal):
    list1=[]
    factorial=2
    while decimal//factorial!=0:
        list1.append(decimal%factorial)
        decimal=decimal//2
    list1.append(decimal%2)
    list1.reverse()
    return list1

def binary_to_decimal(binary):
    decimal = 0
    binary=binary[::-1]
    for i in range(len(binary)):
        decimal +=int( binary[i]) * (2 ** i)
    return str(decimal)


def addlist(l1,l2):
    num1=binary_to_decimal(l1)
    num2=binary_to_decimal(l2)
    reg3=num1+num2
    reg3=conv_binary(reg3)
    return reg3

def addition(reg1, reg2, reg3):
    global r0, r1, r2, r3, r4, r5, r6, flag

    registers = {"R0": (r0, addr0), "R1": (r1, addr1), "R2": (r2, addr2), 
                 "R3": (r3, addr3), "R4": (r4, addr4), "R5": (r5, addr5), 
                 "R6": (r6, addr6)}

    listused = [[0, 0], [0, 0], [0, 0]]

    for i in range(3):
        if reg1 == list(registers.keys())[i]:
            listused[0][0] = list(registers.values())[i][0]
            listused[0][1] = list(registers.values())[i][1]

        if reg2 == list(registers.keys())[i]:
            listused[1][0] = list(registers.values())[i][0]
            listused[1][1] = list(registers.values())[i][1]

        if reg3 == list(registers.keys())[i]:
            listused[2][0] = list(registers.values())[i][0]
            listused[2][1] = list(registers.values())[i][1]

    total = listused[1][0] + listused[2][0]

    if total > 65535:
        flag = 8
        listb = conv_binary(total)
        listb.reverse()
        while len(listb) != 16:
            listb.pop()
        listb.reverse()
        total = int(binary_to_decimal(listb))

    if listused[0][0] == r0:
        r0 = total
    if listused[0][0] == r1:
        r1 = total
    if listused[0][0] == r2:
        r2 = total
    if listused[0][0] == r3:
        r3 = total
    if listused[0][0] == r4:
        r4 = total
    if listused[0][0] == r5:
        r5 = total
    if listused[0][0] == r6:
        r6 = total


def subtraction(reg1, reg2, reg3):
    global r0, r1, r2, r3, r4, r5, r6, flag

    registers = {"R0": (r0, addr0), "R1": (r1, addr1), "R2": (r2, addr2), 
                 "R3": (r3, addr3), "R4": (r4, addr4), "R5": (r5, addr5), 
                 "R6": (r6, addr6)}

    listused = [[0, 0], [0, 0], [0, 0]]

    for i in range(3):
        if reg1 == list(registers.keys())[i]:
            listused[0][0] = list(registers.values())[i][0]
            listused[0][1] = list(registers.values())[i][1]

        if reg2 == list(registers.keys())[i]:
            listused[1][0] = list(registers.values())[i][0]
            listused[1][1] = list(registers.values())[i][1]

        if reg3 == list(registers.keys())[i]:
            listused[2][0] = list(registers.values())[i][0]
            listused[2][1] = list(registers.values())[i][1]

    total = listused[1][0] - listused[2][0]

    if total < 0:
        flag = 8
        total = 0

    if listused[0][0] == r0:
        r0 = total
    if listused[0][0] == r1:
        r1 = total
    if listused[0][0] == r2:
        r2 = total
    if listused[0][0] == r3:
        r3 = total
    if listused[0][0] == r4:
        r4 = total
    if listused[0][0] == r5:
        r5 = total
    if listused[0][0] == r6:
        r6 = total


def multiply(reg1, reg2, reg3):
    global r0, r1, r2, r3, r4, r5, r6, flag

    registers = {"R0": (r0, addr0), "R1": (r1, addr1), "R2": (r2, addr2), 
                 "R3": (r3, addr3), "R4": (r4, addr4), "R5": (r5, addr5), 
                 "R6": (r6, addr6)}

    listused = [[0, 0], [0, 0], [0, 0]]

    for i in range(3):
        if reg1 == list(registers.keys())[i]:
            listused[0][0] = list(registers.values())[i][0]
            listused[0][1] = list(registers.values())[i][1]

        if reg2 == list(registers.keys())[i]:
            listused[1][0] = list(registers.values())[i][0]
            listused[1][1] = list(registers.values())[i][1]

        if reg3 == list(registers.keys())[i]:
            listused[2][0] = list(registers.values())[i][0]
            listused[2][1] = list(registers.values())[i][1]

    total = listused[1][0] * listused[2][0]

    if total > 65535:
        flag = 8
        listb = conv_binary(total)
        listb.reverse()
        while len(listb) != 16:
            listb.pop()
        listb.reverse()
        total = int(binary_to_decimal(listb))

    if listused[0][0] == r0:
        r0 = total
    if listused[0][0] == r1:
        r1 = total
    if listused[0][0] == r2:
        r2 = total
    if listused[0][0] == r3:
        r3 = total
    if listused[0][0] == r4:
        r4 = total
    if listused[0][0] == r5:
        r5 = total
    if listused[0][0] == r6:
        r6 = total


def divide(reg1, reg2):
    global r0, r1, r2, r3, r4, r5, r6, flag

    registers = {"R0": (r0, addr0), "R1": (r1, addr1), "R2": (r2, addr2), 
                 "R3": (r3, addr3), "R4": (r4, addr4), "R5": (r5, addr5), 
                 "R6": (r6, addr6)}

    listused = [[0, 0], [0, 0]]

    for i in range(2):
        if reg1 == list(registers.keys())[i]:
            listused[0][0] = list(registers.values())[i][0]
            listused[0][1] = list(registers.values())[i][1]

        if reg2 == list(registers.keys())[i]:
            listused[1][0] = list(registers.values())[i][0]
            listused[1][1] = list(registers.values())[i][1]

    if listused[1][0] == 0:
        flag = 8
        r0 = 0
        r1 = 0
        return 0

    temp = listused[0][0] // listused[1][0]
    tempr = listused[0][0] % listused[1][0]
    r0 = temp
    r1 = tempr


def Exclusive_OR(reg1, reg2, reg3):
    global r0, r1, r2, r3, r4, r5, r6, flag

    registers = {"R0": r0, "R1": r1, "R2": r2, "R3": r3, "R4": r4, "R5": r5, "R6": r6}
    addresses = {"R0": addr0, "R1": addr1, "R2": addr2, "R3": addr3, "R4": addr4, "R5": addr5, "R6": addr6}

    listused = [[0, 0], [0, 0], [0, 0]]

    for i, reg in enumerate([reg1, reg2, reg3]):
        if reg in registers:
            listused[i][0] = registers[reg]
            listused[i][1] = addresses[reg]
        else:
            exit()

    for reg_index in range(7):
        if listused[0][1] == globals()[f"r{reg_index}"]:
            globals()[f"r{reg_index}"] = listused[2][0] ^ listused[2][1]


def OR(reg1, reg2, reg3):
    global r0, r1, r2, r3, r4, r5, r6, flag

    registers = {"R0": r0, "R1": r1, "R2": r2, "R3": r3, "R4": r4, "R5": r5, "R6": r6}
    addresses = {"R0": addr0, "R1": addr1, "R2": addr2, "R3": addr3, "R4": addr4, "R5": addr5, "R6": addr6}

    listused = [[0, 0], [0, 0], [0, 0]]

    for i, reg in enumerate([reg1, reg2, reg3]):
        if reg in registers:
            listused[i][0] = registers[reg]
            listused[i][1] = addresses[reg]
        else:
            exit()

    for reg_index in range(7):
        if listused[0][1] == globals()[f"r{reg_index}"]:
            globals()[f"r{reg_index}"] = listused[2][0] | listused[2][1]


def AND(reg1, reg2, reg3):
    global r0, r1, r2, r3, r4, r5, r6, flag

    registers = {"R0": r0, "R1": r1, "R2": r2, "R3": r3, "R4": r4, "R5": r5, "R6": r6}
    addresses = {"R0": addr0, "R1": addr1, "R2": addr2, "R3": addr3, "R4": addr4, "R5": addr5, "R6": addr6}

    listused = [[0, 0], [0, 0], [0, 0]]

    for i, reg in enumerate([reg1, reg2, reg3]):
        if reg in registers:
            listused[i][0] = registers[reg]
            listused[i][1] = addresses[reg]
        else:
            exit()

    for reg_index in range(7):
        if listused[0][1] == globals()[f"r{reg_index}"]:
            globals()[f"r{reg_index}"] = listused[2][0] & listused[2][1]


def MoveImmediate(reg, imm, areg):
    global r0, r1, r2, r3, r4, r5, r6, flag

    if reg in globals():
        globals()[reg] = imm


def Right_Shift(reg, imm, areg):
    global r0, r1, r2, r3, r4, r5, r6, flag

    if reg in globals():
        shifted_value = globals()[reg] >> imm
        if shifted_value > 65535:
            listb = conv_binary(shifted_value)
            listb.reverse()
            while len(listb) != 16:
                listb.pop()
            listb.reverse()
            globals()[reg] = int(binary_to_decimal(listb))
        else:
            globals()[reg] = shifted_value

def Left_Shift(reg, imm, areg):
    global r0, r1, r2, r3, r4, r5, r6, flag

    if reg in globals():
        globals()[reg] = globals()[reg] << imm


def MoveRegister(reg1, reg2):
    global r0, r1, r2, r3, r4, r5, r6

    registers = {"R0": r0, "R1": r1, "R2": r2, "R3": r3, "R4": r4, "R5": r5, "R6": r6}
    addresses = {"R0": addr0, "R1": addr1, "R2": addr2, "R3": addr3, "R4": addr4, "R5": addr5, "R6": addr6, "FLAGS": addrflag}

    listused = [[0, 0], [0, 0]]

    for i, reg in enumerate([reg1, reg2]):
        if reg in registers:
            listused[i][0] = registers[reg]
            listused[i][1] = addresses[reg]
        else:
            exit()

    for reg_index in range(7):
        if listused[0][0] == globals()[f"r{reg_index}"]:
            globals()[f"r{reg_index}"] = listused[1][0]


def Compare(reg1, reg2):
    global r0, r1, r2, r3, r4, r5, r6, flag

    registers = {"R0": r0, "R1": r1, "R2": r2, "R3": r3, "R4": r4, "R5": r5, "R6": r6}
    addresses = {"R0": addr0, "R1": addr1, "R2": addr2, "R3": addr3, "R4": addr4, "R5": addr5, "R6": addr6}

    listused = [[0, 0], [0, 0]]

    for i, reg in enumerate([reg1, reg2]):
        if reg in registers:
            listused[i][0] = registers[reg]
            listused[i][1] = addresses[reg]
        else:
            exit()

    if listused[0][0] < listused[1][0]:
        flag = 4
    elif listused[0][0] > listused[1][0]:
        flag = 2
    else:
        flag = 1


def Invert(reg1, reg2):
    global r0, r1, r2, r3, r4, r5, r6, flag

    registers = {"R0": r0, "R1": r1, "R2": r2, "R3": r3, "R4": r4, "R5": r5, "R6": r6}
    addresses = {"R0": addr0, "R1": addr1, "R2": addr2, "R3": addr3, "R4": addr4, "R5": addr5, "R6": addr6}

    listused = [[0, 0], [0, 0]]

    for i, reg in enumerate([reg1, reg2]):
        if reg in registers:
            listused[i][0] = registers[reg]
            listused[i][1] = addresses[reg]

    tempb = conv_binary(listused[1][0])
    newstring = ""
    for bit in tempb:
        if bit == '1':
            newstring += '0'
        else:
            newstring += '1'
    newvalue = int(binary_to_decimal(newstring))

    if listused[0][0] == r0:
        r0 = newvalue
    elif listused[0][0] == r1:
        r1 = newvalue
    elif listused[0][0] == r2:
        r2 = newvalue
    elif listused[0][0] == r3:
        r3 = newvalue
    elif listused[0][0] == r4:
        r4 = newvalue
    elif listused[0][0] == r5:
        r5 = newvalue
    elif listused[0][0] == r6:
        r6 = newvalue


def Load(reg,addr):
    global r0,r1,r2,r3,r4,r5,r6,flag

    if reg=="R0":
       r0=vardict[addr]
    if reg=="R1":
       r1=vardict[addr]
    if reg=="R2":
       r2=vardict[addr]
    if reg=="R3":
       r3=vardict[addr]
    if reg=="R4":
       r4=vardict[addr]
    if reg=="R5":
       r5=vardict[addr]
    if reg=="R6":
       r6=vardict[addr]










def r_binary(binary):
    
    if binary=="000":
        return " R0"
    if binary=="001":
        return " R1"
    if binary=="010":
        return " R2"
    if binary=="011":
        return " R3"
    if binary=="100":
        return " R4"
    if binary=="101":
        return " R5"
    if binary=="110":
        return " R6"
    if binary=="111":
        return " FLAGS"
    
def m_binary(binary):
    return (" "+binary)

def imm_binary(binary):
    l_num=binary_to_decimal(binary)
    string=""
    for i in l_num:
        string=string+i
    return(" $"+string)



def idx_addr(addr):
  return int(binary_to_decimal(addr))

#_____________________CONVERSION_________________________


opcode_map = {
    "00000": "add",
    "00001": "sub",
    "00110": "mul",
    "01010": "xor",
    "01011": "or",
    "01100": "and",
    "00010": "mov",
    "01000": "rs",
    "01001": "ls",
    "00011": "mov",
    "00111": "div",
    "01101": "not",
    "01110": "cmp",
    "00100": "ld",
    "00101": "st",
    "01111": "jmp",
    "11100": "jlt",
    "11101": "jgt",
    "11111": "je",
    "11010": "hlt"
}

dump=[]
for i in range(128):
    dump.append("0000000000000000")
FCon=[]
for i in sys.stdin:
    FCon.append(i)
# Iterate through each instruction in FCon
for i in range(len(FCon)):
    FCon[i] = FCon[i].rsplit()
    dump[i] = FCon[i][0]

for i in range(len(FCon)):
    newstring = ""
    for j in FCon[i]:
        newstring = newstring + j
    FCon[i] = newstring

linevar = len(FCon)

for i in range(len(FCon)):
    opcode_prefix = FCon[i][0:5]
    if opcode_prefix in opcode_map:
        newstring = opcode_map[opcode_prefix]
        if opcode_prefix in ["00010", "01000", "01001"]:
            newstring = newstring + r_binary(FCon[i][6:9]) + imm_binary(FCon[i][9:16])
        elif opcode_prefix in ["00011", "00111", "01101", "01110"]:
            newstring = newstring + r_binary(FCon[i][10:13]) + r_binary(FCon[i][13:16])
        elif opcode_prefix in ["00100", "00101"]:
            newstring = newstring + r_binary(FCon[i][6:9]) + m_binary(FCon[i][9:16])
        elif opcode_prefix in ["01111", "11100", "11101", "11111"]:
            newstring = newstring + m_binary(FCon[i][9:16])
        FCon[i] = newstring


r0,r1,r2,r3,r4,r5,r6=0,0,0,0,0,0,0



varinitcheck=1
vardict={}
line=0

# FCon=[]
# for i in sys.stdin:
#     FCon.append(i)

for i in range(len(FCon)):
    FCon[i]=FCon[i].split()

j=0

while j<len(FCon):

    # if FCon[j][0]=="hlt":
    #     break
  
    
    i=FCon[j]
    print(lenbal(conv_binary(j),7),end="        ")

    # print(FCon)
    if i==[]:
        continue
    elif i[0]=="mov":
        if len(i)==3:
            if i[2][0]=="$":
                flag=0
                if i[1]=="R0":
                    MoveImmediate("r0",int(i[2][1::]),"000")
                elif i[1]=="R1":
                    MoveImmediate("r1",int(i[2][1::]),"001")
                elif i[1]=="R2":
                    MoveImmediate("r2",int(i[2][1::]),"010")
                elif i[1]=="R3":
                    MoveImmediate("r3",int(i[2][1::]),"011")
                elif i[1]=="R4":
                    MoveImmediate("r4",int(i[2][1::]),"100")
                elif i[1]=="R5":
                    MoveImmediate("r5",int(i[2][1::]),"101")
                elif i[1]=="R6":
                    MoveImmediate("r6",int(i[2][1::]),"110")
            

            elif i[2][0]=="R" or i[2][0]=="F":
                MoveRegister(i[1],i[2])
                flag=0
          

          

    


    elif i[0]=="add":
        flag=0
        if len(i) == 4:
            addition(i[1],i[2],i[3])
       

                
    elif i[0]=="sub":
        flag=0
        if len(i) == 4:
            subtraction(i[1],i[2],i[3])
      

                
    
    # elif i[0]=="ld":
           
    #     pass
       
    elif i[0]=="st":
        flag=0
        if i[1]=="R0":
            dump[linevar]="000000000"+lenbal(conv_binary((r0)),7)
        elif i[1]=="R1":
            dump[linevar]="000000000"+lenbal(conv_binary((r1)),7)
        elif i[1]=="R2":
            dump[linevar]="000000000"+lenbal(conv_binary((r2)),7)
        elif i[1]=="R3":
            dump[linevar]="000000000"+lenbal(conv_binary((r3)),7)
        elif i[1]=="R4":
            dump[linevar]="000000000"+lenbal(conv_binary((r4)),7)
        elif i[1]=="R5":
            dump[linevar]="000000000"+lenbal(conv_binary((r5)),7)
        elif i[1]=="R6":
            dump[linevar]="000000000"+lenbal(conv_binary((r6)),7)
        linevar=linevar+1


    
   
    elif i[0]=="mul":
        flag=0
        if len(i) == 4:
            multiply(i[1],i[2],i[3])
       

                
    elif i[0]=="div":
        flag=0
        if len(i)==3:
            divide(i[1],i[2])
      

    elif i[0]=="rs":
        flag=0
        if len(i)==3:
            if i[2][0]=="$":
                if i[1]=="R0":
                    Right_Shift("r0",int(i[2][1::]),"000")
                elif i[1]=="R1":
                    Right_Shift("r1",int(i[2][1::]),"001")
                elif i[1]=="R2":
                    Right_Shift("r2",int(i[2][1::]),"010")
                elif i[1]=="R3":
                    Right_Shift("r3",int(i[2][1::]),"011")
                elif i[1]=="R4":
                    Right_Shift("r4",int(i[2][1::]),"100")
                elif i[1]=="R5":
                    Right_Shift("r5",int(i[2][1::]),"101")
                elif i[1]=="R6":
                    Right_Shift("r6",int(i[2][1::]),"110")
               

          

    
    elif i[0]=="ls":
        flag=0
        if len(i)==3:
            if i[2][0]=="$":
                if i[1]=="R0":
                    Left_Shift(r0,int(i[2][1::]),"000")
                elif i[1]=="R1":
                    Left_Shift(r1,int(i[2][1::]),"001")
                elif i[1]=="R2":
                    Left_Shift(r2,int(i[2][1::]),"010")
                elif i[1]=="R3":
                    Left_Shift(r3,int(i[2][1::]),"011")
                elif i[1]=="R4":
                    Left_Shift(r4,int(i[2][1::]),"100")
                elif i[1]=="R5":
                    Left_Shift(r5,int(i[2][1::]),"101")
                elif i[1]=="R6":
                    Left_Shift(r6,int(i[2][1::]),"110")
               

       

 
   

    elif i[0]=="xor":
            flag=0
            Exclusive_OR(i[1],i[2],i[3])
      

                
    elif i[0]=="or":
            flag=0
            OR(i[1],i[2],i[3])
    

                
    elif i[0]=="and":
            flag=0
            AND(i[1],i[2],i[3])
   
                
    elif i[0]=="not":
            flag=0
            Invert(i[1],i[2])
       

    elif i[0]=="cmp":
            flag=0
            Compare(i[1],i[2])
     

    elif i[0]=="jmp":
        j=idx_addr(i[1])-1
        flag=0

    elif i[0]=="jlt":
        
        if flag==4:
            j=idx_addr(i[1])-1
        flag=0
        

    elif i[0]=="jgt":
        if flag==2:
            j=idx_addr(i[1])-1
        flag=0
       


    elif i[0]=="je":
        if flag==1:
            j=idx_addr(i[1])-1
        flag=0
    
    elif i[0]=="hlt":
        flag=0

        reglist=[lenbal(conv_binary(r0),16),lenbal(conv_binary(r1),16),lenbal(conv_binary(r2),16),lenbal(conv_binary(r3),16),lenbal(conv_binary(r4),16),lenbal(conv_binary(r5),16),lenbal(conv_binary(r6),16),lenbal(conv_binary(flag),16),]
        for i in reglist:
            print(i,end=" ")
        print()
        break

    reglist=[lenbal(conv_binary(r0),16),lenbal(conv_binary(r1),16),lenbal(conv_binary(r2),16),lenbal(conv_binary(r3),16),lenbal(conv_binary(r4),16),lenbal(conv_binary(r5),16),lenbal(conv_binary(r6),16),lenbal(conv_binary(flag),16),]
    for i in reglist:
        print(i,end=" ")
    print()
    j=j+1

# plist=[r0,r1,r2,r3,r4,r5,r6,flag]

for i in dump:
    print(i)