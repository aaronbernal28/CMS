from queue import LifoQueue

# para el tipo pila de enteros, usar: "pila: LifoQueue". La notación "pila: LifoQueue[int]" no funciona.
def calcular_expresion(expr: str) -> float:
  pila: LifoQueue = LifoQueue()
  for elem in expr.split():
    if elem == "+":
      pila = sumar(pila)
    elif elem == "*":
      pila = multiplicar(pila)
    elif elem == "-":
      pila = restar(pila)
    elif elem == "/":
      pila = dividir(pila)
    else:
      pila.put(float(elem))
    pilaLista = list(pila.queue)
  return pila.get()

def sumar(pila: LifoQueue) -> LifoQueue:
  res: float = pila.get()
  res += pila.get()
  pila.put(res)
  return pila

def multiplicar(pila: LifoQueue) -> LifoQueue:
  res: float = pila.get()
  res *= pila.get()
  pila.put(res)
  return pila

def restar(pila: LifoQueue) -> LifoQueue:
  res: float = pila.get()
  res = pila.get() - res
  pila.put(res)
  return pila

def dividir(pila: LifoQueue) -> LifoQueue:
  res: float = pila.get()
  res = pila.get() / res
  pila.put(res)
  return pila

if __name__ == '__main__':
  x = input() # Por ejemplo: 2 5 * 7 +
  print(round(calcular_expresion(x), 5))