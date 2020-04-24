import socket
import time
import binascii
from os import system, name
import string

invOffset = '0xAC4723D0'
countOffset = '0xAC4723D4'

def clear(): 
    if name == 'nt': 
        time.sleep(2)
        _ = system('cls')  
        spawnItem() 
    else: 
        time.sleep(2)
        _ = system('clear') 
        spawnItem()

def is_hex(s):
     hex_digits = set(string.hexdigits)
     return all(c in hex_digits for c in s)

def formatID(x):
    IDStr = str(x)
    
    if( len(IDStr) > 4):
        print("input too large.")
        clear()
    if ( len(IDStr) <= 4 ):
        n0 = "0" * ( 4 - len(IDStr) )
        #print(n0 + IDStr)
        preString = n0 + IDStr
        first, second = preString[:int(len(preString)/2)], preString[int(len(preString)/2):]
        fString = second + first
        return fString

def sendCommand(s, content):
    content += '\r\n'
    s.sendall(content.encode())
    print(content)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#change the connection info here.
s.connect(("192.168.254.85", 6000))





def spawnItem():
    user_input = input("Enter ItemID: ")
    if(is_hex(user_input)):
        itemString = "0x" + formatID(user_input)
        
        pokeString = f"poke {invOffset} {itemString}"

        sendCommand(s, pokeString.format(invOffset, itemString)) 
        
        itemCount = input("How Many?: ")

        if(is_hex(itemCount)):
            sendCommand(s, f"poke {countOffset} {hex(int(itemCount) - 1)}") 
            print("Item(s) sent!")
            clear()
        else:
            print("error, sent 1")
            clear()

    else:
        print("numbers only, dunce.")
        clear()


spawnItem()
