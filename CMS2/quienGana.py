import sys

def quienGana(j1: str, j2: str) -> str : 
    res: str
    if gana(j1,j2):
       res = "Jugador1"
    elif gana(j2,j1):
       res = "Jugador2"
    else:
       res = "Empate"
    return res

def gana(j1: str, j2: str) -> bool:
   res: bool = piedraGanaAtijera(j1,j2) or tijeraGanaAPapel(j1,j2) or papelGanaAPiedra(j1,j2)
   return res

def piedraGanaAtijera(j1: str, j2: str) -> bool:
   res: bool = j1 == "Piedra" and j2 == "Tijera"
   return res

def tijeraGanaAPapel(j1: str, j2: str) -> bool:
   res: bool = j1 == "Tijera" and j2 == "Papel"
   return res

def papelGanaAPiedra(j1: str, j2: str) -> bool:
   res: bool = j1 == "Papel" and j2 == "Piedra"
   return res

if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))