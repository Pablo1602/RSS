#!/usr/bin/env python
# -*- coding: utf-8 -*-
import feedparser
import urllib2
import os
import time
from unidecode import unidecode

#https://www.cooperativa.cl/noticias/stat/rss/rss.html
#https://www.elmostrador.cl/sindicacion/
 
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
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_6_74__1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_6_83__1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_16_256__1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_1_37__1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_3_156__1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_3_163__1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_2_70_935_1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_2_129_963_1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_2_73_985_1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_2_135_1012_1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_2_76_1023_1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_2_142_1069_1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_2_143_1078_1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_2_148_1158_1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_2_152_1226_1.xml'
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

if os.path.exists("cooperativa") == False: 
  print("Crear directorio cooperativa")
  os.mkdir('cooperativa')

if os.path.exists("elmostrador") == False: 
  print("Crear directorio elmostrador")
  os.mkdir('elmostrador')

if os.path.exists("adnradio") == False: 
  print("Crear directorio adnradio")
  os.mkdir('adnradio')

if os.path.exists("theclinic") == False: 
  print("Crear directorio theclinic")
  os.mkdir('theclinic')

if os.path.exists("soychilecl") == False: 
  print("Crear directorio soychilecl")
  os.mkdir('soychilecl')

if os.path.isfile("estado.txt") == False:
  print("Crear archivo estado")
  f = open("estado.txt", 'w')
  f.close

i=0 
# Recorremos cada RSS para cooperativa 
print("RSS de cooperativa") 
for url in cooperativa: 
 rss = feedparser.parse(url) 
 for post in rss.entries: 
  try: 
    titulo = post.title[0:100]
    path = actual+"/cooperativa/"+titulo+".html " 
    if os.path.isfile(path) == False: 
      respuesta = urllib2.urlopen(post.link) 
      contenidoWeb = respuesta.read() 
      f = open(path, 'w') 
      f.write(contenidoWeb) 
      f.close 
      i=i+1 
  except : 
    print("# ERROR #") 
if i != 0: 
  f = open("estado.txt", "a") 
  f.write(fechayhora +" - Se escribieron "+str(i)+" noticias de cooperativa\n") 
  f.close 
 
i=0 
# Recorremos cada RSS para elmostrador 
print("RSS de elmostrador") 
for url in elmostrador: 
 rss = feedparser.parse(url) 
 for post in rss.entries: 
  try: 
    titulo = post.title[0:100] 
    path = actual+"/elmostrador/"+titulo+".html" 
    if os.path.isfile(path) == False: 
      respuesta = urllib2.urlopen(post.link) 
      contenidoWeb = respuesta.read() 
      f = open(path, 'w') 
      f.write(contenidoWeb) 
      f.close 
      i=i+1 
  except : 
    print("# ERROR #") 
if i != 0: 
  f = open("estado.txt", "a") 
  f.write(fechayhora +" - Se escribieron "+str(i)+" noticias de elmostrador\n") 
  f.close 
 
i=0 
# Recorremos cada RSS para adnradio 
print("RSS de adnradio") 
for url in adnradio: 
 rss = feedparser.parse(url) 
 for post in rss.entries: 
  try: 
    titulo = post.title[0:100] 
    path = actual+"/adnradio/"+titulo+".html" 
    if os.path.isfile(path) == False: 
      respuesta = urllib2.urlopen(post.link) 
      contenidoWeb = respuesta.read() 
      f = open(path, 'w') 
      f.write(contenidoWeb) 
      f.close 
      i=i+1 
  except : 
    print("# ERROR #") 
if i != 0: 
  f = open("estado.txt", "a") 
  f.write(fechayhora +" - Se escribieron "+str(i)+" noticias de adnradio\n") 
  f.close 
 
 
i=0 
# Recorremos cada RSS para theclinic 
print("RSS de theclinic") 
for url in theclinic: 
 rss = feedparser.parse(url) 
 for post in rss.entries: 
  try: 
    titulo = post.title[0:100] 
    path = actual+"/theclinic/"+titulo+".html" 
    if os.path.isfile(path) == False: 
      respuesta = urllib2.urlopen(post.link) 
      contenidoWeb = respuesta.read() 
      f = open(path, 'w') 
      f.write(contenidoWeb) 
      f.close 
      i=i+1 
  except : 
    print("# ERROR #") 
 
if i != 0: 
  f = open("estado.txt", "a") 
  f.write(fechayhora +" - Se escribieron "+str(i)+" noticias de theclinic\n") 
  f.close

i=0
basura=0
# Recorremos cada RSS para soychilecl
print("RSS de soychilecl")
for url in soychilecl:
 rss = feedparser.parse(url)
 for post in rss.entries:
  titulo = post.title[0:100]
  path = actual+"/soychilecl/"+titulo+".html"
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

if i != 0:
  f = open("estado.txt", "a")
  f.write(fechayhora +" - Se escribieron "+str(i)+" noticias de soychilecl\n")
  f.close

