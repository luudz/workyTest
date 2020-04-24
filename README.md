# workyTest
> Contiene el código correspondiente a la solución de la PRUEBA WORKY.

## Descripción de la aplicación
La aplicación requiere 3 entradas principales, al ejecutar el código, se irán solicitando una por una en la consola:

- Nombre del reddit (ej. lotr)
- Cantidad de post a clasificar (ej. 100)
- Lista de palabras clave para filtrar, separadas por una coma (ej, frodo,bilbo,sam,merry,pippin,gollum)

Posteriormente, se dará la opción de unificar filtros (ej. SAM y SAMSAGAZ, como uno solo), si el usuario acepta unificar filtros, se le requerirán dos entradas más, por cada grupo de filtros a unificar:

- Lista de filtros que serán unificados
- Nombre con el que se unificarán los filtros

Este proceso se repetirá hasta que el usuario responda que NO desea unificar más filtros.

Una vez que se reciben las 3 entradas, y los filtros unificados, si es el caso, se mostrarán dos campos de salida:

- Post clasificados por las palabras clave guardadas en los filtros, en formato JSON.
- Filtro con más post.

Además que a los post de filtro más popular se les realizará un upvote.

## Demo de ejecución

Se ejecutó la aplicación con los valores del ejemplo anterior:
![Entrada de datos](/images/input_lotr.png)

![Salida al ejecutar](/images/output_lotr.png)

Se volvió a ejecutar el código con diferentes entradas:
- Subreddit: Python
- Cantidad de post: 100
- Filtros: writing,codding,working,doing,script,learn,node,mongo,website

![Entrada de datos](/images/input_python.png)
![Salida al ejecutar](/images/output_python.png)

## Pre-requisitos
* [Python v3.5+](https://www.python.org/downloads/)
* [Python pip](https://pip.pypa.io/en/stable/installing/)
* [PRAW v6.5.1](https://praw.readthedocs.io/en/latest/getting_started/installation.html)

## Descripción del ambiente

- SO: Ubuntu 18.04.4 
- Python 3.6.9 (La versión mínima requerida por paw en la 3.5)
- SublimeText 3 como editor de Textos
- Terminal del Sistema

El mismo código también fue probado satisfactoriamente bajo el siguiente ambiente:
- SO: Debian GNU/Linux 10(buster)
- Python 3.7.3
- Terminal del sistema

## Ejecución del código

> En una terminal, moverse hasta el directorio contenedor del código

> Ejecutar el siguiente comando:

```python3 workyTest.py```



