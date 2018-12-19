#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Deployment of the app.
Copyright 2018, Luis Balderas Ruiz (luisbalderas@correo.ugr.es)
This program is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, version 3.
This program is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
"""
from fabric.api import cd, run, sudo, env

with shell_env(C_URL="CLIENT_URL",C_USER="CLIENT_USERNAME". C_PASS = "CLIENT_PASSWD")


def Borrar():

    # Borramos antiguo codigo
    run('rm -rf TwitterLocationFlow')


def Actualizar():

    # Borramos antiguo codigo
    Borrar()

    # Descargamos nuevo repositorio
    run('git clone https://github.com/luisbalru/TwitterLocationFlow.git')  

    # Instalamos requirements
    run('pip3 install -r TwitterLocationFlow/requirements.txt)


def Iniciar():
    
     # Iniciamos el servicio web
    run('echo $C_URL && cd TwitterLocationFlow && sudo gunicorn app:app -b 0.0.0.0:80')



