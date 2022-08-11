import repcodepack
import math

def addition(list):
    total=0
    for item in list:
        total+=item
    return total


def subtraction(list):
    total = list[0]
    for item in list:
        if item != list[0]:
            total-=item
    return total


def multiplication(list):
    prod=1
    for item in list:
        prod*=item
    return prod


def division(list):
    total=list[0]
    for item in list:
        if item != list[0]:
            total/=item
    return total


def power(base, power):
    return base**power


def rootover(radicand, power):
    return radicand**(1/power)


def expraise(power):
    return 2.718281828459045**power


def sine(angle):
    anglerad=(angle*3.14159)/180
    total = 0
    power=3
    for i in range(3):
        temp = (anglerad**power)/repcodepack.fact(power)
        if i==1:
            total-=temp
        else:
            total+=temp
        power+=2
    total_fin=anglerad-total
    return round(total_fin, 1)


def cosine(angle):
    anglerad=(angle*3.14159)/180
    total = 0
    power=2
    for i in range(3):
        temp = (anglerad**power)/repcodepack.fact(power)
        if i == 1:
            total-=temp
        else:
            total+=temp
        power+=2
    total_fin=1-total
    return round(total_fin, 1)


def tangent(angle):
    x=sine(angle)
    y=cosine(angle)
    return x/y


def naturalog(num):
    var=(num-1)/(num+1)
    total=0
    for i in range(1, 22):
        if i % 2==1:
            temp=(var**i)/i
            total+=temp
    return round(2*total, 8)


def logarithm(num):
    return round(naturalog(num)/naturalog(10), 3)


def quadratic_equations(a, b, c):
    discriminant=4*a*c
    x1 = ((b*-1)+(b**2-discriminant)**0.5)/2*a
    x2 = ((b*-1)-(b**2-discriminant)**0.5)/2*a
    return f'The 1st root is {x1} and the second root is {x2}'


def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')


def DecimalToOctal(decimal):
    octal = 0
    ctr = 0
    temp = decimal  
    
    while(temp > 0):
        octal += ((temp%8)*(10**ctr))  
        temp = int(temp/8)             
        ctr += 1

    return octal


conversion_table = {0: '0',
                    1: '1', 
                    2: '2',
                    3: '3', 
                    4: '4',
                    5: '5', 
                    6: '6', 
                    7: '7',
                    8: '8', 
                    9: '9', 
                    10: 'A', 
                    11: 'B', 
                    12: 'C',
                    13: 'D', 
                    14: 'E', 
                    15: 'F'}
 
 
def DecimalToHexadecimal(decimal):
    hexadecimal = ''
    while(decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16
 
    return hexadecimal


def BinaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def BinaryToOctal(binary):
    temp=BinaryToDecimal(binary)
    return DecimalToOctal(temp)


def BinaryToHexadecimal(binary):
    temp=BinaryToDecimal(binary)
    return DecimalToHexadecimal(temp)


def OctalToBinary(octnum): 
    binary = "" 
    while octnum != 0:
        d = int(octnum % 10)
        if d == 0:
            binary = "".join(["000", binary])
        elif d == 1:
            binary = "".join(["001", binary])
        elif d == 2:
            binary = "".join(["010", binary])
        elif d == 3:
            binary = "".join(["011", binary])
        elif d == 4:
            binary = "".join(["100", binary])
        elif d == 5:
            binary = "".join(["101", binary])
        elif d == 6:
            binary = "".join(["110",binary])
        elif d == 7:
            binary = "".join(["111", binary])
        else:
            binary = "Invalid Octal Digit"
            break
        octnum = int(octnum / 10)
    return binary


def OctalToDecimal(octnum):
    temp=OctalToBinary(octnum)
    return BinaryToDecimal(temp)
 

def OctaltoHexadecimal(octnum):
    temp=OctalToBinary(octnum)
    return BinaryToHexadecimal(temp)


def HexadecimalToBinary(ini_string):
    res = "{0:08b}".format(int(ini_string, 16))
    return str(res)


def HexadecimalToDecimal(ini_string):
    temp=HexadecimalToBinary(ini_string)
    return BinaryToDecimal(int(temp))


def HexadecimalToOctal(ini_string):
    temp=HexadecimalToBinary(ini_string)
    return BinaryToOctal(int(temp))