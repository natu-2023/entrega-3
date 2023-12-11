Mi Proyecto tiene la siguiente estructura en Django:
el proyecto se llama ProyetoFinal
Creamos una Aplicacion llamada AppCoder, y la integran los siguientes archivos:

   Directorio: C:\Users\sistemas01\Documents\coder\entregas\entrega-3\ProyectoFinal\AppCoder


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-r---        11/12/2023     13:47                migrations
d-r---        10/12/2023     10:43                static
d-r---        10/12/2023     10:43                templates
d-r---        11/12/2023     15:53                __pycache__
-a----        10/12/2023     18:24            178 admin.py
-a----        10/12/2023     12:38            152 apps.py
-a----        11/12/2023     13:54            431 forms.py
-a----        11/12/2023     15:18            475 models.py
-a----        06/12/2023     20:19             63 tests.py
-a----        11/12/2023     15:52            690 urls.py
-a----        11/12/2023     15:52           3064 views.py
-a----        06/12/2023     20:19              0 __init__.py

en templates/AppCoder
  C:\Users\sistemas01\Documents\coder\entregas\entrega-3\ProyectoFinal\AppCoder\templates\AppCoder


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        10/12/2023     18:21            781 disfraces_buscar.html
-a----        10/12/2023     18:19            644 disfraces_formulario.html
-a----        10/12/2023     15:43            268 disfraces_list.html
-a----        10/12/2023     12:01            127 inicio.html
-a----        10/12/2023     15:57           5157 padre.html
-a----        10/12/2023     18:26            659 tipo_disfraces_formulario.html
-a----        11/12/2023     14:03            311 tipo_disfraces_list.html

creamos  siete html.
tenemos un padre.html que heredan las demas html.
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-r---        11/12/2023     13:47                migrations
d-r---        10/12/2023     10:43                static
d-r---        10/12/2023     10:43                templates
d-r---        11/12/2023     15:53                __pycache__
-a----        10/12/2023     18:24            178 admin.py
-a----        10/12/2023     12:38            152 apps.py
-a----        11/12/2023     13:54            431 forms.py
-a----        11/12/2023     15:18            475 models.py
-a----        06/12/2023     20:19             63 tests.py
-a----        11/12/2023     15:52            690 urls.py
-a----        11/12/2023     15:52           3064 views.py
-a----        06/12/2023     20:19              0 __init__.py


en esta estructura creamos el archivo forms en el cual lo conforman tres clases de formulario que las vistas invocaran.

class disfracesbuscarformulario(forms.Form):
    nombre = forms.CharField(label='nombre', max_length=30, required=True)

class disfracesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    precio = forms.IntegerField()

class tipodisfracesFormulario(forms.Form):
    clase = forms.CharField(max_length=30)
    talle = forms.IntegerField()
    cantidad = forms.IntegerField()

luego creaos en models nuestras clases los cuales interactuaran con nuestra base de datos creando dos tablas, Disfraces y TipoDisfraces compuestas cada una como se detalla a continuacion:

class Disfraces(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} ({self.precio})"

class TipoDisfraces(models.Model):
    clase = models.CharField(max_length=30)
    talle = models.IntegerField()
    cantidad = models.IntegerField()

   
    def __str__(self):
        return f"{self.clase} ({self.talle}) ({self.cantidad})"

Luego tenemos nuestras vistas en views en las cuales crearemos nuestras logicas y funciones las cuales seran invocadas por nuestras urls.
En las vistas crearemos nuestras funciones e invocaremos las clases de python para que reciban una solicitud web y devuelven una respuesta web. GET y POST.

La arquitectura Django sigue la estructura MVT. En MVT, M significa Modelo, V significa vistas y T significa Plantillas . El modelo es la estructura para almacenar los datos en la base de datos, la vista es una función de Python que se utiliza para manejar la solicitud web y la plantilla contiene contenido estático como HTML, CSS y Javascript.

EXPLICARE DE MANERA BREVE LA FUNCIONALIDAD DE MI PROYECTO UNA VEZ QUE CORRE EL SERVIDOR:

LO PRIMERO QUE ME MUESTRA ES LO SIGUIENTE:
Using the URLconf defined in ProyectoFinal.urls, Django tried these URL patterns, in this order:

1-admin/
2-AppCoder/ inicio/ [name='inicio']
3-AppCoder/ disfraces/ [name='disfraces']
4-AppCoder/ disfraces_buscar/ [name='disfraces_buscar']
5-AppCoder/ disfraces_todos/ [name='disfraces_todos']
6-AppCoder/ tipo_disfraces/ [name='tipo_disfraces']
7-AppCoder/ tipo_disfraces_todos/ [name='tipo_disfraces_todos']


ME DA PARA ELEGIR QUE DESEO VER:
1-Es el administrador en el cual ingresaremos con el super usuario que hemos creado.
2-Inicio, seria nuestra pagina Home, cada vez que terminamos algun proceso vuelve a esta pagina.
3-en disfraces, me permite dar de alta nuevos disfraces, colocaremos los nombres de cada uno y el precio correspondiente de cada uno. los mismos me los guarda en la tabla Disfraces en nuestra base de datos.
4-en disfraces_buscar, podemos generar una busqueda individual de un disfraz para poder ver su precio, lo buscamos por el nombre guardado en la base de datos.
5-disfraces_todos, no tira un listado de todos los disfraces guardados en la base de datos, nombre y precio.
6- tipo_disfraces, esta opcion nos deja dar de alta de nuevo el nombre del disfraz, pero es mas para llevar un control de que de ese disfraz colocar el talle del mismo y que cantidad tengo disponible, por lo que se pueden repetir los nombres de disfraces ya que de un disfraz xx hay varios talles, 6-8-10-12-16 y tengo disponible yy cantidad de cada uno de ellos.
7- me permite tirar un listado para control de todos los disfraces, que talles dispongo y que cantidades de cada disfraz y de cada talle.
todo lo trae de la tabla en la base de datos llamada TipoDisfraces


Se que es Breve pero tengo mucha ambicion de ampliar este proyecto mas adelante incorporando mas opciones, como una galeria de fotos de los disfraces por ejemplo.

saludos cordiales
Atte. Beka Natalia Erica

        

