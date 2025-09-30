import os
import sys
import time


def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para macOS y Linux
        os.system('clear')


def lista_categoria():
    print_centered("""
_______________________________________________
| 1)Equipamientos        || 2) Ropa/Accesorios|
|                        ||                   |
|---------------------------------------------|
| 3)Suplementos/nutricion|| 4)Servicios       |
|_____________________________________________|
""")


def cargando(texto, duracion=3):
    for _ in range(duracion):
        for i in range(4):
            sys.stdout.write(f'\r{texto}{"." * i}   ')
            sys.stdout.flush()
            time.sleep(0.5)
    sys.stdout.write('\r')


def print_colored(text, color='white', delay=0.03):
 colors = {
     'red': '\033[91m',
     'green': '\033[92m',
     'yellow': '\033[93m',
     'blue': '\033[94m',
     'purple': '\033[95m',
     'cyan': '\033[96m',
     'white': '\033[97m',
     'end': '\033[0m'
 }

 for char in text:
     print(colors[color] + char, end='', flush=True)
     time.sleep(delay)
 print(colors['end'])

def print_centered(text, width=80):
    """Imprime el texto centrado en una línea de ancho especificado."""
    lines = text.split('\n')
    for line in lines:
        print(line.center(width))

def print_bold(text):
    """Imprime el texto en negrita."""
    print(f'\033[1m{text}\033[0m')
