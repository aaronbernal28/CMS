import sys
from typing import List

def fibonacciNoRecursivo(n: int) -> int:
  res: int = secuenciaFibonacciNoRecursivo(n)[n]
  return res

def secuenciaFibonacciNoRecursivo(n: int) -> List[int]:
  ls: List[int] = [0,1]
  l: int
  for i in range(n-1):
    l = ls[len(ls)-1] + ls[len(ls)-2]
    ls.append(l)
  return ls

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))