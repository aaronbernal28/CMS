from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def mesetaMasLarga(l: List[int]) -> int :
  res: int
  if len(l) == 0:
    res = 0
  else:
    res = maximo(listaDeMesetas(l))
  return res

def maximo(ls: List[int]) -> int:
  res: int = ls[0]
  for l in ls:
    if l >= res:
      res = l
  return res

def listaDeMesetas(ls: List[int]) -> List[int]:
  apariciones = 0
  lista: list = []
  for i in range(len(ls)-1,-1,-1):
    apariciones += 1
    if ls[i] != ls[i-1]:
      lista.append(apariciones)
      apariciones = 0
  lista.append(apariciones)
  return lista

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))