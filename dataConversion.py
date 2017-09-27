"""
# filename:dataConversion.py
# author:heizhou
# No.:150420226
# date:17/9/27
# purpose:This file is for converting data to different types for using
"""

def uniToHex(string):
    """this method is to convert unicode data to hexadecimal"""
    return_hex = ''
    for char in string:
        return_hex += "%02x" % ord(char)
    return return_hex


def hexToUni(hex):
    """this method is to convert hexadecimal data to unicode"""
    return_str = ''
    hex_len = len(hex)
    for i in range(0, hex_len, 2):
        return_str += chr(int(hex[i:i + 2], 16))
    return return_str


def hexToBina(code, lens):
    """from hexadecimal data to binary"""
    return_code = ''
    lens = lens % 16
    for key in code:
        dec = int(key, 16)
        return_code += decToBin(dec, 4)
    # handle data if key is not multiple of 16
    if lens != 0:
        return_code += '0' * (16 - lens) * 4
    return return_code


def decToBin(dec, lens):
    """from decimal to binary.if use bin(decimal) will output unexpected data,example:'0x22'>>>>'0b100b10'"""
    return_code = ''
    for i in range(lens):
        return_code = str(dec >> i & 1) + return_code
    return return_code
