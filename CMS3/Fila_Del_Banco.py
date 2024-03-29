from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int):
  orden_disponible: int = fila.qsize() + 1
  min_persona_caja_3: int = -1
  persona_caja_3: int = -1
  for i in range(min+1):
    if pasaron_n_minutos(i, 4): #se_forma_una_persona_cada_4_min
      persona_nueva: int = orden_disponible
      fila.put(persona_nueva)
      orden_disponible += 1
    if min_persona_caja_3 >= 0: #se_forma_persona_caja_3
      min_persona_caja_3 += 1
      if min_persona_caja_3 == 3:
        fila.put(persona_caja_3)
        min_persona_caja_3 = -1
    if pasaron_n_minutos(i - 1 , 10) and i >= 1 and not fila.empty(): #caja_1
      fila.get()
    if pasaron_n_minutos(i - 3 , 4) and i >= 3 and not fila.empty(): #caja_2
      fila.get()
    if pasaron_n_minutos(i - 2, 4) and i >= 2 and not fila.empty(): #caja_3
      persona_caja_3 = fila.get()
      min_persona_caja_3 = 0

def pasaron_n_minutos(min: int, n: int) -> bool:
  return min % n == 0

if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero)
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)


# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)

