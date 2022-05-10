import sys
import os
os.system("cls")
os.system("title ben's encryption")
print("""  _                                                       _   _             
 | |                                                     | | (_)            
 | |__   ___ _ __  ___    ___ _ __   ___ _ __ _   _ _ __ | |_ _  ___  _ __  
 | '_ \ / _ \ '_ \/ __|  / _ \ '_ \ / __| '__| | | | '_ \| __| |/ _ \| '_ \ 
 | |_) |  __/ | | \__ \ |  __/ | | | (__| |  | |_| | |_) | |_| | (_) | | | |
 |_.__/ \___|_| |_|___/  \___|_| |_|\___|_|   \__, | .__/ \__|_|\___/|_| |_|
                                               __/ | |                      
                                              |___/|_|                      """)  
print("Decode or Encode?")
optionselected = input("1 is encode, 2 is decode: ")
if optionselected == "1":
    nonencryptedtext = input("Enter text you wanna encrypt: ")
    if len(nonencryptedtext) < 4:
        print("TEXT MUST BE ATLEAST 5 CHARACTERS LONG!")
        input("Press enter to continue...")
        os.system("cls")
        os.system("title Command Prompt")
        sys.exit()
    encrypted = nonencryptedtext.replace('A', '01').replace('B', '02').replace('C', '03').replace('D', '04').replace('E', '05').replace('F', '06').replace('G', '07').replace('H', '08').replace('I', '09').replace('J', 'A').replace('K', 'B').replace('L', 'C').replace('M', 'D').replace('N', 'E').replace('O', 'F').replace('P', 'G').replace('Q', 'H').replace('R', 'I').replace('S', 'J').replace('T', 'K').replace('U', 'L').replace('V', 'M').replace('W', 'N').replace('X', 'O').replace('Y', 'P').replace('Z', 'Q').replace('a', '01').replace('b', '02').replace('c', '03').replace('d', '04').replace('e', '05').replace('f', '06').replace('g', '07').replace('h', '08').replace('i', '09').replace('j', 'A').replace('k', 'B').replace('l', 'C').replace('m', 'D').replace('n', 'E').replace('o', 'F').replace('p', 'G').replace('q', 'H').replace('r', 'I').replace('s', 'J').replace('t', 'K').replace('u', 'L').replace('v', 'M').replace('w', 'N').replace('x', 'O').replace('y', 'P').replace('z', '026').replace(' ', '+')
    print(encrypted)
    input("Press enter to continue...")
    os.system("cls")
    os.system("title Command Prompt")
    sys.exit()
elif optionselected == "2":
    encryptedtext = input("Enter text you wanna decrypt: ")
    if len(encryptedtext) < 4:
        print("TEXT MUST BE ATLEAST 5 CHARACTERS LONG!")
        input("Press enter to continue...")
        os.system("cls")
        os.system("title Command Prompt")
        sys.exit()
    nonencrypted = encryptedtext.replace('K', 'T').replace('L', 'U').replace('M', 'V').replace('N', 'W').replace('O', 'X').replace('P', 'Y').replace('Q', 'Z').replace('A', 'J').replace('B', 'K').replace('C', 'L').replace('D', 'M').replace('E', 'N').replace('F', 'O').replace('G', 'P').replace('H', 'Q').replace('I', 'R').replace('J', 'S').replace('01', 'A').replace('02', 'B').replace('03', 'C').replace('04', 'D').replace('05', 'E').replace('06', 'F').replace('07', 'G').replace('08', 'H').replace('09', 'I').replace('+', ' ')
    print(nonencrypted)
    input("Press enter to continue...")
    os.system("cls")
    os.system("title Command Prompt")
    sys.exit()
else:
    os.system("cls")
    os.system("title Command Prompt")
    sys.exit()