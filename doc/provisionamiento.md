# CREACIÓN Y PROVISIONAMIENTO

## Vagrantfile

El primer cometido de un Vagrantfile es describir qué tipo de máquina requiere el proyecto y cómo se va a configurar. Vagrant genera un entorno fácil de configurar, reproducible y portable que consigue construir nuestra aplicación en un único flujo consistente. En mi caso, construyo una máquina virtual en Azure y una red virtual privada con la que conectar mi máquina virtual y mi base de datos. Debido a las necesidades de mi proyecto, la base de datos está basada en un grafo y aprovechando las herramientas que Microsoft Azure nos da, he elegido Gremlin (GDB) dentro de CosmosDB.  

Para poder crear esta máquina, es necesario tener un Service Principal y un grupo de recursos.

La máquina virtual generada tiene las siguientes características:

- Sistema operativo: Ubuntu Server 16.04 LTS
- Tamaño: Standard_F1
- Localización: Sur de Reino Unido

### Provisionamiento con Ansible

Ansible es el software que he elegido para provisionar la máquina recién creada. La orden de provisionamiento se da también en el Vagrantfile, haciendo referencia al *playbook.yml* que se ha definido previamente. Paso a describir mi *playbook.yml*:  

Con la idea de hacerlo más automatizable, genero un archivo *var.yml* donde especifico los paquetes que quiero que se instalen, de forma en que en el *playbook.yml* sólo tengo qu hacer referencia al anterior para que se instalen. Entre esos paquetes se encuentran build-essential, git, python3, python3-setuptools, python3-pip, libpq-dev. Además, instalo gunicorn.