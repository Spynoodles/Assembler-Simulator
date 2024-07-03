import ctypes
import sys

# Global variables
r0 = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0
addr0 = "000"
addr1 = "001"
addr2 = "010"
addr3 = "011"
addr4 = "100"
addr5 = "101"
addr6 = "110"
flag = 0
addrflag = "111"

# Conversion functions
def conv_binary(decimal):
    list1 = []
    factorial = 2
    while decimal // factorial != 0:
        list1.append(decimal % factorial)
        decimal = decimal // 2
    list1.append(decimal % 2)
    list1.reverse()
    return list1

def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += binary[i] * (2 ** i)
    return decimal

def addlist(l1, l2):
    num1 = binary_to_decimal(l1)
    num2 = binary_to_decimal(l2)
    reg3 = num1 + num2
    reg3 = conv_binary(reg3)
    return reg3

# Registers dictionary
registers = {
    "R0": (r0, addr0),
    "R1": (r1, addr1),
    "R2": (r2, addr2),
    "R3": (r3, addr3),
    "R4": (r4, addr4),
    "R5": (r5, addr5),
    "R6": (r6, addr6)
}

def addition(reg1, reg2, reg3):
    listused = [[0, 0], [0, 0], [0, 0]]
    
    for i, reg in enumerate([reg1, reg2, reg3]):
        if reg in registers:
            listused[i][0], listused[i][1] = registers[reg]
        else:
            print(f"Typo in Register name at line {line}")
            exit()
            return None

    listused[1][0] = conv_binary(listused[1][0])
    listused[2][0] = conv_binary(listused[2][0])

    listused[0][0] = addlist(listused[1][0], listused[2][0])
    if len(listused[0][0]) > 7:
        global flag
        flag = 1
        listused[0][0].reverse()
        while len(listused[0][0]) > 7:
            listused[0][0].pop()
        listused[0][0].reverse()
    
    print("00000" + "00" + listused[0][1] + listused[1][1] + listused[2][1])

    return listused[0]

def sublist(l1, l2):
    num1 = binary_to_decimal(l1)
    num2 = binary_to_decimal(l2)
    reg3 = num1 - num2
    reg3 = conv_binary(reg3)
    return reg3

def subtraction(reg1, reg2, reg3):
    listused = [[0, 0], [0, 0], [0, 0]]
    
    for i, reg in enumerate([reg1, reg2, reg3]):
        if reg in registers:
            listused[i][0], listused[i][1] = registers[reg]
        else:
            print(f"Typo in Register name at line {line}")
            exit()
            return None

    listused[1][0] = conv_binary(listused[1][0])
    listused[2][0] = conv_binary(listused[2][0])

    listused[0][0] = sublist(listused[1][0], listused[2][0])
    if len(listused[0]) > 7:
        global flag
        flag = 1
        listused[0][0].reverse()
        while len(listused[0][0]) > 7:
            listused[0][0].pop()
        listused[0][0].reverse()
    
    print("00001" + "00" + listused[0][1] + listused[1][1] + listused[2][1])

    return listused[0]


def mullist(l1, l2):
    num1 = binary_to_decimal(l1)
    num2 = binary_to_decimal(l2)
    reg3 = num1 * num2
    reg3 = conv_binary(reg3)
    return reg3

def multiply(reg1, reg2, reg3):
    listused = [[0, 0], [0, 0], [0, 0]]
    
    for i, reg in enumerate([reg1, reg2, reg3]):
        if reg in registers:
            listused[i][0], listused[i][1] = registers[reg]
        else:
            print(f"Typo in Register name at line {line}")
            exit()
            return None

    listused[1][0] = conv_binary(listused[1][0])
    listused[2][0] = conv_binary(listused[2][0])

    listused[0][0] = mullist(listused[1][0], listused[2][0])
    if len(listused[0][0]) > 7:
        global flag
        flag = 1
        listused[0][0].reverse()
        while len(listused[0][0]) > 7:
            listused[0][0].pop()
        listused[0][0].reverse()
    
    print("00110" + "00" + listused[0][1] + listused[1][1] + listused[2][1])

    return listused[0]

def divide(reg1, reg2):
    listused = [[0, 0], [0, 0]]
    
    for i, reg in enumerate([reg1, reg2]):
        if reg in registers:
            listused[i][0], listused[i][1] = registers[reg]
        else:
            print(f"Typo in reg name {line}")
            exit()
            return None
    
    listused[0][0] = listused[1][0]
    print("00111" + "00000" + listused[0][1] + listused[1][1])
    
    return reg1
