#!/usr/bin/env python
# -*- coding: utf-8 -*-

def limpiador(text):
	archivo=open(text,'r')
	texto=archivo.read()
	texto2=texto.replace('&ldquo;','"')
	texto2=texto2.replace('&rdquo;','"')
	texto2=texto2.replace('&nbsp;',' ')
	texto2=texto2.replace('&quot;','')
	texto2=texto2.replace('&mdash;','')
	texto2=texto2.replace('&rdquo;','')
	texto2=texto2.replace('&#39;','\'')
	texto2=texto2.replace('&hellip;','')
	texto2=texto2.replace('íquest;','¿')
	texto2=texto2.replace('acute;','')
	texto2=texto2.replace('&a','á')
	texto2=texto2.replace('&e','é')
	texto2=texto2.replace('&i','í')
	texto2=texto2.replace('&o','ó')
	texto2=texto2.replace('&u','ú')
	texto2=texto2.replace('&ntilde;','ñ')
	texto2=texto2.replace('&#8220;','"')
	texto2=texto2.replace('&#8221;','"')
	texto2=texto2.replace('&#8211;','')
	texto2=texto2.replace('&#8217;','\'')
	texto2=texto2.replace('&#039;','\'')
	texto2=texto2.replace('&quot;','"')
	texto2=texto2.replace('property="article:tag" content="','')
	texto2=texto2.replace('" /',' | ')
	texto2=texto2.replace('Radio ADN 91.7','')
	texto2=texto2.replace(' - Cooperativa.cl','')
	texto2=texto2.replace(' Tópicos: ','')
	i = 100
	while i>1:
		texto2=texto2.replace('  ',' ')
		i = i - 1
	archivo2=open('L'+text,'w')
	archivo2.write(texto2)
	archivo.close()
	archivo2.close()



limpiador("Nadnradio.txt")
limpiador("Ncooperativa.txt")
limpiador("Nelmostrador.txt")
limpiador("Ntheclinic.txt")
limpiador("Tadnradio.txt")
limpiador("Tcooperativa.txt")
limpiador("Telmostrador.txt")
limpiador("Ttheclinic.txt")

