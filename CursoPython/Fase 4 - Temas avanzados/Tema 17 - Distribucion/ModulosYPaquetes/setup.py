#ESTE SE UTILIZA PARA IMPORTAR DE MANERA LOCAL NUESTROS ARCHIVOS DE PYTHON(Como /mvn clean package en Java)
from setuptools import setup

#V146
#Configuración del distribuible(paquete que exportaremos a diferentes proyectos para re utilizar contenido)
#Para ejecutar se utiliza en la terminal - "python setup.py sdist" parecido a "mvn clean package"
#Despues de que nos génere el archivo "dist/*.tar.gz" hay que ir a su ruta desde la terminal
#Y ejecutar "pip install mensajes-1.0.tar.gz"
#Posteriormente nos instalara el paquete localmente, con "pip list" podemos ver todos los paquetes instalados de python
#Ahora podre utilizarlos en cualquier lugar donde lo importe(Jupyther, terminal, archivos, etc)
setup(
    name         = 'mensajes',
    version      = '2.0',
    description  = 'Paquete para saludar y despedir',
    author       = 'Irving Mauricio Silva Rivera',
    author_email = 'multizato@...',
    url          = 'https.IrvingRivera.com',
    packages     = ['mensajes', 'mensajes.saludos', 'mensajes.despedidas'],
    scripts      = ['test.py']
)
#Con esto desinstala la versión anterior e instala la nueva
#Para actualizar la version se hace el mismo proceso pero al subirla se coloca "pip install mensajes-2.0.tar.gz --upgrade"
#Si no funciona hay que reiniciar el Kernel
#Si queremos eliminar el paquete es con "pip uninstall 'nombrePaquete'"