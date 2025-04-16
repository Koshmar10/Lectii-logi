#operatorii pe biti
#0 si 1
#34
num = 3412
print(bin(num))
print(oct(num))
print(hex(num))
#b10 = [0, 1 ... 9]
#0x = [ 0, 1, .. 9, A, B, C, D, E, F]
#12 -> 0b
#12 / 2 cat 6 rest 0
#6 / 2 cat 3 rest 0
#3 / 2 cat 1 rest 1
#1 / 2 cat 0 rest 1
# baza 10 -> baza 2 
# 0b1100
# ? baza2 -> baza 10
# 0b1100
# 1, 1, 0, 0
# 3  2  1  0
# 2**0 * 0 + 2**1 * 0 + 2**2 * 1 + 2**3 * 1
# 1234 - baza x
# baza x -> baza 10
# x**0 * 4 + x**1 * 3 + x**2 * 2 ...
# 
#  0 + 0 + 4 + 8
# 12
# 0 finish
num = 0x21f # baza 16
# 0x1f
# 16**0 * f + 16**1 * 1 + 16**2 * 2
#operatori pe biti
# &, |, ~, ^, <<, >>
a = 23
b = 21
print(bin(a))
print(bin(b))
result = a & b
#0b101
#0b001
#0b100
print('a & b', bin(result))
result = a | b
print('a | b', bin(result))
result = a ^ b
#xor = exclusive or
print('a ^ b', bin(result))
print('~a', ~a)
# a = 3 
# ~a = -3 -1 =-4
result = a << 2
#shift la stanga
# a * 2**2
print( 'a << 1',  a<<2)
#shift la dreapta
# b // 2**q
print( 'b >> 1',  bin(b>>1))