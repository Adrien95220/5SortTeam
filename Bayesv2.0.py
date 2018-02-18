import json 
import os

# retourne vrai ssi word est dans index
def search(index, word):
	for e in index:
		if e["word"] == word:
			return True
	return False
# Incrémente le tableau de probabilités
def Bayes(index, word,classe):
	for e in index:
		if e["word"] == word:
			return e[classe];
	return 0.0;

f = open('index.json', 'r')
file_content = f.read()
print("file content : ", file_content)

index = json.loads(file_content)

txt = input('Saisir une chaîne de caractères > ')

words = txt.split(' ')
L = [0.0,0.0,0.0,0.0]
Missing_Word = []
for word in words:
        L[0] = L[0] + Bayes(index,word,"question")
        L[1] = L[1] + Bayes(index,word,"bug")
        L[2] = L[2] + Bayes(index,word,"performance")
        L[3] = L[3] + Bayes(index,word,"ergonomy")
        if(not search(index,word)) :
                Missing_Word.append(word)
print("Question : " + str(L[0]))
print("Bug : " + str(L[1]))
print("Performance : " + str(L[2]))
print("Ergonomy : " + str(L[3]))
f.close();
if(len(Missing_Word) != 0) :
        os.remove('index.json')
        f = open('index.json','w')
        for word in Missing_Word:
                print("Pour le mot " + word +" Veuillez donner ses attributs")
                question = input("Question > ")
                bug = input("Bug > ")
                performance = input("Performance > ")
                ergonomy = input("ergonomy > ")
                # ajouter un élément à json index
                index.append({
                        "word" : word,
                        "question" : float(question),
                        "bug" : float(bug),
                        "performance" : float(performance),
                        "ergonomy" : float(ergonomy)
                })

        f.write(json.dumps(index, indent = 4))
        f.close()


               
                        
        