def Exclusive_OR(reg1, reg2, reg3):
    listused = [[0, 0], [0, 0], [0, 0]]
    
    for i, reg in enumerate([reg1, reg2, reg3]):
        if reg in registers:
            listused[i][0], listused[i][1] = registers[reg]
        else:
            print(f"Typo in Register name at line {line}")
            exit()
            return None

    listused[1][0] = conv_binary(listused[1][0])
    listused[2][0] = conv_binary(listused[2][0])

    listused[0][0] = mullist(listused[1][0], listused[2][0])
    if len(listused[0][0]) > 7:
        global flag
        flag = 1
        listused[0][0].reverse()
        while len(listused[0][0]) > 7:
            listused[0][0].pop()
        listused[0][0].reverse()
    
    print("01010" + "00" + listused[0][1] + listused[1][1] + listused[2][1])

    return listused[0]

def OR(reg1, reg2, reg3):
    listused = [[0, 0], [0, 0], [0, 0]]
    
    for i, reg in enumerate([reg1, reg2, reg3]):
        if reg in registers:
            listused[i][0], listused[i][1] = registers[reg]
        else:
            print(f"Typo in Register name at line {line}")
            exit()
            return None

    listused[1][0] = conv_binary(listused[1][0])
    listused[2][0] = conv_binary(listused[2][0])

    listused[0][0] = mullist(listused[1][0], listused[2][0])
    if len(listused[0][0]) > 7:
        global flag
        flag = 1
        listused[0][0].reverse()
        while len(listused[0][0]) > 7:
            listused[0][0].pop()
        listused[0][0].reverse()
    
    print("01011" + "00" + listused[0][1] + listused[1][1] + listused[2][1])

    return listused[0]

def AND(reg1, reg2, reg3):
    listused = [[0, 0], [0, 0], [0, 0]]
    
    for i, reg in enumerate([reg1, reg2, reg3]):
        if reg in registers:
            listused[i][0], listused[i][1] = registers[reg]
        else:
            print(f"Typo in Register name at line {line}")
            exit()
            return None

    listused[1][0] = conv_binary(listused[1][0])
    listused[2][0] = conv_binary(listused[2][0])

    listused[0][0] = mullist(listused[1][0], listused[2][0])
    if len(listused[0][0]) > 7:
        global flag
        flag = 1
        listused[0][0].reverse()
        while len(listused[0][0]) > 7:
            listused[0][0].pop()
        listused[0][0].reverse()
    
    print("01100" + "00" + listused[0][1] + listused[1][1] + listused[2][1])

    return listused[0]


def MoveImmediate(reg, imm, areg):
    if imm > 127 or imm < 0:
        print(f"Illegal Immediate values at line {line}")
        exit()
        return None
    if type(imm) != int:
        print(f"IMMEDIATE VALUE IS NOT AN INTEGER at line {line}\n")
        exit()
        return None

    imm = conv_binary(imm)
    balance = 7 - len(imm)
    covstr = "".join(str(i) for i in imm)
    print("00010" + "0" + areg + "0" * balance + covstr + "\n")

    return reg


def Right_Shift(reg, imm, areg):
    if imm > 127 or imm < 0:
        print(f"Illegal Immediate values at line {line}\n")
        exit()
        return None
    if type(imm) != int:
        print(f"IMMEDIATE VALUE IS NOT AN INTEGER at line {line}\n")
        exit()
        return None

    imm = conv_binary(imm)
    balance = 7 - len(imm)
    covstr = "".join(str(i) for i in imm)
    print("01000" + "0" + areg + "0" * balance + covstr + "\n")

    return reg


def Left_Shift(reg, imm, areg):
    if imm > 127 or imm < 0:
        print(f"Illegal Immediate values at line {line}\n")
        exit()
        return None
    if type(imm) != int:
        print(f"IMMEDIATE VALUE IS NOT AN INTEGER at line {line}\n")
        exit()
        return None

    imm = conv_binary(imm)
    balance = 7 - len(imm)
    covstr = "".join(str(i) for i in imm)
    print("01001" + "0" + areg + "0" * balance + covstr + "\n")

    return reg


