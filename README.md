
Instrucciones para Pruebas Unitarias

Este documento proporciona instrucciones detalladas sobre cómo realizar pruebas unitarias para una API que maneja libros y pedidos, utilizando `pytest` para Python. A continuación, se describen los pasos para la implementación de las pruebas, incluyendo los casos de uso, el diseño de las pruebas, la implementación en un repositorio de Git, y la documentación relevante.

---

## Casos de Uso

### Caso de Uso 1: Verificar el estado de la API
**Descripción**: El objetivo de este caso es verificar que el endpoint `/status` de la API devuelva el estado correcto del servidor, que debe ser `OK`.

**Pasos**:
1. Realizar una solicitud `GET` al endpoint `/status`.
2. Validar que el código de respuesta HTTP sea 200.
3. Verificar que la respuesta JSON contenga un campo `status` con el valor `'OK'`.

### Caso de Uso 2: Obtener todos los libros disponibles en la categoría "No Ficción"
**Descripción**: Este caso de uso verifica que la API devuelva correctamente los libros de tipo "no ficción" disponibles.

**Pasos**:
1. Realizar una solicitud `GET` al endpoint `/books`, con un parámetro de consulta `type=non-fiction`.
2. Validar que el código de respuesta HTTP sea 200.
3. Filtrar los libros que estén disponibles (`available == True`).
4. Verificar que haya al menos un libro disponible en la categoría "No Ficción".

### Caso de Uso 3: Obtener un libro específico
**Descripción**: El objetivo de este caso es asegurarse de que se pueda obtener la información de un libro en particular a partir de su `id`.

**Pasos**:
1. Realizar una solicitud `GET` al endpoint `/books/{book_id}`, donde `book_id` es el ID de un libro específico.
2. Validar que el código de respuesta HTTP sea 200.
3. Verificar que el campo `id` en la respuesta JSON coincida con el ID del libro solicitado.

### Caso de Uso 4: Realizar un pedido de un libro
**Descripción**: Este caso de uso verifica que un usuario pueda realizar un pedido de un libro, proporcionando el `bookId` y el nombre del cliente.

**Pasos**:
1. Realizar una solicitud `POST` al endpoint `/orders`, pasando los datos del libro y el nombre del cliente en el cuerpo de la solicitud.
2. Validar que el código de respuesta HTTP sea 201.
3. Asegurarse de que la respuesta contenga el campo `created` con valor `True` y un `orderId` único.

### Caso de Uso 5: Obtener todos los pedidos
**Descripción**: Este caso verifica que se puedan obtener todos los pedidos realizados, asegurándose de que la respuesta contenga la información correcta.

**Pasos**:
1. Realizar una solicitud `GET` al endpoint `/orders`.
2. Validar que el código de respuesta HTTP sea 200.
3. Verificar que la lista de pedidos no esté vacía.

---

## Diseño de Pruebas Unitarias

A continuación, se presentan las pruebas unitarias implementadas para cubrir los casos de uso mencionados.

### 1. Verificar el estado de la API

```python
def test_status_code():
    response = requests.get(f"{BASE_URL}/status")
    assert response.status_code == 200
    assert response.json()['status'] == 'OK'
```

### 2. Obtener libros de la categoría "No Ficción"

```python
def test_get_non_fiction_books():
    response = requests.get(f"{BASE_URL}/books", params={"type": "non-fiction"})
    assert response.status_code == 200
    books = response.json()
    non_fiction_books = [book for book in books if book['available'] == True]
    assert len(non_fiction_books) > 0, "No available non-fiction books found"
```

### 3. Obtener un libro específico

```python
def test_get_single_book():
    book_id = 1  
    response = requests.get(f"{BASE_URL}/books/{book_id}")
    assert response.status_code == 200
    book = response.json()
    assert book['id'] == book_id
```

### 4. Realizar un pedido de un libro

```python
def test_order_book():
    order_data = {
        "bookId": 1, 
        "customerName": "Samir"
    }
    response = requests.post(f"{BASE_URL}/orders", json=order_data, headers=headers)
    assert response.status_code == 201
```

### 5. Obtener todos los pedidos

```python
def test_get_all_orders():
    headers = {'Authorization': f'Bearer {TOKEN}'}
    response = requests.get(f"{BASE_URL}/orders", headers=headers)
    assert response.status_code == 200
    orders = response.json()
    assert len(orders) > 0, "No orders found"
```

### 6. Crear un nuevo pedido

```python
def test_create_order():
    data = {
        "bookId": 1,
        "customerName": "Alfreda"
    }
    response = requests.post(f"{BASE_URL}/orders", headers=headers, json=data)
    assert response.status_code == 201
    order = response.json()
    assert order['created'] is True
    assert 'orderId' in order
```

---

## Implementación en un Repositorio de Git

1. **Clonar el Repositorio**: Si aún no lo has hecho, clona el repositorio de tu proyecto.
   ```bash
   git clone "https://github.com/samilr/actividad-final-1er-parcial-aseguramiento-de-la-calidad-del-sw"
   ```

2. **Crear un Nuevo Archivo de Pruebas**: Crea un archivo llamado `test_book_api.py` y agrega las pruebas unitarias descritas arriba.

3. **Instalar Dependencias**:
   Si aún no tienes `requests` y `pytest` instalados, usa el siguiente comando:
   ```bash
   pip install requests pytest
   ```

4. **Ejecutar las Pruebas**: Para ejecutar las pruebas en el archivo, usa el siguiente comando:
   ```bash
   pytest test_book_api.py
   ```

5. **Subir los Cambios al Repositorio**:
   - Agrega los cambios al repositorio.
   ```bash
   git add test_book_api.py
   ```

   - Realiza un commit con un mensaje descriptivo.
   ```bash
   git commit -m "Añadidas pruebas unitarias para la API de libros"
   ```

   - Sube los cambios al repositorio remoto.
   ```bash
   git push origin main
   ```

---

## Documentación

- **`test_status_code`**: Verifica que la API esté operativa y que el endpoint `/status` devuelva un estado "OK".
- **`test_get_non_fiction_books`**: Se asegura de que los libros de la categoría "no ficción" estén disponibles y retornados correctamente.
- **`test_get_single_book`**: Valida que un libro específico se puede obtener correctamente usando su ID.
- **`test_order_book`**: Realiza un pedido para un libro específico y verifica que el pedido se crea correctamente.
- **`test_get_all_orders`**: Obtiene todos los pedidos realizados y verifica que la respuesta no esté vacía.
- **`test_create_order`**: Valida que la creación de un pedido sea exitosa y que contenga el campo `orderId` y `created`.

---

Con estos pasos, las pruebas unitarias cubrirán los casos de uso básicos de la API y se podrán ejecutar de manera confiable en cualquier entorno de desarrollo o CI/CD.
