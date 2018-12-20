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
import os
from fabric.api import cd, run, sudo, shell_env



def Borrar():
    # Borramos antiguo codigo
    run('sudo rm -rf TwitterLocationFlow')


def Actualizar():

    # Borramos antiguo codigo
    Borrar()

    # Descargamos nuevo repositorio
    run('git clone https://github.com/luisbalru/TwitterLocationFlow.git')

    # Instalamos requirements
    run('pip3 install --user -r TwitterLocationFlow/requirements.txt')


def Iniciar():
     # Iniciamos el servicio web
    with shell_env(C_URL="'wss://twitterlocationflow.gremlin.cosmosdb.azure.com:443'",C_USER=os.environ['CLIENT_USERNAME'], C_PASS = os.environ['CLIENT_PASSWD']):
        run('echo $C_USER && cd TwitterLocationFlow && sudo gunicorn app:app -b 0.0.0.0:80')