def MoveRegister(reg1, reg2):
    listused = [[0, 0], [0, 0]]
    
    for i, reg in enumerate([reg1, reg2]):
        if reg in registers:
            listused[i][0], listused[i][1] = registers[reg]
        else:
            print(f"Typo in reg name at line {line}")
            exit()
            return None

    listused[0][0] = listused[1][0]
    print("00011" + "00000" + listused[0][1] + listused[1][1])

    return reg1

def Compare(reg1, reg2):
    listused = [[0, 0], [0, 0]]

    for i, reg in enumerate([reg1, reg2]):
        if reg in registers:
            listused[i][0], listused[i][1] = registers[reg]
        else:
            print(f"Typo in reg name at line {line}")
            exit()
            return None

    listused[0][0] = listused[1][0]
    print("01110" + "00000" + listused[0][1] + listused[1][1])
    
    return reg1


def Invert(reg1, reg2):
    listused = [[0, 0], [0, 0]]

    for i, reg in enumerate([reg1, reg2]):
        if reg in registers:
            listused[i][0], listused[i][1] = registers[reg]
        else:
            print(f"Typo in reg name at line {line}")
            exit()
            return None

    listused[0][0] = listused[1][0]
    print("01101" + "00000" + listused[0][1] + listused[1][1])
    
    return reg1


def Load(reg, addr):
    if reg in registers:
        reg_value, reg_addr = registers[reg]
        print("00100" + "0" + reg_addr + addr)
        ptr = ctypes.cast(addr, ctypes.POINTER(ctypes.c_int))
        reg_value = ptr.contents.value
        registers[reg] = (reg_value, reg_addr)
        return reg_value
    else:
        print(f"Typo in Reg Name at line {line}")
        exit()
        return None


def Store(reg, addr):
    if reg in registers:
        reg_value, reg_addr = registers[reg]
        print("00101" + "0" + reg_addr + addr)
        return addr
    else:
        print(f"Typo in Reg Name at line {line}")
        exit()
        return None


def hlt():
    print("1101000000000000\n")
def jlt(addr):
    s = '11100' + '0000' + addr
    print(s)

def jgt(addr):
    s = '11101' + '0000' + addr
    print(s)

def je(addr):
    s = '11111' + '0000' + addr
    print(s)

def jmp(addr):
    s = '01111' + '0000' + addr
    print(s)


#_____________________MAIN________________________________

varinitcheck=1
memadd=2**7-1
vardict={}
line=0
# file=open("Assembly.txt","r+")
# FCon=file.readlines()
FCon=[]
for i in sys.stdin:
    FCon.append(i)

hltcount=0
for i in range(len(FCon)):
    FCon[i]=FCon[i].rsplit()
lineskips=-1
countvar=0
for i in FCon:
    if i[0]=="var":
        countvar=countvar+1
    
for i in FCon:
    # print(line)
    lineskips=lineskips+1
    if i[0]!="var":
        line=line+1
   
    if i[0][len(i[0])-1]==":":
        if i[1]=="hlt":
            hltcount=hltcount+1
        if i[0][len(i[0])-2]==" ":
            print("Space between semicolon and label at line"+str(line))
            exit()
        t=conv_binary(line-1)
        string_con=""
        t.reverse()
        num=0
        while len(t)!=7:
              
               t.append("0")

        t.reverse()
        for k in t:
            string_con=string_con+str(k)

        vardict[i[0]]=string_con
    # line=line+lineskips
    if i[0]=="hlt":
        hltcount=hltcount+1

    if i[0]=="var":
        if(len(i)==1):
            print("Variable not defined at line"+str(line))
            exit()

        if varinitcheck==0:
            print("Variable initialised in between the instructions"+str(line)+'\n')
            exit()

        k=len(FCon)-countvar+lineskips+1
        t=conv_binary(k-1)
        t.reverse()
        while len(t)!=7:
               t.append("0")
        t.reverse()
        string_con=""
        for k in t:
            string_con=string_con+str(k)
        vardict[i[1]]=string_con
    else:
        varinitcheck=0
 

        memadd=memadd-1

