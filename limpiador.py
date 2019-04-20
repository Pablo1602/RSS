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
        if word == "c" and script == 1:
            script = 2
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

def reset():
    global cuerpo, topicos, basura, contador, espacio
    cuerpo = 0
    topicos = 0
    basura = 0
    contador = 0
    espacio = 0

#path = actual+"/cooperativa"
path = "/home/ubuntu/cooperativa"
n = open ("Ncooperativa.txt", 'w')
t = open ("Tcooperativa.txt", 'w')
print("cooperativa")
for arch in listdir(path):
    ruta = join(path, arch)
    try:
        if isfile(ruta):
            f = open (ruta, 'r')
            reset()
            for line in f:
                espacio = 0
                if line[0:7] == "<title>": #Comienzo titulo
                  if line[7:14] == "[Video]" or line[7:14] == "[Audio]" or line[7:14] == "[Fotos]":
                    break #Saltar video o audio
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0:
                        if sacarSaltoTab(word):
                            n.write(' ')
                        else:
                            n.write(word)
                  n.write('| ') #Fin de titulo               
                if line[13:27] == "rotulo-topicos" or line[9:17] == "keywords": #Comienzo topico
                  topicos = 1
                if topicos == 1:
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0:
                        if sacarSaltoTab(word):
                            t.write(' ')
                        else:
                            t.write(word)
                if line[1:7] == "</div>" or line[8:10] == "],": #Fin topico
                  topicos = 0
                if line[12:27] == "cuerpo-articulo" or line[9:20] == "articleBody": #Comienzo cuerpo
                  cuerpo = 1
                if  cuerpo == 1:
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0 and script != 2:
                        if sacarSaltoTab(word):
                            n.write(' ')
                        else:
                            n.write(word)
                if line[10:16] == "prompt" or line[9:20] == "articleBody": #Fin cuerpo
                  cuerpo = 0
            f.close
            n.write('\n')
            t.write('\n')
    except:
        print("#ERROR en cooperativa# "+ruta) 
n.close

n = open ("Ntheclinic.txt", 'w')
t = open ("Ttheclinic.txt", 'w')
#path = actual+"/theclinic"
path = "/home/ubuntu/theclinic"
print("theclinic")
for arch in listdir(path):
    ruta = join(path, arch)
    try:
        if isfile(ruta):
            reset()
            basura = 1
            f = open (ruta, 'r')
            for line in f:
                espacio = 0
                if line[61:68] == "<title>": #Comienzo titulo
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0:
                        if sacarSaltoTab(word):
                            n.write(' ')
                        else:
                            n.write(word)
                  n.write('| ') #Fin titulo  
                if line[10:21] == "article:tag": #Comienzo topico
                    topicos = 1
                    basura = 0
                if topicos == 1:
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0:
                        if sacarSaltoTab(word):
                            t.write(' ')
                        else:
                            t.write(word)
                if line[10:25] == "article:section": #Fin topico
                    topicos = 0
                if line[17:44] == "</span></span></a></div><p>" or line [7:18] == "articleBody": #Comienzo cuerpo
                    cuerpo = 1
                if cuerpo == 1:
                  contador = contador + 1
                  if contador == 1 or contador > 14:
                      for word in line:
                        if sacarEntre(word):
                            continue
                        if basura == 0 and script != 2:
                            if sacarSaltoTab(word):
                                n.write(' ')
                            else:
                                n.write(word)
                if line[6:28] == "http://20.theclinic.cl": #Fin cuerpo
                    cuerpo = 0
            n.write('\n')
            t.write('\n')    
            f.close
    except:
        print("# ERROR en theclinic# "+ruta) 
n.close

n = open ("Nelmostrador.txt", 'w')
t = open ("Telmostrador.txt", 'w')
#path = actual+"/elmostrador"
path = "/home/ubuntu/elmostrador"
print("elmostrador")
for arch in listdir(path):
    ruta = join(path, arch)
    try:
        if isfile(ruta):
            f = open (ruta, 'r')
            reset()
            for line in f:
                if line[16:23] == "<title>": #Comienzo titulo
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0:
                        if sacarSaltoTab(word):
                            n.write(' ')
                        else:
                            n.write(word)
                  n.write('| ') #Fin titulo  
                if line[132:145] == "tags-noticias": #Comienzo topico
                    topicos = 1
                if topicos == 1:
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0 and script != 2:
                        if sacarSaltoTab(word):
                            t.write(' ')
                        else:
                            t.write(word)
                if line[52:83] == "</div> <!-- /.tags-noticias -->": #Fin topico
                    topicos = 0
                if line[102:116] == "cuerpo-noticia": #Comienzo cuerpo
                    cuerpo = 4
                if cuerpo > 1:
                    cuerpo = cuerpo - 1
                    continue
                if  cuerpo == 1:
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0 and script != 2:
                        if sacarSaltoTab(word):
                            n.write(' ')
                        else:
                            n.write(word)
                if line[52:62] == "<!--BBC-->": #fin cuerpo
                    cuerpo = 0
            f.close
            n.write('\n')
            t.write('\n')    
    except:
        print("# ERROR en el mostrador# "+ruta) 
n.close

n = open ("Nadnradio.txt", 'w')
t = open ("Tadnradio.txt", 'w')
#path = actual+"/adnradio"
path = "/home/ubuntu/adnradio"
print("adnradio")
for arch in listdir(path):
    ruta = join(path, arch)
    try:
        if isfile(ruta):
            f = open (ruta, 'r')
            reset()
            for line in f:
                contador = contador + 1
                if contador == 5: # Comienzo titulo
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0:
                        if sacarSaltoTab(word):
                            n.write(' ')
                        else:
                            n.write(word) #Titulo
                  n.write('| ') #Fin de titulo  
                if line[16:24] == "keywords": #topico en una linea
                  for word in line:
                    if sacarEntre(word):
                        continue
                    if basura == 0:
                        if sacarSaltoTab(word):
                            t.write(' ')
                        else:
                            t.write(word)
                if line[27:44] == "<!--Desarrollo-->": #Comienzo cuerpo
                    cuerpo = 1
                    continue
                if line[27:48] == "<!--Fin Desarrollo-->": #Fin cuerpo
                    cuerpo = 0
                if cuerpo == 1:
                    for word in line:
                        if sacarEntre(word):
                            continue
                        if basura == 0:
                            if sacarSaltoTab(word):
                                n.write(' ')
                            else:
                                n.write(word)
            f.close
            n.write('\n')
            t.write('\n')
    except:
        print("# ERROR en adn radio# "+ruta) 
n.close

