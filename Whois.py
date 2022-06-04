from os import system, name
import pystyle
from pystyle import Colorate, Colors, Center

def lookup():
    host = input('\n-> Host or ip Address % ')
    print('\n')
    system('whois '+ host)
     
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

header = """ 
 ██     ██░ ██░ ██  ▒█████   ██▓  ██████ 
▓██░ █ ░██░▓██░ ██▒▒██▒  ██▒▓██▒▒██    ▒ 
▒██░ █ ░██ ▒██▀▀██░▒██░  ██▒▒██▒░ ▓██▄   
░██░ █ ░██ ░▓█ ░██ ▒██   ██░░██░  ▒   ██▒
░░░███▒█▓ ░▓█▒░██▓░ ████▓▒░░██░▒██████▒▒
░ ▓░▒ ▒   ▒ ░░▒░▒░ ▒░▒░▒░ ░▓  ▒ ▒▓▒ ▒ ░
  ▒ ░ ░   ▒ ░▒░ ░  ░ ▒ ▒░  ▒ ░░ ░▒  ░ ░
  ░   ░   ░  ░░ ░░ ░ ░ ▒   ▒ ░░  ░  ░  
    ░     ░  ░  ░    ░ ░   ░        ░  
                                       """
if name == 'nt':
    system('cls')
else:
    system('clear')

print(Colorate.Horizontal(Colors.rainbow, Center.Center(header)))


while True:

    command = input('\nWHOIS % ')
    if command == "help":
        print(Colorate.Horizontal(Colors.rainbow,'\nlook at README.md'))

    if command == "lookup":
        lookup()

    if command == "exit":
        quit()
    
    if command == "clear":
        clear()
    
    if command == "restart":
        clear()
        print(Colorate.Horizontal(Colors.rainbow, Center.Center(header)))
                        