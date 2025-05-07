#Lectia 9
#Operatori
#1 Aritmetici

def OpAritmetici():
    print(3 + 5)
    print(10 / 4, 10 // 4, 10 / -4, 10 // -4)
    print(5 - 3)
    print(3 * 5)
    print(3 ** 3)

def OpComparatie():
    print(3 == 3)
    print(3 < 5, 3 > 5, 3 <= 4, 3 >= 4)

def OpLogici():
    print ( True and True)
    print( not 5)
    print(True or False)

def OpPyhon():
    #in si is
    x = None
    list = [1, 4, 10 , 20]
    print(20 in list)
    print(x is None)
#baza 16 cifre de la 0  pana la 15
#ce facem cu cifrele 10 - 15?
#10 = A 11 = B 12 = C 13 = D 14 = E 15 = F

#ZECIMAL IN BINAR
#numar 5
# 5 / 2 => catul 2 rest 1
# 2 / 2 => catul 1 rest 0
# 1 / 2 => catul 0 rest 1
# 0 finish
#(5)2 (101)2

#BINAR IN ZECIMAL
#0b011
#[ 0, 1, 1]
#  2  1  0
# 0b => b10
# 1 * 2**0 + 1 * 2**1 + 0 * 2**2
# 1* 1 + 1*2 + 0 = 1 + 2 + 0 = 3

#OCTAL IN ZECIMAL
# avem cifre de la 0 la 7
#0o41
#[4, 1] baza 8
# 1  0
# 1 * 8**0 + 4 * 8**1 = 1*1 + 4*8  = 1 + 32 = 33
#
#HEXAZECIMAL IN ZECIMAL
#0x12F
#[1, 2, f] baza 16
# 2  1  0
# 15 * 16**0 + 2 * 16**1 + 2 * 16** 2 =  15 + 32 + 512 = 15 + 545 = 560
def OpBiti():
    x = 212
    print(bin(x))
    print(oct(x))
    print(hex(x))

    #operatorul &
    x = 5 #101
    y = 3 #011
    #5 & 3 = 001
    # 1 * 2*0 = 1  
    print(x, bin(x))
    print(y, bin(y))
    print('x & y ', bin(x & y))

    #operatorul |
    # 2 /2 c 1 r 0
    # 1 /2 c 0 r 1
    # 0b10
    # 9 / 2 c 4 r 1
    # 4 / 2 c 2 r 0
    # 2 / 2 c 1 r 0
    # 1 / 2 c 0 r 1
    # 0 --
    x = 3 #0011 
    y = 9 #1001
    #or    1011
    #xor   1010
    # 1 * 2**0 + 1 * 2 **1 + 0*2**2 1*2**3
    # 12
    print(x, bin(x))
    print(y, bin(y))
    print('x | y', bin(x | y))
    print('x ^ y', bin(x ^ y))
    print('~x', ~x)
    #x =3
    #~x = -x -1

    num = 0b101
    #Left shit 
    print(bin(num << 2)) # inmultire cu 2**2
    #Right shift
    print(bin(num >> 2)) # impartire cu 2 **2

def Shifts(a):
    print(a, a << 3)
    #0b010 << 1
    #0b0100
    # a * 2**3
    print(a, a >> 2)
    #0b010 >> 1
    #0b01
    #a // 2 * 2
def isEven(a):
    # cu modulo
    '''
    if a % 2 == 0:
        return True
    else:
        return False
    '''
    # biti
    if a & 0b1 == 1:
        return False
    else:
        return True
    #0b101   
    #0b001
    #2**0*1 + 2**1 * 0 + 2**2 * 1
#transformari
# zecmal -> binar
# 5 / 2 cat 2 rest 1
# 2 /2 cat 1 rest 0
# 1 / 2 cat 0 rest 1
# binar -> zecimal
# 0b101
#   210
# 2**0 * 1 + 2**1 * 0 + 2**2 * 2
# 1 + 0 + 4 = 5 

#OpBiti()
Shifts(11)
print(isEven(4))