#ESTE SE UTILIZA PARA IMPORTAR DE MANERA LOCAL NUESTROS ARCHIVOS DE PYTHON(Como /mvn clean package en Java)
#Re utilice lo hecho anteriormente para aprender buenas prácticas y mas maneras de hacer el setup
from setuptools import setup, find_packages

"""V146
Configuración del distribuible(paquete que exportaremos a diferentes proyectos para re utilizar contenido)
Para ejecutar se utiliza en la terminal - "python setup.py sdist" parecido a "mvn clean package"
Despues de que nos génere el archivo "dist/*.tar.gz" hay que ir a su ruta desde la terminal
Y ejecutar "pip install mensajes-1.0.tar.gz"
Posteriormente nos instalara el paquete localmente, con "pip list" podemos ver todos los paquetes instalados de python
Ahora podre utilizarlos en cualquier lugar donde lo importe(Jupyther, terminal, archivos, etc)"""
setup(
    name             = 'mensajes',
    version          = '4.0',
    description      = 'Paquete para saludar y despedir',
    author           = 'Irving Mauricio Silva Rivera',
    author_email     = 'multizato@...',
    url              = 'https.IrvingRivera.com',
    packages         = find_packages(),
    scripts          = [],
    test_suite       = 'tests',   #Para indicar donde tenemos las pruebas(Los diferentes tipos de archivos de testing, necesita el __init__ en el paquete)
    install_requires = [paquete.strip() for paquete in open("requirements.txt").readlines()] #Para los paquetes externos que deba instalar(La mejor forma es hacerlo en otro archivo "requirements.txt")
)                                                                                            #También utiliza el archivo "MANIFEST.in" para incluir el archivo "requirements.txt"
#Para desinstalar la versión anterior y actualizar por la nueva:
#Para actualizar la version se hace el mismo proceso pero al subirla se coloca "pip install mensajes-2.0.tar.gz --upgrade"
#Si no funciona hay que reiniciar el Kernel
#Si queremos eliminar el paquete es con "pip uninstall 'nombrePaquete'"


#También puedo manejar los test y la manera corresta es en la raíz crear la carpeta "tests" con el fichero
#Deberia haber un fichero "test" para cada paquete que estamos utilizando


""" Lo anterior fue distribución LOCAL
    También puedo almacenarlo de forma PÚBLICA, en "pypi.org" es donde estan todos los paquetes(librerias)
    que instalamos con el compando "pip install". Puedo crear cuenta y tener mis paquetes versionados alli.
    (Parecido al maven repository)
    En lugar de publicar en "pypi.org" puedo usar "test.pypi.org", es un mirror de la página original
    pero es de prueba. Es mejor publicarlo primero en la cuenta de prueba(test) cuando todo funcione correctamente
    ahora si es la página original se puede publicar.
    Hay algunas recomendaciones para publicarlo PUBLICAMENTE para manejar bien los nombres, versiones, "README.md", etc.
    El README debe incluirse en el "MANIFEST.in" como todos los archivos que querramos añadir.
    El "setup()" se le pueden añadir mas campos según lo que necesitemos(Podemos tener Licencias(License),
    clasificadores(Classifiers), long_description, long_description_content_type, etc).
    Se debe instalar "build"(Para la construcción del paquete público) y "twine"(Para la publicación). 
    Comando "pip install build twine --upgrade" (--upgrade es por si los tengo desactualizados)
    Ahora podre generar la nueva version con "python -m build"
    Y "python -m twine check dist/*" para poder publicarlos(Solo debo tener las que desplegare, los versiones LOCALES NO)
    "python -m twine upload -r testpypi dist/*" para poder subirlos en el servidor de pruebas(Pedira autenticación)
    Si todo sale bien, dara un enlace que nos llevara al repositorio donde he subido mi libreria(paquete)
    Ahora puedo desplegar en el repositorio que no es test con el mismo comando "python -m twine upload dist/*"(Sitio Oficial)
"""