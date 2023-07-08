from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue, stock_productos: Dict[str, int], precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  res: List[Dict[str, Union[int, str, float, Dict[str, int]]]] = []
  for i in range(pedidos.qsize()):
    pedido: Dict[str, Union[int, str, float, Dict[str, int]]] = pedidos.get()
    pedido_copia = pedido.copy()
    pedidos.put(pedido_copia)
    pedido_procesado: Dict[str, Union[int, str, float, Dict[str, int]]] = procesar_pedido(pedido, stock_productos, precios_productos)
    res.append(pedido_procesado)
  return res

def procesar_pedido(pedido: Dict[str, Union[int, str, float, Dict[str, int]]], stock_productos: Dict[str, int], precios_productos: Dict[str, float]) -> Dict[str, Union[int, str, float, Dict[str, int]]]:
  precio_total: float = 0
  estado: str = "completo"
  productos: Dict[str, int] = pedido["productos"]
  for producto, cantidad in productos.items():
    precio: float = precios_productos[producto]
    if stock_productos[producto] < cantidad:
      productos[producto] = stock_productos[producto]
      precio_subtotal = precio * stock_productos[producto]
      estado = "incompleto"
      stock_productos[producto] = 0
    else:
      stock_productos[producto] -= cantidad
      precio_subtotal = precio * cantidad
    precio_total += precio_subtotal
  pedido["precio_total"] = precio_total
  pedido["estado"] = estado
  return pedido

if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))

# Ejemplo input  
#pedidos: [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
#stock_productos: {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
#precios_productos: {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}
