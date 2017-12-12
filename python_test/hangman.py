#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random 

def mixwords(bonjour):

	# Définition de la varaible du mot que l'on devra retourné mixé
	mix_word = ""²

	# On boucle sur toute les lettres du mot sauf une
	# sinon le random.randrange(0, 0) retourne une erreur
	while len(bonjour) > 1:
		
		#On recupère un index aléatoire du mot saisie par l'utilisateur
		# -1 puisque dans un tableau les index commence à 0
		index_aleatoire = random.randrange(0, len(bonjour)-1)

		# On ajoute à notre mot que l'on doit retourner les lettre aléatoire
		mix_word = mix_word + bonjour[index_aleatoire]

		# Petit trick pour retirer la lettre du mot
		b = bytearray(bonjour)
		del b[index_aleatoire]
		bonjour = str(b)

		pass

	#on ajouter à la fin la dernière letre restante du mot choisie
	mix_word = mix_word + bonjour

	# Enfin on retourn le texte mixé
	return mix_word
	

	pass

print('\n\n------------------------------------------')
print('-------------- SUPER GAME ----------------')
print('------------------------------------------\n')
text = raw_input('Put a text here : \n')


print ("\nVotre texte mixed est: \n"  + mixwords(text))

print('\n------------   CREDITS: US ----------------')

