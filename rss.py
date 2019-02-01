#!/usr/bin/env python
# -*- coding: utf-8 -*-
import feedparser
import urllib2
import os


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
'http://www.adnradio.cl/feed.aspx?id=PROG_1853535'
]

publimetro = ['https://www.publimetro.cl/cl//newtenberg/index_rss.rss'
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
print(actual)

if os.path.exists("cooperativa") == False: 
  print("Crear directorio cooperativa")
  os.mkdir('cooperativa')

if os.path.exists("elmostrador") == False: 
  print("Crear directorio elmostrador")
  os.mkdir('elmostrador')

if os.path.exists("adnradio") == False: 
  print("Crear directorio adnradio")
  os.mkdir('adnradio')

if os.path.exists("publimetro") == False: 
  print("Crear directorio publimetro")
  os.mkdir('publimetro')

if os.path.exists("theclinic") == False: 
  print("Crear directorio theclinic")
  os.mkdir('theclinic')

if os.path.exists("soychilecl") == False: 
  print("Crear directorio soychilecl")
  os.mkdir('soychilecl')

# Recorremos cada RSS para cooperativa
print("RSS de cooperativa")
for url in cooperativa:
 rss = feedparser.parse(url)
 for post in rss.entries:
  try:
    titulo = post.title[0:100]
    path = actual+"/cooperativa/"+titulo+".html"
    if os.path.isfile(path) == False:
      respuesta = urllib2.urlopen(post.link)
      contenidoWeb = respuesta.read()
      f = open(path, 'w')
      f.write(contenidoWeb)
      f.close
  except :
    print("# ERROR #")



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
  except :
    print("# ERROR #")



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
  except :
    print("# ERROR #")



# Recorremos cada RSS para publimetro
print("RSS de publimetro")
for url in publimetro:
 rss = feedparser.parse(url)
 for post in rss.entries:
  try:
    titulo = post.title[0:100]
    path = actual+"/publimetro/"+titulo+".html"
    if os.path.isfile(path) == False:
      respuesta = urllib2.urlopen(post.link)
      contenidoWeb = respuesta.read()
      f = open(path, 'w')
      f.write(contenidoWeb)
      f.close
  except :
    print("# ERROR #")


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
  except :
    print("# ERROR #")


# Recorremos cada RSS para soychilecl
print("RSS de soychilecl")
for url in soychilecl:
 rss = feedparser.parse(url)
 for post in rss.entries:
  try:
    titulo = post.title[0:100]
    path = actual+"/soychilecl/"+titulo+".html"
    if os.path.isfile(path) == False:
      respuesta = urllib2.urlopen(post.link)
      contenidoWeb = respuesta.read()
      f = open(path, 'w')
      f.write(contenidoWeb)
      f.close
  except :
    print("# ERROR #")
