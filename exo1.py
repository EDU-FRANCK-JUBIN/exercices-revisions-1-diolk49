


def printSapin(nbLigne):
	for i in range(0, nbLigne + 1):
		ligne = ""	
		nbSpaces = (nbLigne - i)
		
		for s in range(0, nbSpaces):
			ligne += " "
		
		for c in range(0, (nbLigne - nbSpaces)*2 - 1):
			ligne += "*"
		
		print(ligne)


def main():
	nbLignes = int(input("Combien de lignes ? : ")

	printSapin(nbLignes)
