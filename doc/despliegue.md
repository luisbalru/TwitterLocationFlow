# DESPLIEGUE CON FABRIC

Para el despliegue utilizo la herramienta Fabric. [Aquí](http://docs.fabfile.org/en/2.4/) está la documentación oficial.

En el fabfile.py defino tres funciones:

- InstalarApp: Hace un clon del proyecto de Github, instala sus dependencias y crea el directorio Errors (para las salidas de nohup)
- ActualizarApp: En el directorio del proyecto hace un pull e instala las nuevas dependencias (si hubiere).
- IniciarApp: ActualizaApp, genera variables de entorno, se las pasa a la máquina remota y genera credenciales allí y, por último, ejecuta la aplicación.
- KillApp: Al lanzar la app, guardo un fichero el número del PID de ese proceso. Cuando se lanza KillApp, se recupera el contenido de ese fichero y se detiene el proceso.

Estas funciones son llamadas a través de los scripts install.sh (crea la máquina, la provisiona e instala la app), run.sh y kill.sh, tomando el papel de botón para instalar, ejecutar y acabar la app.

**Creando la máquina virtual y provisionando con Ansible**

![actualizar](images/instalando1.png)

**Instalando App**

![instalando2](images/instalando2.png)

**Instalando dependecias**
![instalando3](images/instalando3.png)

**Creando Carpeta de errores**

![instalando4](images/instalando4.png)

**Ejecutando la App**

![ejecutando1](images/ejecutando1.png)

**Generando credenciales y lanzando app**
![ejecutando2](images/ejecutando2.png)

**Comprobando que hay un proceso en ejecución de gunicorn**
![prueba-ejecución](images/ejecucion.png)

**Prueba en el navegador**

![funcionando](images/prueba.png)

**REFERENCIAS**
- [Fabricate your automated devops environment using python](https://www.youtube.com/watch?v=g4rCFMWAwgo)
