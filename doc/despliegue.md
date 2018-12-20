# DESPLIEGUE CON FABRIC

Para el despliegue utilizo la herramienta Fabric. [Aquí](http://docs.fabfile.org/en/2.4/) está la documentación oficial.

En el fabfile.py defino tres funciones:

- Borrar: Elimina la carpeta del proyecto en la máquina remota
- Actualizar: Borra el proyecto, hace un nuevo clon del mismo e instala sus dependencias (requirements.txt)
- Iniciar: Pasa las variables de entorno necesarias para la app y la ejecuta.