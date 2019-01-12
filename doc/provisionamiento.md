# CREACIÓN Y PROVISIONAMIENTO

## Vagrantfile

El primer cometido de un Vagrantfile es describir qué tipo de máquina requiere el proyecto y cómo se va a configurar. Vagrant genera un entorno fácil de configurar, reproducible y portable que consigue construir nuestra aplicación en un único flujo consistente. En mi caso, construyo una máquina virtual en Azure y una red virtual privada con la que conectar mi máquina virtual y mi base de datos. Debido a las necesidades de mi proyecto, la base de datos está basada en un grafo y aprovechando las herramientas que Microsoft Azure nos da, he elegido Gremlin (GDB) dentro de CosmosDB.  

Para poder crear esta máquina, es necesario tener un Service Principal y un grupo de recursos.

La máquina virtual generada tiene las siguientes características:

- Sistema operativo: Ubuntu Server 16.04 LTS
- Tamaño: Standard_F1
- Localización: Sur de Reino Unido

Veamos línea a línea el contenido del Vagrantfile:

- Declaro una variable 'configuracion'. En ella, defino:
  - vm.box = 'mv-iv'
  - vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'
  (la aparición de estas líneas no está muy bien justificada aún. Sin ellas, la configuración falla. Según la documentación oficial, aquí se especifica con qué 'box' se levantará la máquina virtual).
  - vm.network "private_network". En mi caso, necesito una red virtual privada debido a que mi base de datos se ejecuta en otro microservicio propio de Azure llamado CosmosDB y, por motivos de seguridad, no debe estar accesible desde cualquier otra máquina.
  - ssh.private_key_path. Path para configurar la clave privada y conectar vía ssh con la máquina virtual.
- Declaro la variable 'az' como principal de la máquina virtual en Azure. En ella, defino:
  - vm_image_urn = 'Canonical:UbuntuServer:16.04-LTS:latest' como la imagen de SO que deseo en la MV.
  - vm_size = 'Standard_F1' características de la máquina deseada (1 core, 2GB RAM). Esta decisión se justifica como consecuencia de la necesidad de una base de datos de grafos, que a priori podía ser pesada (tipo neo4j). Más tarde decidí usar CosmosDB y como el precio no era muy alto, mantuve las características.
  - location = 'uksouth'
  - tcp_endpoints = 80 (Puertos TCP abiertos)
Y demás datos de la máquina virtual tales como su nombre, el grupo de recursos y todas las claves necesarias (conferidas por el Service Principal)


![creacion](images/up.png)

### Provisionamiento con Ansible

Ansible es el software que he elegido para provisionar la máquina recién creada. La orden de provisionamiento se da también en el Vagrantfile, haciendo referencia al *playbook.yml* que se ha definido previamente. Paso a describir mi *playbook.yml*:  

Para el correcto funcionamiento de mi app, es necesario tener  git, python (Python3) y sus herramientas. Por ello, utilizo un task con el módulo apt para instalar git, otro con un bucle para instalar todo lo concerniente a python (actualizando los repositorios previamente con *update_caché:yes*) y después tasks con comandos específicos para la actualizacion de pip.  
Como curiosidad, quiero comentar que en el Vagrantfile he añadido *run:always* para que cada vez que se ejecute, provisione la máquina.

![provisionamiento](images/provision.png)

**REFERENCIAS**

- [Documentación de Vagrant](https://www.vagrantup.com/docs/vagrantfile/)

- [Documentación de Vagrant-Azure](https://github.com/Azure/vagrant-azure#create-an-azure-active-directory-aad-application)

- [Ansible –6. Redactando un playbook](https://www.youtube.com/watch?v=Wuv0ZPOMLf0&list=PLTd5ehIj0goP2RSCvTiz3-Cko8U6SQV1P&index=6)

- [Iniciaciación a Ansible](https://www.youtube.com/watch?v=gFd9aj78_SM&t=1317s)
