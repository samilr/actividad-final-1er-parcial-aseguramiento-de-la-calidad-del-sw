# Generando el archivo README.md con las instrucciones proporcionadas

readme_content = """
# README - Instrucciones para Pruebas Unitarias

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
