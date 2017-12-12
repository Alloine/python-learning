#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random 

def delete_word_index(oldstr, index):
	
	if index > 0:
		return oldstr[:index] + oldstr[index+1:]
	else:
		return oldstr[1:]
		pass

	pass

def mixwords(mot_saisi_a_melanger):

	# Définition de la varaible du mot que l'on devra retourné mixé
	mix_word = ""

	# On boucle sur toute les lettres du mot sauf une
	# sinon le random.randrange(0, 0) retourne une erreur
	while len(mot_saisi_a_melanger) > 1:
		
		#On recupère un chiffres aléatoire du mot saisie par l'utilisateur
		# Compris entre 0 et le maximum de lettre dans le mot  ( salut = 5 index soit de 0 à 4 )
		# -1 puisque dans un tableau les index commence à 0
		index_maximum_du_mot = len(mot_saisi_a_melanger)-1
		index_aleatoire = random.randrange(0, index_maximum_du_mot)

		# On ajoute à notre mot que l'on doit retourner la lettre aléatoire
		mix_word = mix_word + mot_saisi_a_melanger[index_aleatoire]

		# Petit trick pour retirer la lettre du mot
		# supprimer du mot d'origine la lettre que l'on a recupéré
		mot_saisi_a_melanger = delete_word_index(mot_saisi_a_melanger, index_aleatoire)

		pass

	#on ajouter à la fin la dernière letre restante du mot choisie
	mix_word = mix_word + mot_saisi_a_melanger

	# Enfin on retourn le texte mixé
	return mix_word
	

	pass


print('\n\n------------------------------------------')
print('-------------- SUPER GAME ----------------')
print('------------------------------------------\n')


# Vairable contenant le mot saisie par l'utilisateur
text = input('Put a text here : \n')


mot_mixe = mixwords(text)

# On affiche à l'utilisateur le mot mixé
print ("\nVotre texte mixed est: \n"  + mot_mixe)

print('\n------------   CREDITS: US ----------------')

