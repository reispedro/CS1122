'''
	hw03

	Pedro Vasconcelos de Almeida Reis
	CS1122
	Polytechnic University
'''

import string
import binascii
import math

def convertToBinary(num):
	binNum = '{0:08b}'.format(num)
	print("The number " + str(num) + " as a 8-bit Binary is " + str(binNum))

def hexaToAscii(alist):
	charList = []
	for i in alist:
		data = i[2:]
		charList.append(''.join(chr(int(data[i:i+2], 16)) for i in range(0, len(data), 2)))
	mergedString = ''.join(charList)
	print(mergedString)

def binToHex(binStr):
	alist = binStr.split()
	hexList = []
	for i in alist:
		ahex = hex(int(i,2))
		astr = ahex[:2] + ahex[2:].upper()
		hexList.append(astr)
	mergedString = ' '.join(hexList)
	print(mergedString)

def octalToDec(octal):
	octList = list(str(octal))
	octList.reverse()
	total = 0
	for i,c in enumerate(octList):
		decimal = int(c) * math.pow(8,i)
		total = total + decimal
	print("The octal number " + str(octal) + " as a decimal is " + str(total))

def main():
	convertToBinary(57)
	convertToBinary(123)
	convertToBinary(85)
	convertToBinary(38)
	print("__________________________\n")
	alist = ["0x41","0x53","0x43","0x49","0x49","0x20","0x77","0x68","0x61","0x74","0x20","0x79","0x6f","0x75","0x20","0x64","0x69","0x64","0x20","0x74","0x68","0x65","0x72","0x65"]
	blist = ['0x39', '0x41', '0x4d', '0x20', '0x69', '0x73', '0x20', '0x74', '0x6f', '0x6f', '0x20', '0x65', '0x61', '0x72', '0x6c', '0x79', '0x20', '0x66', '0x6f', '0x72', '0x20', '0x63', '0x6c', '0x61', '0x73', '0x73']
	clist = ['0x43', '0x6f', '0x6d', '0x70', '0x75', '0x74', '0x65', '0x72', '0x73', '0x20', '0x61', '0x72', '0x65', '0x20', '0x6d', '0x61', '0x67', '0x69', '0x63']
	dlist = ["0x57", "0x68", "0x61", "0x74", "0x20", "0x74", "0x68", "0x65", "0x20", "0x68", "0x65", "0x78", "0x3f"]
	hexaToAscii(alist)
	hexaToAscii(blist)
	hexaToAscii(clist)
	hexaToAscii(dlist)
	print("__________________________\n")
	binToHex("0000 1011 1010 1110 1101 1110 1010 1101")
	binToHex("1100 1010 1111 1110 1111 1010 1100 1110")
	binToHex("1011 1110 1110 1111 1101 0000 0000 1101")
	binToHex("1111 1111 1111 1111 1001 0000 0110 0010")
	print("__________________________\n")
	octalToDec(10)
	octalToDec(42)
	octalToDec(77)
	octalToDec(113)
	print("__________________________\n")



if __name__ == "__main__":
    main()