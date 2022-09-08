from clases import cliente_classic
from clases import cliente_gold
from clases import cliente_black
from scripts.creadorHTML import generate_html

try:
    cliente_class = cliente_classic.Classic()
    cliente_gold = cliente_gold.Gold()
    cliente_black = cliente_black.Black()
except FileNotFoundError:
    print("Alguno de los archivos json no existe")
    exit()
generate_html(cliente_class, cliente_gold, cliente_black)

#ejecutar main.py para crear los index