line=0
for i in FCon:
    line=line+1
    if i[0][len(i[0])-1]==":":
        i.reverse()
        i.pop()
        i.reverse()
    # if i[0]==hlt:
    #     hltcount=hltcount+1
    if i==[]:
        continue
    elif i[0]=="var":
        continue
    elif i[0]=="mov":
        if len(i)==3:
            if i[2][0]=="$":
                registers = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]
                found_register = False
                for reg in registers:
                    if i[1]==reg:
                        MoveImmediate(reg,int(i[2][1::]),format(registers.index(reg), '03b'))
                        found_register = True
                        break
                if not found_register:
                    print("INVALID REGISTER NAME\n"+str(line)+'\n')
                    exit()

            elif i[2][0]=="R" or i[2][0]=="F":
                MoveRegister(i[1],i[2])
            else:
                print("Invalid Value defined"+str(line)+'\n')
                exit()

        else:
            print("Invalid number of registers"+str(line)+'\n')
            exit()


    elif i[0] in ["add", "sub", "mul", "div", "xor", "or", "and"]:
        if len(i) == 4:
            if i[0] == "add":
                addition(i[1],i[2],i[3])
            elif i[0] == "sub":
                subtraction(i[1],i[2],i[3])
            elif i[0] == "mul":
                multiply(i[1],i[2],i[3])
            elif i[0] == "div":
                divide(i[1],i[2])
            elif i[0] == "xor":
                Exclusive_OR(i[1],i[2],i[3])
            elif i[0] == "or":
                OR(i[1],i[2],i[3])
            elif i[0] == "and":
                AND(i[1],i[2],i[3])
        else:
            print("MISSING REGISTER.INVALID INPUT FORMAT."+str(line))
            exit()


    elif i[0] in ["ld", "st"]:
         if len(i)==3:
            check=0
            for key,value in vardict.items():
                    if i[2]==key:
                        if i[0] == "ld":
                            Load(i[1],value)
                        elif i[0] == "st":
                            Store(i[1],value)
                        check=1
                        break
            if check==0:
                print("Use of undefined variables/lable"+str(line))
                exit()

         else:
            print("Invalid number of parameters"+str(line)+'\n') 
            exit()
       
    elif i[0] in ["hlt", "rs", "ls"]:
        if i[0] == "hlt":
            hlt()
        elif i[0] == "rs":
            if len(i)==3:
                if i[2][0]=="$":
                    registers = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]
                    found_register = False
                    for reg in registers:
                        if i[1]==reg:
                            Right_Shift(reg,int(i[2][1::]),format(registers.index(reg), '03b'))
                            found_register = True
                            break
                    if not found_register:
                        print("INVALID REGISTER NAME\n"+str(line)+'\n')
                        exit()

                else:
                    print("Value is not defined"+str(line)+'\n')
                    exit()

            else:
                print("Invalid number of registers"+str(line)+'\n')
                exit()

        elif i[0] == "ls":
            if len(i)==3:
                if i[2][0]=="$":
                    registers = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]
                    found_register = False
                    for reg in registers:
                        if i[1]==reg:
                            Left_Shift(reg,int(i[2][1::]),format(registers.index(reg), '03b'))
                            found_register = True
                            break
                    if not found_register:
                        print("INVALID REGISTER NAME\n"+str(line)+'\n')
                        exit()

                else:
                    print("Value is not defined"+str(line)+'\n')
                    exit()

            else:
                print("Invalid number of registers"+str(line)+'\n')
                exit()

    elif i[0] == "not":
        if len(i)==3:
            Invert(i[1],i[2])
        else:
            print("Invalid number of registers"+str(line)+'\n')
            exit()

    elif i[0] == "cmp":
        if len(i)==3:
            Compare(i[1],i[2])
        else:
            print("Invalid number of registers"+str(line)+'\n')
            exit()

    elif i[0] in ["jmp", "jlt", "jgt", "je"]:
        if len(i)==2:
            check=0
            for key,value in vardict.items():
                    if i[1]==key[0:-1]:
                        if i[0] == "jmp":
                            jmp(value)
                        elif i[0] == "jlt":
                            jlt(value)
                        elif i[0] == "jgt":
                            jgt(value)
                        elif i[0] == "je":
                            je(value)
                        check=1
                        break
            
            if check==0:
                print("Use of undefined variables/lable"+str(line)+" \n")
                exit()

        else:
            print("Invalid number of parameters"+str(line)+'\n')
            exit()

    else:
        print("ERROR MISSPELLED"+str(line))
        exit()


    if hltcount==0:
        print("NO HLT instruction present\n")
        exit()

    elif hltcount>1:
        print("More than 1 HLT instructions present\n")
        exit()
  
    checklhalt=1
    for j in FCon[len(FCon)-1]:

        if j=="hlt":
            checklhalt=0
    if checklhalt!=0:  
        print("HLT is not the last instruction\n")
        exit()
