from ast import Pass
from distutils.log import error
from turtle import st
import paramiko 
from colorama import Back, init, Fore

init()
"""Colores uwu"""
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET
BLUE = Fore.BLUE

def main():
    #Variables de authenticacion
    print(Fore.GREEN + "Ingresar ip: ")
    ip = input(">>: ")
    print(Fore.GREEN + "Ingresar usuario: ")
    user = str(input(">>: "))
    port = 22
    print(Fore.GREEN + "Ingresar password: ")
    Passw = str(input(">>: "))

    #se inicializa el cliente ssh
    ssh_client = paramiko.SSHClient()
    #se cargan las hotkeys
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try: 
        ssh_client.connect(hostname=ip, port=port, username=user, password=Passw)
        print(Fore.GREEN + "Se pudo conectar, la contraseña es: " + Passw)
    except ValueError:
        print("Hubo un error al momento de conectarse")
        

main()
