#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pythonPremierTest.py
#
# Copyright 2014 yves Mercadier <yves.mercadier@ac-montpellier.fr>
#
#Les entrees du programme
#specifications
#parametre :
# aucun
#retour :
# a un nombre entier representant l'age de la personne.
def entree():
#Les entrees du programme
	print ("Es'que tu est gros ou maigre?\n")
	p = int(input("Quelle est ton poids en kg? "))
	t = int(input("Quelle est ta taille en cm? "))
	return p,t
#Calcul de l'IMC de la personne'
#specifications
#parametre :
# p un nombre entier representant le poids
#retour
# t un nombre entier represantant la taille de la personne
def metier(p,t):
#le calcul
	IMC =p/(t*t)
	return IMC
#Affichage
#specifications
#parametre :
# p un nombre entier represantant le poids de la personne
# t un nombre entier represantant la taille de la personne
#retour
# aucun
def pourImpression(IMC):
 strImpression="";""
 if IMC<16.5:
  strImpression ="\nTu est un somalien"
 if IMC>= 16.5 and IMC<= 18.5:
  strImpression ="\nTu commence a devenir normal"
 if IMC>= 18.5 and IMC<= 25:
  strImpression ="\nTu est normal"
 if IMC>= 25 and IMC<= 30:
  strImpression ="\nTu est trop gros"
 if IMC>= 30 and IMC<= 35:
  strImpression ="\nTu est VRAIMENT trop gros"
 if IMC>= 35 and IMC<=40:
  strImpression ="\nTu est tellement gros que tu ne vois plus tes pieds"
 if IMC> 40:
  strImpression ="\nTu est tellement gros que tu va mourir... Aller a+"
 return strImpression;
print (" ---> Debut du programme.\n")
poids,taille=entree()
IMC=metier(poids,taille)
print(pourImpression(IMC))
print ("\n ---> Fin du programme.")
