# Importa la biblioteca 'requests' para realizar solicitudes HTTP.
import requests
# Importa la biblioteca 'json' para trabajar con datos en formato JSON.
import json 

# Este script de Python realiza una solicitud GET a la API de Fake Store para obtener información sobre todos los productos disponibles.
def get_products():
    # Realiza una solicitud GET a la API de Fake Store para obtener todos los productos.
    response = requests.get('https://fakestoreapi.com/products')

    # Convierte la respuesta de la API a formato JSON.
    result =  response.json()

    # Imprime el resultado en un formato JSON legible.
    print(json.dumps(result, indent=4))

# Este script de Python realiza una solicitud GET a la API de Fake Store para obtener información sobre un producto especifico
def get_one_product(id):
    # Realiza una solicitud GET a la API de Fake Store para obtener informacion de un producto especifico.
    response = requests.get(f'https://fakestoreapi.com/products/{id}')

    # Convierte la respuesta de la API a formato JSON.
    result =  response.json()

    # Imprime el resultado en un formato JSON legible.
    print(json.dumps(result, indent=4))


#agrega un nuevo producto a la API de Fake Store.
def create_product():

    # Crea un diccionario 'data' con información de un nuevo producto.
    data = {
        "titulo": "new product",
        "descripcion": "new product description",
        "price": 12.50,
        "image": "https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg",
        "category": "electronic"
    }

    # Realiza una solicitud POST a la API de Fake Store para agregar un nuevo producto. transforma la data en formato json
    response = requests.post('https://fakestoreapi.com/products', json=data)

    # Convierte la respuesta de la API a formato JSON.
    result =  response.json()

    # Imprime el contenido de la respuesta en formato JSON con indentación de 2 espacios para una presentación más ordenada.
    print(json.dumps(result, indent=2))

    print('The new product has been created successfully.')


#actualiza un producto a la API de Fake Store
def update_product(id):
    data={
        "titulo": "new product",
        "descripcion": "new product description",
        "price": 12.50,
        "image": "https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg",
        "category": "electronic"
    }
    # Realiza una solicitud PUT a la API de Fake Store para actualizar un producto. transforma la data en formato json
    response = requests.put(f'https://fakestoreapi.com/products/{id}', json=data)

    # Convierte la respuesta de la API a formato JSON.
    result =  response.json()

    # Imprime el contenido de la respuesta en formato JSON con indentación de 2 espacios para una presentación más ordenada.
    print(json.dumps(result, indent=2))

    print('The product has been updated successfully.')


#elimina un producto a la API de Fake Store
def delete_product(id):
    # Realiza una solicitud DELETE a la API de Fake Store para actualizar un producto
    response = requests.delete(f'https://fakestoreapi.com/products/{id}')

    # Convierte la respuesta de la API a formato JSON.
    result =  response.json()

    # Imprime el contenido de la respuesta en formato JSON con indentación de 2 espacios para una presentación más ordenada.
    print(json.dumps(result, indent=2))

    print('The product has been deleted successfully.')


def login():
    # Datos del usuario
    data={
        "username":"mor_2314",
        "password":"83r5^_",
    }   

    # Realiza una solicitud POST a la API de Fake Store para logear
    response = requests.post(' https://fakestoreapi.com/auth/login', json=data)

    # Imprime el contenido de la respuesta en formato JSON con indentación de 2 espacios.
    print('your token is ' + json.dumps(response.json(), indent=2))

#  función de inicio.
def init():
   
    # Imprime las opciones disponibles para el usuario.
    print('1. Get all the products')
    print('2. Get specific  product')
    print('3. Register a new product')
    print('4. Update an existing product')
    print('5. Delete an existing product')
    print('6. Log in')
    print('')

    # Solicita al usuario que ingrese una opción y convierte la entrada en un entero.
    option = int(input('Choose the option you desire: '))   

    print('')

    # Si el usuario elige la opción 1...
    if option == 1:
        # Llama a la función 'get_products'.
        get_products()
    # Si el usuario elige la opción 2...
    if option == 2:
        id= int(input('Enter the ID: '))
        # Llama a la función 
        get_one_product(id)
    # Si el usuario elige la opción 3...
    if option == 3:
        create_product()
    # Si el usuario elige la opción 3...
    if option == 4:
        id= int(input('Enter the ID: '))
        update_product(id)
    
    if option == 5:
        id= int(input('Enter the ID: '))
        delete_product(id)

    if option == 6:
        login()


   
# Verifica si este script está siendo ejecutado directamente y no importado como un módulo.
if __name__ == '__main__':
    # Si el script se está ejecutando directamente, llama a la función 'get_products'.
    init()
