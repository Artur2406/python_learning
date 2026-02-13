# que es una lista, como agregar elementos y quitar elementos
elementos = ["primero", "segundo", "tercero"]
"""
list = []
"""
my_list = [
    1,
    "ariku",
    {"key": "value"},
    ["otra", "lista"],
    None,
]  # una lista puede tener elementos de todo tipo
print(f"my lista: {my_list}")
# la forma en la que se agrega elementos y se quita depende mucho,
# hay una estructura de datos llamado Colas y Pilas  (Youtube) Fifo y Lifo (https://www.noegasystems.com/blog/logistica/fifo-y-lifo-tecnicas-de-almacenaje)
# segun el caso


print("CON LA ESTRUCUTRA COLAS, FIFO. Primero en entrar es el Primero en Salir")
# ejemplo de cola (Queue) FIFO -> First In First out
my_cola = []
# el append agrega un elemento y lo pone al ultimo   1 -> [a]  |  2 -> [a,b]  | 3 -> [a,b,c]
# my_cola.append("primero")
# my_cola.append("segundo")
# my_cola.append("tercero")

for persona_lugar in elementos:
    print(f"entro el {persona_lugar} a la cola")
    my_cola.append(persona_lugar)


print(f"mi cola se encuentra en este estado:  {my_cola}")
# en este caso usaremos pop ya que solo existe esto en python
# con el pop le pasaremos el indice de nuestro elemento a remover, en este caso iteraremos del 0 al [CANTIDAD MAXIMA DE LA LISTA] para ir removiendo 1 por 1
# y nosotros debemos quitar el primero segun nuestra Estructura de Datos FIFO

# ejm de como se va 1 por 1 con FIFO
for _ in range(len(my_cola)):
    se_fue = my_cola.pop(0)  # Ponemos 0 porque se ira removiendo de la lista osea, step 1 -> [a,b,c].pop(0) -> [b,c].pop(0) -> [c].pop(0)
    print(f"se fue el {se_fue}")

print(f"mi cola se encuentra en este estado:  {my_cola}")


print("CON LA ESTRUCUTRA PILAS, LIFO. Ultimo en entrar es el Primero en Salir")
# ejemplo de pilas (Stack) LIFO -> Last In First out
# en este caso con Pila se trabaja de manera que el primero en entrar es el ULTIMO en salir, a diferencia del FIFO que salia el primer elemento.
my_pila = []

# igualmente con append para agregar elementos de por si es una lista, la diferencia es como nosotros lo manejamos
# my_pila.append("primero")
# my_pila.append("segundo")
# my_pila.append("tercero")
for persona_lugar in elementos:
    print(f"entro el {persona_lugar} a la pila")
    my_pila.append(persona_lugar)

print(f"mi pila se encuentra en este estado:  {my_pila}")
for i in range(len(my_pila)):
    se_fue = my_pila.pop() # por defecto ya tiene -1, con -1 le estamos indicando que quiero que retires el ULTIMO elemento
    print(f"se fue el {se_fue}")

print(f"mi pila se encuentra en este estado:  {my_pila}")

# Conclusion: estos tipos de estrucutras FIFO y LIFO se usan para manejo de ordenes en la que quieres ir enviando cierta accion por ejemplo
# la mas facil es la de una impresa, donde vas metiendo un archivo, y el primero que entra es el primero que sale ( FIFO) usarias la estructura de cola
# porque al usuario le importa la primera cosa que insertó y no que le traigas copias en diferentes ordenes

# usaria pila en casos donde (https://www.mecalux.es/blog/metodo-lifo) <- info

"""
set = set()
"""
my_list_con_mucha_data = [1, 2, 3, 53, 5, 2, 23, 5, 1, 2, 3, 5, 23]
# normalmente usas set para pasar una lista con data repetida a una donde nose repite, y set funciona de esta manera
no_repetidos_set = set(my_list_con_mucha_data)
print(
    f"Set no permite elementos repetidos, set(params) <- al insertar los datos dentro del set() internamente quitara los que se repiten:"
)
print(f"anteriormenta era una lista: {my_list_con_mucha_data}")
print(f"con set termina siendo asi: {no_repetidos_set}")


"""
La tupla es una lista inmutable (que no pueden cambiar sus vales o tirara una exception)
tupla = (...elements)
"""
my_tupla = (1, 2, 3, 3, 3, 3, 3, 3, 3)
# my_tupla[0] = "ariku" # <- error, no puedes mutar, con mutar se refiere a cambiar algo del origen  # TypeError: 'tuple' object does not support item assignment

# Metodos más usados de una tupla
# count ->
cantidad_repetidos = my_tupla.count(3)  # das el elemento que deseas saber sus repetidos
print(f"Se repitio el número 3 estas veces: {cantidad_repetidos}")


"""
diccionario = {}
"""

my_ariku  = {"level": 0, "name": "ariku", "games": ["genshin","endfield","honkai star rail", "zenless zero"]}

print("esto es un diccionario, o objeto como desees llamarlo")
print(my_ariku)
