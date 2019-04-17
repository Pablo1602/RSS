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

if os.path.exists("Nelmostrador") == False: 
  print("Crear directorio Lelmostrador")
  os.mkdir('Nelmostrador')

if os.path.exists("Ncooperativa") == False: 
  print("Crear directorio Lcooperativa")
  os.mkdir('Ncooperativa')

if os.path.exists("Ntheclinic") == False: 
  print("Crear directorio Ltheclinic")
  os.mkdir('Ntheclinic')

if os.path.exists("Telmostrador") == False: 
  print("Crear directorio Telmostrador")
  os.mkdir('Telmostrador')

if os.path.exists("Tcooperativa") == False: 
  print("Crear directorio Tcooperativa")
  os.mkdir('Tcooperativa')

if os.path.exists("Ttheclinic") == False: 
  print("Crear directorio Ttheclinic")
  os.mkdir('Ttheclinic')

cuerpo = 0
topicos = 0
basura = 0
path = actual+"/cooperativa"
noticia = actual+"/Ncooperativa"
topico = actual+"/Tcooperativa"
for arch in listdir(path):
    ruta = join(path, arch)
    try:
        if isfile(ruta):
            f = open (ruta, 'r')
            nruta = join(noticia, arch)
            truta = join(topico, arch)
            n = open (nruta, 'w')
            t = open (truta, 'w')
            for line in f:
                if line[0:7] == "<title>":
                  for word in line:
                    if word == "<":
                        basura = 1
                    if word == ">":
                        basura = 0
                        continue
                    if basura == 0:
                        n.write(word)
                if line[13:27] == "rotulo-topicos":
                  topicos = 1
                if topicos == 1:
                  for word in line:
                    if word == "<":
                        basura = 1
                    if word == ">":
                        basura = 0
                        continue
                    if basura == 0:
                        t.write(word)
                if line[1:7] == "</div>":
                  topicos = 0
                if line[12:27] == "cuerpo-articulo":
                  cuerpo = 1
                if  cuerpo == 1:
                  for word in line:
                    if word == "<":
                        basura = 1
                    if word == ">":
                        basura = 0
                        continue
                    if basura == 0:
                        n.write(word)
                if line[10:16] == "prompt":
                  cuerpo = 0
            f.close
            n.close
    except:
        print("# ERROR #")  

cuerpo = 0
topicos = 0
path = actual+"/theclinic"
noticia = actual+"/Ntheclinic"
topico = actual+"/Ttheclinic"
for arch in listdir(path):
    ruta = join(path, arch)
    try:
        if isfile(ruta):
            f = open (ruta, 'r')
            nruta = join(noticia, arch)
            truta = join(topico, arch)
            n = open (nruta, 'w')
            t = open (truta, 'w')
            contador = 0
            for line in f:
                if line[61:68] == "<title>":
                  for word in line:
                    if word == "<":
                        basura = 1
                    if word == ">":
                        basura = 0
                        continue
                    if basura == 0:
                        n.write(word)
                if line[10:21] == "article:tag":
                  for word in line:
                    if word == "<":
                        basura = 1
                    if word == ">":
                        basura = 0
                        continue
                    if basura == 0:
                        t.write(word)
                if line[17:44] == "</span></span></a></div><p>":
                    cuerpo = 1
                if cuerpo == 1:
                  contador = contador + 1
                  if contador == 1 or contador > 14:
                      for word in line:
                        if word == "<":
                            basura = 1
                        if word == ">":
                            basura = 0
                            continue
                        if basura == 0:
                            n.write(word)
                if line[15:29] == "><strong><span":
                    cuerpo = 0
            f.close
            n.close
    except:
        print("# ERROR #")  

cuerpo = 0
topicos = 0
path = actual+"/elmostrador"
noticia = actual+"/Nelmostrador"
topico = actual+"/Telmostrador"
for arch in listdir(path):
    ruta = join(path, arch)
    try:
        if isfile(ruta):
            f = open (ruta, 'r')
            nruta = join(noticia, arch)
            truta = join(topico, arch)
            n = open (nruta, 'w')
            t = open (truta, 'w')
            for line in f:
                if line[16:23] == "<title>":
                  for word in line:
                    if word == "<":
                        basura = 1
                    if word == ">":
                        basura = 0
                        continue
                    if basura == 0:
                        n.write(word)
                if line[132:145] == "tags-noticias":
                    topicos = 1
                if topicos == 1:
                  for word in line:
                    if word == "<":
                        basura = 1
                    if word == ">":
                        basura = 0
                        continue
                    if basura == 0:
                        t.write(word)
                if line[52:83] == "</div> <!-- /.tags-noticias -->":
                    topicos = 0
                if line[102:116] == "cuerpo-noticia":
                    cuerpo = 1
                if  cuerpo == 1:
                  for word in line:
                    if word == "<":
                        basura = 1
                    if word == ">":
                        basura = 0
                        continue
                    if basura == 0:
                        n.write(word)
                if line[52:62] == "<!--BBC-->":
                    cuerpo = 0
            f.close
            n.close
    except:
        print("# ERROR #")  

 

