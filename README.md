# Reto Técnico Backend 💻
REST API para gestión de tareas, la cual permite:

  - Registrar y autenticar usuarios.
  - Crear, actualizar y eliminar tareas.
  - Marcar tareas como completa/incompleta.
  - Buscar tareas por descripción.

---

## Tabla de contenido  📄
1. [Requerimientos](#requerimientos-⚙️)
2. [Instalación](#instalación--🚀)
3. [Endpoints](#endpoints-🔩)
    - [Registro](#registro--registration-👤)
    - [Inicio de sesión](#inicio-de-sesión--login🔒🔓)
    - [Obtener listado de tareas](#obtener-listado-de-tareas--rest_apiget_tasks📋)
    - [Crear tareas](#crear-tareas--rest_apiadd_task-➕)
    - [Actualizar tareas](#actualizar-tareas--rest_apiupdate_taskid🔄)
    - [Eliminar tareas](#eliminar-tareas--rest_apidelete_taskid➖)
    - [Buscar tareas por descripción](#buscar-tareas-por-descripción--rest_apisearch_task-🔍)
    - [Marcar tareas como Completas/Incompletas](#marcar-tareas-como-completasincompletas--rest_apichange_stateid-✔️-❌)
4. [Pruebas unitarias](#pruebas-unitarias-💣)
5. [Autor](#autor-✒️)

 ---
    
### Requerimientos ⚙️
  - Python versión 3

---

### Instalación  🚀

  - Clonar repositorio
    ```sh
        git clone https://github.com/CristianAlba75/Technical-Test-Backend.git
    ```
  - Crear entorno virtual local, ya sea con **pipenv** o **virtualenv**.
  - Instalar requerimientos del proyecto.
    ```sh
        pip install -r requirements.txt
    ```
 - Hacer migraciones.
    ```sh
        python manage.py makemigrations
        python manage.py migrate
    ```
 - Ejecutar servidor.
    ```sh
        python manage.py runserver
    ```
    
---
### Endpoints 🔩

Los endpoints del REST API son:

| Acción | Url |
| ------ | ------ |
| Registro | /registration |
| Inicio de sesión | /login |
| Obtener tareas del usuario | /rest_api/get_tasks |
| Crear tareas | /rest_api/add_task |
| Actualizar tareas | /rest_api/update_task/<id>|
| Eliminar tareas | /rest_api/delete_task/<id> |
| Buscar tareas por descripción  | /rest_api/search_task |
| Marcar tareas como Completas/Incompletas | /rest_api/change_state |

 A continuación se detalla cada uno de los endpoints del REST API.
 
 ---
 
 #### Registro  `/registration` 👤
 Este endpoint permite hacer el registro e inicio de sesión de usuarios. Recibe 3 parámetros:
 
| Parámetro | Descripción | Requerido | Tipo |
| ------ | ------ |  ------ | ------ |
| username | Nombre de usuario | Si | String |
| password1 | Contraseña 1 | Si | String |
| password2 | Contraseña 2 | Si | String |

El **body** de la petición es de la siguiente forma:
 
```json
{
    "username":"testuser", 
    "password1":"testpassword", 
    "password2":"testpassword"
}
```
 
 Como resultado, este endpoint retorna un token único para cada usuario:
 ```json
{
    "key": "asd0cfbf0a39a63c65rttg6cdf9a80dc1ear6hki"
}
```

---

 #### Inicio de sesión  `/login`🔒🔓
 Este endpoint permite hacer inicio de sesión de usuarios. Recibe 3 parámetros:
 
| Parámetro | Descripción | Requerido | Tipo |
| ------ | ------ | ------ | ------ |
| username | Nombre de usuario | Si | String |
| email | Correo usuario | No | String |
| password | Contraseña usuario | Si | String |

El **body** de la petición es de la siguiente forma:
 
```json
{
    "username": "testuser",
    "email": "",
    "password": "testpassword"
}
```
 
 Como resultado, este endpoint retorna un token único para cada usuario, el cual se usará para la gestión de tareas (crear, actualizar, eliminar, búsquedas, listado de tareas):
 ```json
{
    "key": "540cfbf0a39a63c6511d47ecdf9a80dc1ea36bdd"
}
```

---

 #### Obtener listado de tareas  `/rest_api/get_tasks`📋
 Este endpoint permite consultar el listado de tareas asociadas al usuario autenticado. Las tareas se muestran paginadas, una tarea por página.

En el **header** de la petición se debe enviar el token generado en el inicio de sesión:
 
| Key | Value | Description |
| ------ | ------ | ------ |
| Authorization | Token 540cfbf0a39a63c6511d47ecdf9a80dc1ea36bdd |  |
 
 Como resultado, este endpoint retorna la lista de tareas asociadas al usuario autenticado, indicando la cantidad de tareas con los enlaces **anterior** y **siguiente** para navegar entre ellas:
 
 ```json
{
    "count": 2,
    "next": "http://127.0.0.1:8000/rest_api/get_tasks?page=2",
    "previous": null,
    "results": [
        {
            "id": 3,
            "title": "Task 3",
            "description": "Test task 3",
            "status": false,
            "owner": 1
        }
    ]
}
```

---

 #### Crear tareas  `/rest_api/add_task` ➕
 Este endpoint permite crear tareas y asociaralas al usuario autenticado. Recibe 3 parámetros:
 
| Parámetro | Descripción | Requerido | Tipo |
| ------ | ------ | ------ | ------ | 
| title | Título de la tarea | Si | String |
| description | Descripción de la tarea | Si | String |
| status | Estado de la tarea Completa/Incompleta | Si | Boolean |

En el **header** de la petición se debe enviar el token generado en el inicio de sesión:
 
| Key | Value | Description |
| ------ | ------ | ------ |
| Authorization | Token 540cfbf0a39a63c6511d47ecdf9a80dc1ea36bdd |  |

El **body** de la petición es de la siguiente forma:
 
```json
{
    "title":"Task 4", 
    "description":"Test task 4", 
    "status":false
}
```
 
 Como resultado, este endpoint retorna la tarea creada con la información relacionada
 ```json
{
    "tasks": {
        "id": 4,
        "title": "Task 4",
        "description": "Test task 4",
        "status": false,
        "owner": 1
    }
}
```

---

 #### Actualizar tareas  `/rest_api/update_task/<id>`🔄
 Este endpoint permite actualizar tareas asociadas al usuario autenticado. En la url se envía el id de la tarea a actualizar.Recibe 3 parámetros:
 
| Parámetro | Descripción | Requerido | Tipo |
| ------ | ------ | ------ | ------ | 
| title | Título de la tarea | No | String |
| description | Descripción de la tarea | No | String |
| status | Estado de la tarea Completa/Incompleta | No | Boolean |

En el **header** de la petición se debe enviar el token generado en el inicio de sesión:
 
| Key | Value | Description |
| ------ | ------ | ------ |
| Authorization | Token 540cfbf0a39a63c6511d47ecdf9a80dc1ea36bdd |  |

El **body** de la petición es de la siguiente forma:
 
```json
{
    "title":"Task 3 updated", 
    "description":"Test task 3 updated", 
    "status":true
}
```
 
 Como resultado, este endpoint retorna la tarea con la información actualizada:
 ```json
{
    "tasks": {
        "id": 3,
        "title": "Task 3 updated",
        "description": "Test task 3 updated",
        "status": true,
        "owner": 1
    }
}
```

---

 #### Eliminar tareas  `/rest_api/delete_task/<id>`➖
 Este endpoint permite eliminar tareas asociadas al usuario autenticado. En la url se envía el id de la tarea a eliminar.Recibe 3 parámetros:
 

En el **header** de la petición se debe enviar el token generado en el inicio de sesión:
 
| Key | Value | Description |
| ------ | ------ | ------ |
| Authorization | Token 540cfbf0a39a63c6511d47ecdf9a80dc1ea36bdd |  |

 
 Como resultado, este endpoint retorna el estado **204 No Content**.

---

 #### Buscar tareas por descripción  `/rest_api/search_task` 🔍
 Este endpoint permite buscar tareas asociadas al usuario autenticado por la descripción. Recibe 1 parámetro:
 
| Parámetro | Descripción | Requerido | Tipo |
| ------ | ------ | ------ | ------ | 
| description | Descripción de la tarea | Si | String |

En el **header** de la petición se debe enviar el token generado en el inicio de sesión:
 
| Key | Value | Description |
| ------ | ------ | ------ |
| Authorization | Token 540cfbf0a39a63c6511d47ecdf9a80dc1ea36bdd |  |

El **body** de la petición es de la siguiente forma:
 
```json
{
    "description":"task"
}
```
 
 Como resultado, este endpoint retorna la(s) tarea(s) cuya descripción contenga el valor enviado para la búsqueda:
 ```json
{
  "task": [
        {
            "id": 3,
            "title": "Task 3 updated",
            "description": "Test task 3 updated ",
            "status": true,
            "owner": 1
        },
        {
            "id": 4,
            "title": "Task 4",
            "description": "Test task 4",
            "status": false,
            "owner": 1
        }
    ]
}
```

---

 #### Marcar tareas como Completas/Incompletas  `/rest_api/change_state/<id>` ✔️ ❌
 Este endpoint permite cambiar el estado de las tareas asociadas al usuario autenticado, como **completas** o **incompletas**. En la url se envía el id de la tarea a actualizar.Recibe 1 parámetro:
 
| Parámetro | Descripción | Requerido | Tipo |
| ------ | ------ | ------ | ------ | 
| status | Estado de la tarea Completa/Incompleta | Si | Boolean |

En el **header** de la petición se debe enviar el token generado en el inicio de sesión:
 
| Key | Value | Description |
| ------ | ------ | ------ |
| Authorization | Token 540cfbf0a39a63c6511d47ecdf9a80dc1ea36bdd |  |

El **body** de la petición es de la siguiente forma:
 
```json
{
    "status":false
}
```
 
 Como resultado, este endpoint retorna la tarea con el estado actualizado:
 ```json
{
    "tasks": {
        "id": 3,
        "title": "Task 3 updated",
        "description": "Test task 3 updated",
        "status": false,
        "owner": 1
    }
}
```

---

### Pruebas Unitarias 💣

Para ejecutar las pruebas unitarias ejecutar:

   ```sh
       python manage.py test
   ```
<sub><sup>Debe estar ubicado el directorio en donde se encuentra el archivo manage.py.</sup></sub>
---

### Autor ✒️

Desarrollado por Cristian Eduardo González Alba
📧 <ingcristianalba@gmail.com>
📇 <https://www.linkedin.com/in/cristian-eduardo-gonz%C3%A1lez-alba-583359150/>
 🛠️<https://github.com/CristianAlba75/Technical-Test-Backend>