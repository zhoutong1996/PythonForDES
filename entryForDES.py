"""
# filename:entryForDES.py
# author:heizhou
# No.:150420226
# date:17/9/27
# purpose:all entry for des to encrypt .txt,password and img
"""
from encodeByDES import entry as encodeEntry
from decodeByDES import entry as decodeEntry
from dataConversion import uniToHex,hexToBina
import dateSource as DS
import os


class Entry():
    def __init__(self, mode=0):
        self.mode = mode

    def txtDES(self, mode):
        if mode == 1:
            """encode"""
            # read the file
            input = open('destest.txt', 'r')
            code = input.read()
            input.close()
            # output the data encoded into file
            output = open('encodedata.txt', 'w')
            output.write(encodeEntry(code, DS.key))
            output.close()
            path = "encode data in:" + os.path.dirname(os.path.realpath(__file__)) + "/encodedata.txt"
            print (path)
        elif mode == 2:
            """decode"""
            # decode the data
            input = open('encodedata.txt', 'r')
            code = input.read()
            input.close()
            # output the data decoded into file
            output = open('decodedata.txt', 'w')
            output.write(decodeEntry(code, DS.key).replace("\00", ""))
            output.close()
            path = "decode data in:" + os.path.dirname(os.path.realpath(__file__)) + "/decodedata.txt"
            print (path)

    def password(self, mode):
        if mode == 1:
            print "Please input your password:\n"
            password = str(raw_input())

            print "store password and encrypt it by des..."
            password = hexToBina(uniToHex(password), len(uniToHex(password)))[:64]

            # encode destest.txt with password
            input = open('destest.txt', 'r')
            code = input.read()
            input.close()
            # store encode data with password
            output = open('password.txt', 'w')
            output.write(encodeEntry(code, password))
            output.close()
            path = "encode password in:" + os.path.dirname(os.path.realpath(__file__)) + "/password.txt"
            print (path)
        elif mode == 2:
            print "Please input your password:\n"
            password = str(raw_input())
            password = hexToBina(uniToHex(password), len(uniToHex(password)))[:64]

            input = open('password.txt', 'r')
            code_encode = input.read()
            input.close()

            # encode destest.txt with password
            input = open('destest.txt', 'r')
            code = input.read()
            input.close()
            data = encodeEntry(code, password)
            if data == code_encode:
                print "your password is current"
            else:
                print "your password is wrong"

    def imgDES(self, mode):
        if mode == 1:
            """encode img"""
            img = open("dlam.jpg", "r")
            code = img.read()
            img.close()
            output = open('imgencode.jpg', 'w')
            output.write(encodeEntry(code, DS.key))
            output.close()
            path = "encode img in:" + os.path.dirname(os.path.realpath(__file__)) + "/imgencode.jpg"
            print (path)
        if mode == 2:
            """decode img"""
            input = open('imgencode.jpg', 'r')
            code = input.read()
            input.close()
            output = open('dlamdecode.jpg', 'w')
            output.write(decodeEntry(code, DS.key))
            output.close()
            path = "decode img in:" + os.path.dirname(os.path.realpath(__file__)) + "/dlamdecode.jpg"
            print (path)




    def run(self):
        if self.mode == 1:
            while(True):
                print "-----------------------------------------"
                print("1.encode destest.txt")
                print("2.decode the data")
                print("0.exit")
                mode = int(raw_input())
                if mode == 0:
                    break
                self.txtDES(mode)

        elif self.mode == 2:
            while (True):
                print "-----------------------------------------"
                print("1.encode dlam.jpg")
                print("2.decode imgencode.jpg")
                print("0.exit")
                mode = int(raw_input())
                if mode == 0:
                    break
                self.imgDES(mode)

        elif self.mode == 3:
            while (True):
                print "---------------------------------------"
                print("1.first input password")
                print("2.password authentication")
                print("0.exit")
                mode = int(raw_input())
                if mode == 0:
                    break
                self.password(mode)






if __name__ == '__main__':
    while(True):
        print "==========================================================="
        print("DES TEST:")
        print("   1. .txt")
        print("   2. img")
        print("   3. password")
        print("   0. exit\n")
        mode = int(raw_input())
        if mode == 0:
            break
        Entry(mode).run()
