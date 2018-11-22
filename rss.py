#!/usr/bin/env python
# -*- coding: utf-8 -*-
import feedparser
import urllib2
import time
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
 
urlList = ['https://www.cooperativa.cl/noticias/site/tax/port/all/rss_16___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_5___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_1___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_6___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_4___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_35___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_2___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_3___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_7___1.xml',
'https://www.cooperativa.cl/noticias/site/tax/port/all/rss_8___1.xml',
'https://www.elmostrador.cl/destacado/feed/',
'https://www.elmostrador.cl/dia/feed/',
'https://www.elmostrador.cl/noticias/pais/feed/',
'https://www.elmostrador.cl/noticias/mundo/feed/',
'https://www.elmostrador.cl/noticias/cultura/feed/',
'https://www.elmostrador.cl/vida-en-linea/feed/',
'https://www.elmostrador.cl/opinion/feed/',
'https://www.elmostrador.cl/sin-editar/feed/',
'https://www.elmostrador.cl/kiosko/feed/',
'https://www.elmostrador.cl/seleccion/feed/',
'https://www.elmostrador.cl/multimedia/feed/',
'http://www.adnradio.cl/feed.aspx?id=PROG_555474',
'http://www.adnradio.cl/feed.aspx?id=PROG_555477',
'http://www.adnradio.cl/feed.aspx?id=PROG_1853535',
'https://www.publimetro.cl/cl//newtenberg/index_rss.rss',
'http://www.theclinic.cl/feed/',
'http://feeds.feedburner.com/soychilecl-todas',
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
 

# Se obtiene la fecha de hoy
#hoy = time.strftime("%a")+", "+time.strftime("%d")
  #Obtiene la fecha de publicación de la noticia
  #publicacion = post.published[0:7]
  #Si la fecha corresponde a la de hoy
  #if publicacion == hoy:

i=1
# Recorremos cada RSS
for url in urlList:	
 rss = feedparser.parse(url)
 # Recorremos todos los post que aparecen en el RSS
 for post in rss.entries:
  #Obtener el link de la noticia
  respuesta = urllib2.urlopen(post.link)
  #Leer noticia desde la pagina de origen
  contenidoWeb = respuesta.read()
  titulo = post.title[0:10]
  publicacion = post.published[0:11]
  print(str(i)+": "+titulo)
  i=i+1
  #Escribir la noticia
  f = open(publicacion+"_"+titulo+".html", 'w')
  f.write(contenidoWeb)
  f.close