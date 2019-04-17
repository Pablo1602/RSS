#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os import listdir
from os.path import isfile, join
from unidecode import unidecode

import feedparser
import urllib2
import time

cooperativa = ['https://www.cooperativa.cl/noticias/site/tax/port/all/rss_16___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_5___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_1___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_6___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_4___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_35___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_2___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_3___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_7___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_8___1.xml',
]

elmostrador = ['https://www.elmostrador.cl/destacado/feed/',
'https://www.elmostrador.cl/dia/feed/',
'https://www.elmostrador.cl/noticias/pais/feed/',
'https://www.elmostrador.cl/noticias/mundo/feed/',
'https://www.elmostrador.cl/noticias/cultura/feed/',
'https://www.elmostrador.cl/vida-en-linea/feed/',
'https://www.elmostrador.cl/opinion/feed/',
'https://www.elmostrador.cl/sin-editar/feed/',
'https://www.elmostrador.cl/kiosko/feed/',
'https://www.elmostrador.cl/seleccion/feed/',
'https://www.elmostrador.cl/multimedia/feed/'
]

adnradio = ['http://www.adnradio.cl/feed.aspx?id=PROG_555474',
'http://www.adnradio.cl/feed.aspx?id=PROG_555477',
'http://www.adnradio.cl/feed.aspx?id=PROG_1853535',
'http://www.adnradio.cl/feed.aspx?id=PROG_2047349',
'http://www.adnradio.cl/feed.aspx?id=PROG_1909940',
'http://www.adnradio.cl/feed.aspx?id=PROG_1302638',
'http://www.adnradio.cl/feed.aspx?id=PROG_555475',
'http://www.adnradio.cl/feed.aspx?'
]


theclinic = ['http://www.theclinic.cl/feed/'
]

soychilecl = ['http://feeds.feedburner.com/soychilecl-todas',
'http://feeds.feedburner.com/soychilecl-cultura',
'http://feeds.feedburner.com/soychilecl-deportes',
'http://feeds.feedburner.com/soychilecl-economia-y-negocios',
'http://feeds.feedburner.com/soychilecl-espectaculos',
'http://feeds.feedburner.com/soychilecl-internacional'
'http://feeds.feedburner.com/soychilecl-policial',
'http://feeds.feedburner.com/soychilecl-politica',
'http://feeds.feedburner.com/soychilecl-sociedad',
'http://feeds.feedburner.com/soychilecl-tecnologia'
]

actual = os.getcwd()
fechayhora = time.strftime("%c")
print(actual)
print(fechayhora)

if os.path.exists("Nelmostrador") == False: 
  print("Crear directorio Nelmostrador")
  os.mkdir('Nelmostrador')

if os.path.exists("Ncooperativa") == False: 
  print("Crear directorio Ncooperativa")
  os.mkdir('Ncooperativa')

if os.path.exists("Ntheclinic") == False: 
  print("Crear directorio Ntheclinic")
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

if os.path.exists("Nsoychilecl") == False: 
  print("Crear directorio Nsoychilecl")
  os.mkdir('Nsoychilecl')

if os.path.isfile("Nestado.txt") == False:
  print("Crear archivo estado")
  f = open("Nestado.txt", 'w')
  f.close


i=0
cuerpo = 0
topicos = 0
# Recorremos cada RSS para cooperativa
print("RSS de cooperativa")
for url in cooperativa:
    rss = feedparser.parse(url)
    for post in rss.entries:
            titulo = post.title[0:100]
            npath = actual+"/Ncooperativa/"+titulo+".txt"
            tpath = actual+"/Tcooperativa/"+titulo+".txt"
            if os.path.isfile(npath) == False:
              n = open(npath, 'w')
              t = open(tpath, 'w')
              respuesta = urllib2.urlopen(post.link)
              for line in respuesta:
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
              n.close
              t.close
              i=i+1

# Recorremos cada RSS para theclinic
cuerpo = 0
topicos = 0
print("RSS de theclinic")
for url in theclinic:
    rss = feedparser.parse(url)
    for post in rss.entries:
        try:
            titulo = post.title[0:100]
            npath = actual+"/Ntheclinic/"+titulo+".txt"
            tpath = actual+"/Ttheclinic/"+titulo+".txt"
            if os.path.isfile(npath) == False:
              n = open(npath, 'w')
              t = open(tpath, 'w')
              respuesta = urllib2.urlopen(post.link)
              for line in respuesta:
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
            i=i+1
        except :
            print("# ERROR #")
# Recorremos cada RSS para elmostrador
cuerpo = 0
topicos = 0
print("RSS de elmostrador")
for url in elmostrador:
    rss = feedparser.parse(url)
    for post in rss.entries:
        try:
            titulo = post.title[0:100]
            npath = actual+"/Nelmostrador/"+titulo+".txt"
            tpath = actual+"/Telmostrador/"+titulo+".txt"
            if os.path.isfile(npath) == False:
              n = open(npath, 'w')
              t = open(tpath, 'w')
              respuesta = urllib2.urlopen(post.link)
              for line in respuesta:
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
            i=i+1
        except :
            print("# ERROR #")
# Recorremos cada RSS para soychilecl
print("RSS de soychilecl")
for url in soychilecl:
 rss = feedparser.parse(url)
 for post in rss.entries:
  try:
    titulo = post.title[0:100]
    path = actual+"/Nsoychilecl/"+titulo+".txt"
    if os.path.isfile(path) == False:
      f = open(path, 'w')
      text = unidecode(post.summary)
      for line in text:
        for word in line:
          if word == "<":
              basura = 1
          if word == ">":
              basura = 0
              continue
          if basura == 0:
              f.write(word)
      f.close
      i=i+1
  except :
    print("# ERROR #")
    
if i != 0:
    f = open("Nestado.txt", "a")
    f.write(fechayhora +" - Se escribieron "+str(i)+" noticias nuevas\n")
    f.close