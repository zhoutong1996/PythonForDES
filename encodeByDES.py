"""
# filename:encodeByDES.py
# author:heizhou
# No.:150420226
# date:17/9/27
# purpose:This file is to encode by DES algorithm
"""
import dateSource as DS
import dataConversion as DC
import handleMethod as HM


class DESEncode():
    """encode with des"""
    def __init__(self):
        pass

    def encode(self, from_code, key, code_len):
        output = ""
        trun_len = 0

        # translate form_code and key to binary
        code_string = DC.hexToBina(from_code, code_len)

        # if code_len is not the multiple of 16, change it
        if code_len % 16 != 0:
            real_len = (code_len / 16) * 16 + 16
        else:
            real_len = code_len

        # hexadecimal to binaty ,bit will plus 4
        trun_len = 4 * real_len
        # use function f handle every 64bit from_code
        for i in range(0, trun_len, 64):
            run_code = code_string[i:i + 64]

            # first permutation for 64bit code and key
            run_code = HM.permuWithIp(run_code)
            run_key = HM.keyFirstCompr(key)

            # 16 rounds of iteration
            for j in range(16):
                # get code left 32bit and right 32bit
                code_r = run_code[32:64]
                code_l = run_code[0:32]

                # handle right 32bit code
                run_code = code_r

                # expansion 32bit code to 48bit
                code_r = HM.expansionCode(code_r)

                # get subkey for this round
                key_l = run_key[0:28]
                key_r = run_key[28:56]
                key_l = key_l[DS.leftShift[j]:28] + key_l[0:DS.leftShift[j]]
                key_r = key_r[DS.leftShift[j]:28] + key_r[0:DS.leftShift[j]]
                run_key = key_l + key_r
                key_y = HM.keySecondCompr(run_key)

                # code_r xor key_y
                code_r = HM.xorFunc(code_r, key_y)

                # S-BOX
                code_r = HM.subsWithS(code_r)

                # P-BOX
                code_r = HM.permuWithP(code_r)

                # code_l xor code_r
                code_r = HM.xorFunc(code_l, code_r)
                run_code += code_r
            # change left code and right code
            code_r = run_code[32:64]
            code_l = run_code[0:32]
            run_code = code_r + code_l

            # handle code with IP^-1
            output += HM.finalPermutation(run_code)
        return output


def entry(from_code, key):
    """the entry for des encode function"""
    # turn code to hexadecimal
    from_code = DC.uniToHex(from_code)

    en = DESEncode()
    string_len = len(from_code)

    if string_len < 1:
        print 'error input'
        return False
    key_code = en.encode(from_code, key, string_len)
    return key_code




