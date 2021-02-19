# Requirements
- Python3
- Python3 virtualenv

# Installation
###### For debian based OS

```
$ cd project_folder
$ python3 -m venv venv
$ source venv/bin/activate
$ cd over_roasted
$ python3 -m pip install -r requirements.txt
```
Django
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

## Next steps

El test fue realizado en django principalmente.

Debido al tiempo limitado del test, no se ha podido probar ni programar todos los escenarios posibles. Para exitar errores inesperados, por favor sigue los siguientes pasos :D

Además te estoy compartiendo la base de datos en un documento, usando sqlite3. ya hay dos usuarios creados, las credenciales son (user1: admin123, user2:admin123). Si se desea crear más usuarios, adelante :)


* Create a user
* Login
* Create a recipe
* Vote

Si se desea crear otro usuario, sigue los pasos de arriba de nuevo.

* See results


# Test challenges:

* Registro de Recetas:

Cada visitante puede registrar recetas nuevas, solo debe indicar su correo, el nombre de la receta y sus ingredientes (max 200 caracteres).
Cada visitante puede registrar solo 1 receta nueva cada 5 min.

-------------

**Hecho: a diferencia de registrar el correo para crear la receta, he realizado una authenticación de usuarios. Los usuarios pueden registrar una receta cada 5 minutos.**

**Si no deseas esperar 5 min para crear más recetas, comenta todo el método save() de la clase Recipe en el archivo recipes/models.py**
 
-------
* Votación:

Cada visitante podrá votar por una receta anteriormente registrada, solo 1 vez cada 2min.
Para votar por una receta debe indicar su correo electrónico.
Solo se permitirá la siguiente escala de valores para los votos:  -5, -2, -1, 1, 2, 5
Cada visitante podrá votar todas las recetas registradas si así lo desea
Las recetas deberán mostrarse aleatoriamente y el visitante podrá indicar “PASO” para pasar a la siguiente sin registrar su voto en caso de no haber probado esa receta anteriormente.

-------

**Hecho: Se puede hacer skip de las recetas, ellas se irán mostrando de manera aleatoria y se puede votar con las puntuaciones solicitadas.**

**También hay reestricción de votar cada 2 min. Si deseas saltarte eso, comenta el método save() de la clase RecipeRanking en el archivo recipes/models.py**

------
 

* Resultados:

Se debe mostrar el conteo y porcentaje de las 10 recetas más votadas de los últimos: 1 día, 1 hora, 15 min.
Se debe mostrar nuestro comensal más exigente. Para esto considerar: la diferencia entre su mejor voto y el promedio de sus votos, la proporción entre sus votos y aquel que registro la mayor cantidad de votos..
(MAX_voto_visitante – Prom_votos_visitante) * (Cont_votos_visitante/ Max_cont_votos_visitantes)
El más exigente será aquel que tiene el producto más alto de la diferencia entre su mejor voto y el promedio de sus votos, y el cociente del total de sus votos entre el total de votos de aquel con más votos registrados en recetas.
Se debe mostrar nuestro comensal mas conformista. (Indique el criterio con el cual realiza el calculo para determinarlo)  
Se debe mostrar los ingredientes más comunes en las recetas

---------

**Todos los resultados fueron hechos. El criterio del coensal más conformista es: el que menos votó.**

**Lo único que me faltó fue mostrar los ingredientes más usados. la razón es que me di cuenta de esto al final y ya se me acaba el tiempo :( no sería muy complicado implementarlo. Solo habria que hacer un ManyToManyField y bueno, luego contar cual es el que está mayormente presente en la base de datos.**

**La app es responsive. No le hice deploy en Heroku porque me faltó tiempo :(**
