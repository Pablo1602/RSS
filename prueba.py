#!/usr/bin/env python
# -*- coding: utf-8 -*-
import feedparser
import urllib2
import os
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



print("RSS de adnradio")
for url in adnradio:
 rss = feedparser.parse(url)
 for post in rss.entries:
	try:
	  	titulo = post.title[0:100]
	  	path = actual+"/adnradio/"+titulo+".txt" 
		if os.path.isfile(path) == False: 
	  		respuesta = urllib2.urlopen(post.link)
	  		contenidoWeb = respuesta.read() 
	  		f = open(path, 'w')
	  		for line in respuesta:
	  			f.write(contenidoWeb)
	  		f.close 
	except:
		print("_ERROR_")
