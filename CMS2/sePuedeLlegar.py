from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  largoDeRuta: int = len(ruta(origen, destino, vuelos)) - 1
  return largoDeRuta

def ruta(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
  ruta: List[Tuple[str, str]] = [("","")]
  i: int = 0
  while ruta[len(ruta)-1][1] != destino:
    for vuelo in vuelos:
      if vuelo[0] == origen:
        ruta.append(vuelo)
        origen = vuelo[1]
    i += 1
    if i > len(vuelos)**len(vuelos):
      return []
  return ruta

if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))