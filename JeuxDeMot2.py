import pygame
from pygame.locals import *
from random import *
import tkinter as tk


 


		
pygame.init()

pygame.font.init()

taille = (300,800)

main = pygame.display.set_mode(taille)
main.fill((0,0,0))

pygame.display.flip()
vitesse = 3

textMot = pygame.font.SysFont("comicsansms",30,True)
titre_Mot = pygame.font.SysFont("comicsansms",60,True)



liste_mots=[
'java','python','favorable','jazz','espace',
'ordinateur','banane','bleu','atome','ecran','sigma',
'koala','travailler','tetris','dessins','sujet','choix',
'bonheur','malheur','connaissance','desir','crayon','longtemps',
'despotique','circonstances','contradiction','lapin',
'orgueilleux','anticonstitutionnellement','inverse','constament',
'liberte','chaines','humain','accoutumance','sophisme','voyageur',
'ombre','tabouret','gorge','poing','scottie','atelier','odeur',
'machine','barbe','souffle','combinaisons','machoire','capitalisme',
'deces','papyruss','bizarre','fratricide','meurtre','evasion','defaite',
'echec','orthographe','pluralite','decentralisation','amateurisme',
'lundi','inscription','dossier','service','creation','acces',
'concour','avenir','restauration','condition','refectoire',
'reserver','tarif','finance','tarification','paiement',
'crediter','remboursement','principe','regle','bourse',
'intendance','forfait','absence','souci','sourir','courir',
'soupe','chef','cadre','badge','punition','blame','avertissement',
'mesure','responsabilisation','chatiment','sanction','haine','colere',
'temporaire','conseil','discipline','zero','exclusion','adjoint',
'palpation','cryogene','foutriquet','esoterique','croupion',
'gourdin','morbleu','tartare','rustre','morue','rance','bourru',
'grabuge','ganglion','rebelote','moribon','chasuble','cuistre',
'surimi','bougainvillier','freluquet','parpaing','chalumeau',
'chameau','garage','plante','abrasif','abusif','accusatif',
'actif','aculeiforme','adaptatif','addictif','additif','adhesif',
'adjectif','administratif','affabuler','affairement','affaisement',
'abessif','abhorrant'
]












########################################

class Mots:
	def __init__(self,mot,pos_x):
		self.nom = mot
		self.x = pos_x
		self.y = 15

	def affiche(self):
		mot_aff = textMot.render(self.nom, True, (0,0,0), (150,150,150))
		main.blit(mot_aff,(self.x, self.y))
		

	def detruit(self):
		if self.y >= taille[1]-100:
			return True

		return False

	def deplace(self):
		self.y += vitesse
		
	def set_nom(self,pnom):
		self.nom = pnom








########################################

def play():
	global vitesse
	vitesse = 3

	score = 0

	run = True
	PERDU = False

	n = randint(0, len(liste_mots)-1)
	Current_mot = Mots( liste_mots[n] , randint(30,taille[0]-30) )

	while run:

		rempli = False

		

		#QUITTER
		for event in pygame.event.get():

			key = pygame.key.get_pressed()
			if key[pygame.K_ESCAPE]:
				run = False
			if event.type == pygame.QUIT :
				run = False

		


		#MOT REMPLI
		n = randint(0, len(liste_mots)-1)
		if len(Current_mot.nom) < 1:
			Current_mot = Mots( liste_mots[n] , randint(0,taille[0]) )
			score += 1
			rempli = True


		#AFFICHAGE DU MOT
		titre_perdu = titre_Mot.render("PERDU", True, (150,0,0),(0,0,0))
		mot_aff = textMot.render(Current_mot.nom, True, (150,0,0), (0,0,0))

		main.blit(mot_aff,(Current_mot.x, Current_mot.y))



		ligne = pygame.draw.rect(main, (150,150,150),(0,taille[1]-100,taille[0],10))

		pygame.display.flip()

		

		main.fill((0,0,0))

		#PAS PERDU
		if not(PERDU):
			Current_mot.deplace()

			if event.type == KEYDOWN :
				if event.unicode == Current_mot.nom[0]:
					Current_mot.set_nom(Current_mot.nom[1:])

		#PERDU
		if Current_mot.detruit():
			main.fill((0,0,0))
			main.blit(titre_perdu, (70,300))
			PERDU = True

		if event.type == MOUSEBUTTONDOWN and Current_mot.detruit():
			run = False
			play()


		#AUGMENTATION DE LA VITESSE
		if score%10==0 and rempli:
			vitesse +=1



		#AFFICHAGE DU SCORE
		score_aff = textMot.render("Score : " + str(score),True,(150,0,0),(0,0,0))
		main.blit(score_aff,(10,10))

		
			

			
	pygame.quit()






play()






