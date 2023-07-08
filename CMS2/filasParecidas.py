from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def filasParecidas(matriz: List[List[int]]) -> bool :
  res: bool = True
  cantidadFilas: int = len(matriz)
  if cantidadFilas == 1:
    return True
  else:
    fila1 = matriz[0]
    fila2 = matriz[1]
    filaN = restarFilas(fila2,fila1)
    if todosIguales(filaN):
      for i in range(1,cantidadFilas-1):
        filaActual: List[int] = matriz[i]
        filaSiguiente: List[int] = matriz[i+1]
        if sumarFilas(filaActual,filaN) != filaSiguiente:
          return False
      return True
    else:
      return False

def todosIguales(fila: List[int]) -> bool:
  res: bool = True
  cantidadColumnas: int = len(fila)
  for i in range(cantidadColumnas - 1):
    if fila[i] != fila[i+1]:
      res = False
  return res

def sumarFilas(fila1: List[int], fila2: List[int]) -> List[int]:
  cantidadColumnas: int = len(fila1)
  suma: List[int] = []
  for i in range(cantidadColumnas):
    suma.append(fila1[i] + fila2[i])
  return suma

def restarFilas(fila1: List[int], fila2: List[int]) -> List[int]:
  cantidadColumnas: int = len(fila1)
  resta: List[int] = []
  for i in range(cantidadColumnas):
    resta.append(fila1[i] - fila2[i])
  return resta

if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))