"""
# filename:handleMethod.py
# author:heizhou
# No.:150420226
# date:17/9/27
# purpose:the method in this file is to handle 16 rounds' iteration
"""
import dateSource as DS
from dataConversion import decToBin


def xorFunc(code, key):
    """xor function"""
    code_len = len(key)
    return_list = ''
    for i in range(code_len):
        if code[i] == key[i]:
            return_list += '0'
        else:
            return_list += '1'
    return return_list


def permuWithIp(code):
    """Initial permutation with table IP"""
    changed_code = ''
    for i in range(64):
        changed_code += code[DS.ip[i] - 1]
    return changed_code


def finalPermutation(code):
    """Final permutation with table IP^-1"""
    return_list = ''
    for i in range(16):
        list = ''
        for j in range(4):
            list += code[DS.ip_1[i * 4 + j] - 1]
        return_list += "%x" % int(list, 2)
    return return_list


def keyFirstCompr(key):
    """first compress for key from 64bit to 56bit"""
    changed_key = ''
    for i in range(56):
        changed_key += key[DS.ck1[i] - 1]
    return changed_key


def keySecondCompr(key):
    """second compress for key from 56bit to 48bit"""
    return_list = ''
    for i in range(48):
        return_list += key[DS.ck2[i] - 1]
    return return_list

def expansionCode(code):
    """expansion the code from 32bit to 48bit"""
    return_list = ''
    for i in range(48):
        return_list += code[DS.expansionTable[i] - 1]
    return return_list


def permuWithP(code):
    """permutation with P-BOX"""
    return_list = ''
    for i in range(32):
        return_list += code[DS.pBox[i] - 1]
    return return_list



def subsWithS(code):
    """substitution with S-BOX"""
    return_list = ''
    for i in range(8):
        row = int(str(code[i * 6]) + str(code[i * 6 + 5]), 2)
        raw = int(str(code[i * 6 + 1]) + str(code[i * 6 + 2]) + str(code[i * 6 + 3]) + str(code[i * 6 + 4]), 2)
        return_list += decToBin(DS.sBox[i][row][raw], 4)
    return return_list





