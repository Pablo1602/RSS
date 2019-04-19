#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os import listdir
from os.path import isfile, join

import feedparser
import urllib2
import time

actual = os.getcwd()
fechayhora = time.strftime("%c")
print(actual)
print(fechayhora)

cuerpo = 0
topicos = 0
basura = 0
contador = 0

def sacarEntre(word):
    global basura, script
    if basura == 1:
        if word == "s":
            script = 1
            return 1
    if word == "/":
        script = 0
    if word == "<":
        basura = 1
    if word == ">":
        basura = 0
        return 1
    return 0

def sacarSaltoTab(word):
    if word == '\n' or word == '\t':
        return 1
    return 0

def sacarEspacioDoble(word):
    global espacio
    if espacio == 1:
        if word == ' ':
            espacio = 0
            return 1
        else:  
            espacio = 0
    if word == ' ':
        espacio = 1
    return 0

def reset():
    global cuerpo, topicos, basura, contador, espacio
    cuerpo = 0
    topicos = 0
    basura = 0
    contador = 0
    espacio = 0

path = actual+"/cooperativa"
n = open ("Ncooperativa.txt", 'w')
t = open ("Tcooperativa.txt", 'w')
for arch in listdir(path):
    ruta = join(path, arch)
    try:
        if isfile(ruta):
            f = open (ruta, 'r')
            reset()
            for line in f:
                espacio = 0
                if line[0:7] == "<title>":
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0:
                        if sacarSaltoTab(word):
                            n.write(' ')
                            continue
                        if sacarEspacioDoble(word):
                            continue
                        n.write(word)
                if line[13:27] == "rotulo-topicos":
                  topicos = 1
                if topicos == 1:
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0:
                        if sacarSaltoTab(word):
                            t.write(' ')
                            continue
                        if sacarEspacioDoble(word):
                            continue
                        t.write(word)
                if line[1:7] == "</div>":
                  topicos = 0
                if line[12:27] == "cuerpo-articulo":
                  cuerpo = 1
                if  cuerpo == 1:
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0 and script == 0:
                        if sacarSaltoTab(word):
                            n.write(' ')
                            continue
                        if sacarEspacioDoble(word):
                            continue
                        n.write(word)
                if line[10:16] == "prompt":
                  cuerpo = 0
            f.close
            n.write('\n')
            t.write('\n')
    except:
        print("# ERROR en cooperativa#") 
n.close

n = open ("Ntheclinic.txt", 'w')
t = open ("Ttheclinic.txt", 'w')
titulo = []
path = actual+"/theclinic"
for arch in listdir(path):
    ruta = join(path, arch)
    try:
        if isfile(ruta):
            reset()
            basura = 1
            f = open (ruta, 'r')
            for line in f:
                espacio = 0
                if line[61:68] == "<title>":
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0:
                        if sacarSaltoTab(word):
                            n.write(' ')
                            continue
                        if sacarEspacioDoble(word):
                            continue
                        n.write(word)
                if line[10:21] == "article:tag":
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0:
                        if sacarSaltoTab(word):
                            t.write(' ')
                            continue
                        if sacarEspacioDoble(word):
                            continue
                        t.write(word)
                if line[17:44] == "</span></span></a></div><p>":
                    cuerpo = 1
                if cuerpo == 1:
                  contador = contador + 1
                  if contador == 1 or contador > 14:
                      for word in line:
                        if sacarEntre(word):
                            continue
                        if basura == 0 and script == 0:
                            if sacarSaltoTab(word):
                                n.write(' ')
                                continue
                            if sacarEspacioDoble(word):
                                continue
                            n.write(word)
                if line[6:28] == "http://20.theclinic.cl":
                    cuerpo = 0
            f.close
            n.write('\n')
            t.write('\n')    
    except:
        print("# ERROR en theclinic#")  
n.close

n = open ("Nelmostrador.txt", 'w')
t = open ("Telmostrador.txt", 'w')
path = actual+"/elmostrador"
for arch in listdir(path):
    ruta = join(path, arch)
    try:
        if isfile(ruta):
            f = open (ruta, 'r')
            reset()
            for line in f:
                if line[16:23] == "<title>":
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0:
                        if sacarSaltoTab(word):
                            n.write(' ')
                            continue
                        n.write(word)
                if line[132:145] == "tags-noticias":
                    topicos = 1
                if topicos == 1:
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0 and script == 0:
                        if sacarSaltoTab(word):
                            t.write(' ')
                            continue
                        t.write(word)
                if line[52:83] == "</div> <!-- /.tags-noticias -->":
                    topicos = 0
                if line[102:116] == "cuerpo-noticia":
                    cuerpo = 4
                if cuerpo > 1:
                    cuerpo = cuerpo - 1
                    continue
                if  cuerpo == 1:
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0 and script == 0:
                        if sacarSaltoTab(word):
                            n.write(' ')
                            continue
                        n.write(word)
                if line[52:62] == "<!--BBC-->":
                    cuerpo = 0
            f.close
            n.write('\n')
            t.write('\n')    
    except:
        print("# ERROR en el mostrador#")  
n.close

n = open ("Nadnradio.txt", 'w')
t = open ("Tadnradio.txt", 'w')
path = actual+"/adnradio"
for arch in listdir(path):
    ruta = join(path, arch)
    try:
        if isfile(ruta):
            f = open (ruta, 'r')
            reset()
            for line in f:
                contador = contador + 1
                if contador == 5:
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0:
                        if sacarSaltoTab(word):
                            n.write(' ')
                            continue
                    n.write(word) #Titulo
                if line[16:24] == "keywords":
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0:
                        if sacarSaltoTab(word):
                            t.write(' ')
                            continue
                        t.write(word)
                if line[27:44] == "<!--Desarrollo-->":
                    cuerpo = 1
                    continue
                if line[27:48] == "<!--Fin Desarrollo-->":
                    cuerpo = 0
                if cuerpo == 1:
                    for word in line:
                        if sacarEntre(word):
                            continue
                        if basura == 0:
                            if sacarSaltoTab(word):
                                n.write(' ')
                                continue
                            n.write(word)
            f.close
            n.write('\n')
            t.write('\n')
    except:
        print("# ERROR en adn radio#") 
n.close

