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
optionselected = input("1 is decode, 2 is encode: ")
if optionselected == "2":
    nonencryptedtext = input("Enter text you wanna encrypt: ")
    if len(nonencryptedtext) < 4:
        print("TEXT MUST BE ATLEAST 5 CHARACTERS LONG!")
        input("Press enter to continue...")
        os.system("cls")
        os.system("title Command Prompt")
        sys.exit()
    encrypted = nonencryptedtext.replace('A', '01').replace('B', '02').replace('C', '03').replace('D', '04').replace('E', '05').replace('F', '06').replace('G', '07').replace('H', '08').replace('I', '09').replace('J', '010').replace('K', '011').replace('L', '012').replace('M', '013').replace('N', '014').replace('O', '015').replace('P', '016').replace('Q', '017').replace('R', '018').replace('S', '019').replace('T', '020').replace('U', '021').replace('V', '022').replace('W', '023').replace('X', '024').replace('Y', '025').replace('Z', '026').replace('a', '01').replace('b', '02').replace('c', '03').replace('d', '04').replace('e', '05').replace('f', '06').replace('g', '07').replace('h', '08').replace('i', '09').replace('j', '010').replace('k', '011').replace('l', '012').replace('m', '013').replace('n', '014').replace('o', '015').replace('p', '016').replace('q', '017').replace('r', '018').replace('s', '019').replace('t', '020').replace('u', '021').replace('v', '022').replace('w', '023').replace('x', '024').replace('y', '025').replace('z', '026').replace(' ', '+')
    print(encrypted)
    input("Press enter to continue...")
    os.system("cls")
    os.system("title Command Prompt")
    sys.exit()
elif optionselected == "1":
    encryptedtext = input("Enter text you wanna decrypt: ")
    if len(encryptedtext) < 4:
        print("TEXT MUST BE ATLEAST 5 CHARACTERS LONG!")
        input("Press enter to continue...")
        os.system("cls")
        os.system("title Command Prompt")
        sys.exit()
    nonencrypted = encryptedtext.replace('020', 'T').replace('021', 'U').replace('022', 'V').replace('023', 'W').replace('024', 'X').replace('025', 'Y').replace('026', 'Z').replace('010', 'J').replace('011', 'K').replace('012', 'L').replace('013', 'M').replace('014', 'N').replace('015', 'O').replace('016', 'P').replace('017', 'Q').replace('018', 'R').replace('019', 'S').replace('01', 'A').replace('02', 'B').replace('03', 'C').replace('04', 'D').replace('05', 'E').replace('06', 'F').replace('07', 'G').replace('08', 'H').replace('09', 'I').replace('+', ' ')
    print(nonencrypted)
    input("Press enter to continue...")
    os.system("cls")
    os.system("title Command Prompt")
    sys.exit()
else:
    os.system("cls")
    os.system("title Command Prompt")
    sys.exit()