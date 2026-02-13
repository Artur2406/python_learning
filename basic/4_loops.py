## slicing con lista
## ejm:
my_list = [1, 2, 3]
# my_list_slicing = my_list[0:2:2]  # 3 creo aprenderlo usando ia o docs de internet
# print(my_list_slicing)


"""
 Uso de for:
"""


# con enumerate


# con range


# con objetos, MyObjet   lo mas usados   .items() -> te retorna key y value,    .values -> te retorna los valores ,   .keys -> te retorna las keys

fruta = {"id": 1, "name": "Apple"}

# De cada propiedad key: value (id, 1), (name, apple) <- esto es una tupla (elemnts..),   cuando el dicionario {} tiene un metodo items() que te retorna una lista de tuplas [(key,value)]
for key, value in fruta.items():
    print(f"Key del objeto: {key} con valor: {value}")


"""
 Uso de while
"""
i = 0

while i < 5:
    i += 1
    print(f"contador usando while: {i}")
