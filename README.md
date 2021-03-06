# Reto T茅cnico Backend 馃捇
REST API para gesti贸n de tareas, la cual permite:

  - Registrar y autenticar usuarios.
  - Crear, actualizar y eliminar tareas.
  - Marcar tareas como completa/incompleta.
  - Buscar tareas por descripci贸n.

---

## Tabla de contenido  馃搫
1. [Requerimientos](#requerimientos-鈿欙笍)
2. [Instalaci贸n](#instalaci贸n--馃殌)
3. [Endpoints](#endpoints-馃敥)
    - [Registro](#registro--registration-馃懁)
    - [Inicio de sesi贸n](#inicio-de-sesi贸n--login馃敀馃敁)
    - [Obtener listado de tareas](#obtener-listado-de-tareas--rest_apiget_tasks馃搵)
    - [Crear tareas](#crear-tareas--rest_apiadd_task-鉃?)
    - [Actualizar tareas](#actualizar-tareas--rest_apiupdate_taskid馃攧)
    - [Eliminar tareas](#eliminar-tareas--rest_apidelete_taskid鉃?)
    - [Buscar tareas por descripci贸n](#buscar-tareas-por-descripci贸n--rest_apisearch_task-馃攳)
    - [Marcar tareas como Completas/Incompletas](#marcar-tareas-como-completasincompletas--rest_apichange_stateid-鉁旓笍-鉂?)
4. [Pruebas unitarias](#pruebas-unitarias-馃挘)
5. [Autor](#autor-鉁掞笍)

 ---
    
### Requerimientos 鈿欙笍
  - Python versi贸n 3

---

### Instalaci贸n  馃殌

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
### Endpoints 馃敥

Los endpoints del REST API son:

| Acci贸n | Url |
| ------ | ------ |
| Registro | /registration |
| Inicio de sesi贸n | /login |
| Obtener tareas del usuario | /rest_api/get_tasks |
| Crear tareas | /rest_api/add_task |
| Actualizar tareas | /rest_api/update_task/<id>|
| Eliminar tareas | /rest_api/delete_task/<id> |
| Buscar tareas por descripci贸n  | /rest_api/search_task |
| Marcar tareas como Completas/Incompletas | /rest_api/change_state |

 A continuaci贸n se detalla cada uno de los endpoints del REST API.
 
 ---
 
 #### Registro  `/registration` 馃懁
 Este endpoint permite hacer el registro e inicio de sesi贸n de usuarios. Recibe 3 par谩metros:
 
| Par谩metro | Descripci贸n | Requerido | Tipo |
| ------ | ------ |  ------ | ------ |
| username | Nombre de usuario | Si | String |
| password1 | Contrase帽a 1 | Si | String |
| password2 | Contrase帽a 2 | Si | String |

El **body** de la petici贸n es de la siguiente forma:
 
```json
{
    "username":"testuser", 
    "password1":"testpassword", 
    "password2":"testpassword"
}
```
 
 Como resultado, este endpoint retorna un token 煤nico para cada usuario:
 ```json
{
    "key": "asd0cfbf0a39a63c65rttg6cdf9a80dc1ear6hki"
}
```

---

 #### Inicio de sesi贸n  `/login`馃敀馃敁
 Este endpoint permite hacer inicio de sesi贸n de usuarios. Recibe 3 par谩metros:
 
| Par谩metro | Descripci贸n | Requerido | Tipo |
| ------ | ------ | ------ | ------ |
| username | Nombre de usuario | Si | String |
| email | Correo usuario | No | String |
| password | Contrase帽a usuario | Si | String |

El **body** de la petici贸n es de la siguiente forma:
 
```json
{
    "username": "testuser",
    "email": "",
    "password": "testpassword"
}
```
 
 Como resultado, este endpoint retorna un token 煤nico para cada usuario, el cual se usar谩 para la gesti贸n de tareas (crear, actualizar, eliminar, b煤squedas, listado de tareas):
 ```json
{
    "key": "540cfbf0a39a63c6511d47ecdf9a80dc1ea36bdd"
}
```

---

 #### Obtener listado de tareas  `/rest_api/get_tasks`馃搵
 Este endpoint permite consultar el listado de tareas asociadas al usuario autenticado. Las tareas se muestran paginadas, una tarea por p谩gina.

En el **header** de la petici贸n se debe enviar el token generado en el inicio de sesi贸n:
 
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

 #### Crear tareas  `/rest_api/add_task` 鉃?
 Este endpoint permite crear tareas y asociaralas al usuario autenticado. Recibe 3 par谩metros:
 
| Par谩metro | Descripci贸n | Requerido | Tipo |
| ------ | ------ | ------ | ------ | 
| title | T铆tulo de la tarea | Si | String |
| description | Descripci贸n de la tarea | Si | String |
| status | Estado de la tarea Completa/Incompleta | Si | Boolean |

En el **header** de la petici贸n se debe enviar el token generado en el inicio de sesi贸n:
 
| Key | Value | Description |
| ------ | ------ | ------ |
| Authorization | Token 540cfbf0a39a63c6511d47ecdf9a80dc1ea36bdd |  |

El **body** de la petici贸n es de la siguiente forma:
 
```json
{
    "title":"Task 4", 
    "description":"Test task 4", 
    "status":false
}
```
 
 Como resultado, este endpoint retorna la tarea creada con la informaci贸n relacionada
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

 #### Actualizar tareas  `/rest_api/update_task/<id>`馃攧
 Este endpoint permite actualizar tareas asociadas al usuario autenticado. En la url se env铆a el id de la tarea a actualizar.Recibe 3 par谩metros:
 
| Par谩metro | Descripci贸n | Requerido | Tipo |
| ------ | ------ | ------ | ------ | 
| title | T铆tulo de la tarea | No | String |
| description | Descripci贸n de la tarea | No | String |
| status | Estado de la tarea Completa/Incompleta | No | Boolean |

En el **header** de la petici贸n se debe enviar el token generado en el inicio de sesi贸n:
 
| Key | Value | Description |
| ------ | ------ | ------ |
| Authorization | Token 540cfbf0a39a63c6511d47ecdf9a80dc1ea36bdd |  |

El **body** de la petici贸n es de la siguiente forma:
 
```json
{
    "title":"Task 3 updated", 
    "description":"Test task 3 updated", 
    "status":true
}
```
 
 Como resultado, este endpoint retorna la tarea con la informaci贸n actualizada:
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

 #### Eliminar tareas  `/rest_api/delete_task/<id>`鉃?
 Este endpoint permite eliminar tareas asociadas al usuario autenticado. En la url se env铆a el id de la tarea a eliminar.Recibe 3 par谩metros:
 

En el **header** de la petici贸n se debe enviar el token generado en el inicio de sesi贸n:
 
| Key | Value | Description |
| ------ | ------ | ------ |
| Authorization | Token 540cfbf0a39a63c6511d47ecdf9a80dc1ea36bdd |  |

 
 Como resultado, este endpoint retorna el estado **204 No Content**.

---

 #### Buscar tareas por descripci贸n  `/rest_api/search_task` 馃攳
 Este endpoint permite buscar tareas asociadas al usuario autenticado por la descripci贸n. Recibe 1 par谩metro:
 
| Par谩metro | Descripci贸n | Requerido | Tipo |
| ------ | ------ | ------ | ------ | 
| description | Descripci贸n de la tarea | Si | String |

En el **header** de la petici贸n se debe enviar el token generado en el inicio de sesi贸n:
 
| Key | Value | Description |
| ------ | ------ | ------ |
| Authorization | Token 540cfbf0a39a63c6511d47ecdf9a80dc1ea36bdd |  |

El **body** de la petici贸n es de la siguiente forma:
 
```json
{
    "description":"task"
}
```
 
 Como resultado, este endpoint retorna la(s) tarea(s) cuya descripci贸n contenga el valor enviado para la b煤squeda:
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

 #### Marcar tareas como Completas/Incompletas  `/rest_api/change_state/<id>` 鉁旓笍 鉂?
 Este endpoint permite cambiar el estado de las tareas asociadas al usuario autenticado, como **completas** o **incompletas**. En la url se env铆a el id de la tarea a actualizar.Recibe 1 par谩metro:
 
| Par谩metro | Descripci贸n | Requerido | Tipo |
| ------ | ------ | ------ | ------ | 
| status | Estado de la tarea Completa/Incompleta | Si | Boolean |

En el **header** de la petici贸n se debe enviar el token generado en el inicio de sesi贸n:
 
| Key | Value | Description |
| ------ | ------ | ------ |
| Authorization | Token 540cfbf0a39a63c6511d47ecdf9a80dc1ea36bdd |  |

El **body** de la petici贸n es de la siguiente forma:
 
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

### Pruebas Unitarias 馃挘

Para ejecutar las pruebas unitarias ejecutar:

   ```sh
       python manage.py test
   ```
<sub><sup>Debe estar ubicado el directorio en donde se encuentra el archivo manage.py.</sup></sub>
---

### Autor 鉁掞笍

Desarrollado por Cristian Eduardo Gonz谩lez Alba
馃摟 <ingcristianalba@gmail.com>
馃搰 <https://www.linkedin.com/in/cristian-eduardo-gonz%C3%A1lez-alba-583359150/>
 馃洜锔?<https://github.com/CristianAlba75/Technical-Test-Backend>