import sys

class ceaser():
    def __init__(self, parameter):
        self.__k = parameter
        self.__limit_upperCase = 90
        self.__limit_lowerCase = 122
        self.__limit_abc = 26
        self.result = ""
        
    def encrypt(self, text):
        result = ""
        mod = self.__k % self.__limit_abc

        if(mod > 0):
            for letter in text:
                code_ascii = ord(letter) 
                if((code_ascii >= 65 and code_ascii <= 90) or (code_ascii >= 97 and code_ascii <= 122)):
                    position = code_ascii + mod
                    if (letter.isupper()):
                        if position > self.__limit_upperCase:
                            result += chr(position - 26)
                        else:
                            result += chr(position)
                    else:
                        if position > self.__limit_lowerCase:
                            result += chr(position - 26)
                        else:
                            result += chr(position)
                else:
                    result += letter
        else:
            result = text    
        self.result = result
    
    def printCipherText(self):
        print("ciphertext:", self.result)

if __name__ == "__main__":

    if( len(sys.argv) == 2):
        try:
            k = int(sys.argv[1])
            if(k>0):
                newCeaser = ceaser(k)
                plaintext = input("plaintext: ")
                newCeaser.encrypt(plaintext)
                newCeaser.printCipherText()
                del newCeaser
            else:
                print("negative argument")    
        except:
            print("Error: data format")
            print("Usage: python caesar.py k")
            exit(1)
    else:
        print("Usage: python caesar.py k")
        exit(1)