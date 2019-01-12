#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from fabric.api import cd, run, sudo, shell_env

def InstalarApp():
    run('git clone https://github.com/luisbalru/TwitterLocationFlow.git')
    with cd('TwitterLocationFlow'):
        run('pip3 install --user -r requirements.txt')
        run('mkdir Errors')


def ActualizarApp():
    with cd('TwitterLocationFlow'):
        run('git pull')
        run('pip3 install --user -r requirements.txt')


def IniciarApp():
     # Iniciamos el servicio web.
    ActualizarApp()
    with shell_env(C_URL='wss://twitterlocationflow.gremlin.cosmosdb.azure.com:443',C_USER=os.environ['CLIENT_USERNAME'], C_PASS = os.environ['CLIENT_PASSWD']):
        run('cd TwitterLocationFlow && python src/genera_credenciales.py $C_URL $C_USER $C_PASS')
        sudo('nohup gunicorn app:app -b 0.0.0.0:80 & echo $! > ~/pid.txt')

def KillApp():
    sudo('pkill gunicorn')
