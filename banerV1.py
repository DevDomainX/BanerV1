#!/usr/bin/env python3
import os
from colorama import init, Fore, Style
init()

rojo = Fore.RED+Style.BRIGHT
azul = Fore.BLUE+Style.BRIGHT 
verde = Fore.GREEN+Style.BRIGHT
cyan = Fore.CYAN+Style.BRIGHT 
blanco = Fore.WHITE+Style.BRIGHT
os.system("clear")
os.system("pkg install update -y")
os.system("pkg install upgrade -y")
os.system("pkg install figlet")
os.system("clear")
print("Elije un color a eleccion \n\n")
print("[1] - ROJO\n[2] - AZUL\n[3] - VERDE\n[4] - CYAN\n[5] - BLANCO")
color = int(input("Ingrese el color que desea agregar: "))
if color == 1:
    name = input(rojo+"Ingresa el baner: ")
if color == 2:
    name = input(azul+"Ingresa el baner: ")
if color == 3:
    name = input(verde+"Ingresa el baner: ")
if color == 4:
    name = input(cyan+"Ingresa el baner: ")
if color == 5:
    name = input(blanco+"Ingresa el baner: ")
else:
    print("Tienes que ingresar un dijito valido")
os.system("clear")
os.system("figlet "+name)
print("\nCreated by: Hans Saldias")