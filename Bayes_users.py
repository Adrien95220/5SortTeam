import json
import os
from collections import OrderedDict
import datetime

# Incrémente le tableau de probabilités
def Bayes(index, word):
    Frequencies = {"F > bug" : 0.0,"F > enhancement" : 0.0,"F > ergonomy" : 0.0,"F > performance" : 0.0,"M > duplicate" : 0.0,"M > to discuss" : 0.0, "P > must-have" :0.0,
              "P > nice-to-have" :0.0,"P > should-have" : 0.0,"S > ADMIN" : 0.0, "S > APPSCRIPT AP" : 0.0,"S > BIG JURY" : 0.0,"S > CODE REVERSER" :0.0,
              "S > DELIVERABLES" :0.0,"S > FDP" : 0.0,"S > FEEDBACK" :0.0,"S > FORMS" :0.0,"S > GAME" :0.0, "S > MATCHING ENGINE" :0.0,
              "S > ONLINE IDE" :0.0, "S > PLANNING MGT" : 0.0, "S > PROG CLOUD" : 0.0,"S > PROJECTS MGT" : 0.0,"S > QUIZZES" : 0.0,
              "S > TALLY SHEETS" : 0.0,"S > VIEWS" : 0.0, "S > GDRIVE GSHEETS" :0.0,"S > GDRIVE TEMPLATES" : 0.0,"U > help wanted" :0.0,
              "U > question" :0.0,"U > NEED DOC" :0.0, "WONTFIX" :0.0}
    for element in index :
        if element["word"] == word :
            for key in Frequencies.keys() :
                Frequencies[key] = element[key] / element["NbOfAppearances"]
            
    return Frequencies;

def put_in_json(user,text,Labels,freq) :
    f = open('feedbacks.json', 'r')
    file_content = f.read()
    index = json.loads(file_content)
    date = datetime.datetime.now()
    labels_input = ""
    count = 0
    for label in Labels :
        count = count +1
    if(count==1):
        labels_input = Labels[0]
    if(count==2):
        labels_input = Labels[0]+","+Labels[1]
    if(count == 3) :
        labels_input = Labels[0]+","+Labels[1]+","+Labels[2]
    index.append({
                                "user" : user,
                                "date":str(date.day)+"/"+str(date.month)+"/"+str(date.year),
                                "text":text,
                                "classes":labels_input,
                                "freq":freq
                        })
    f.close()
    os.remove('feedbacks.json')
    f = open('feedbacks.json', 'w')
    f.write(json.dumps(index, indent = 4))
    f.close()


def new_issue():
    f = open('bdd.json', 'r')
    file_content = f.read()
    index = json.loads(file_content)
    count_words = 0
    user = input("Saisir votre nom d'utilisateur > ")
    text = input('Saisir votre retour > ')
    words = text.split(' ')
    Labels = {"F > bug" : 0.0,"F > enhancement" : 0.0,"F > ergonomy" : 0.0,"F > performance" : 0.0,"M > duplicate" : 0.0,"M > to discuss" : 0.0, "P > must-have" :0.0,
              "P > nice-to-have" :0.0,"P > should-have" : 0.0,"S > ADMIN" : 0.0, "S > APPSCRIPT AP" : 0.0,"S > BIG JURY" : 0.0,"S > CODE REVERSER" :0.0,
              "S > DELIVERABLES" :0.0,"S > FDP" : 0.0,"S > FEEDBACK" :0.0,"S > FORMS" :0.0,"S > GAME" :0.0, "S > MATCHING ENGINE" :0.0,
              "S > ONLINE IDE" :0.0, "S > PLANNING MGT" : 0.0, "S > PROG CLOUD" : 0.0,"S > PROJECTS MGT" : 0.0,"S > QUIZZES" : 0.0,
              "S > TALLY SHEETS" : 0.0,"S > VIEWS" : 0.0, "S > GDRIVE GSHEETS" :0.0,"S > GDRIVE TEMPLATES" : 0.0,"U > help wanted" :0.0,
              "U > question" :0.0,"U > NEED DOC" :0.0, "WONTFIX" :0.0}
    for word in words:
        count_words = count_words + 1
        Frequencies = Bayes(index,word)
        for key in Labels.keys() :
            Labels[key] = Labels[key] + Frequencies[key]
    LabelsSorted = OrderedDict(sorted(Labels.items(), key=lambda t: t[1]))
    count = 0;
    MultipleValues = []
    MultipleLabels = {}
    freq = 0
    labels = []
    for key, value in LabelsSorted.items():
        count= count +1
        if(count>=30) :
            MultipleValues.append(value)
            MultipleLabels[key]=value
    if(MultipleValues[2] == 0) :
        labels.append("WONTFIX")
        put_in_json(user,text,labels,1.0)
    if(MultipleValues[0] == MultipleValues[1]) :
        if(MultipleValues[1] == MultipleValues[2]):
            freq = 3
            for key,value in LabelsSorted.items():
                if(value == MultipleValues[1] and value != 0 ) :
                    labels.append(key)
                    put_in_json(user,text,labels,value/count_words)
        if(MultipleValues[2] != 0) :
            freq = 1
            for key,value in LabelsSorted.items():
                if(value  == MultipleValues[2] and value != 0 ) :
                    labels.append(key)
                    put_in_json(user,text,labels,value/count_words)
        if(MultipleValues[2] == None) :
                freq = 0
    else :
        if(MultipleValues[1] == MultipleValues[2]) :
            print("Les classes finales sont : ")
            freq = 2
            for key,value in LabelsSorted.items():
                if(value == MultipleValues[2] and value != 0 ) :
                    labels.append(key)
                    put_in_json(user,text,labels,value/count_words)
        else :
            freq = 1
            for key,value in LabelsSorted.items():
                if(value  == MultipleValues[2] and value != 0) :
                    labels.append(key)
                    put_in_json(user,text,labels,value/count_words)

quit = 0
while(quit == 0) :
    print("Traiter une nouvelle issue : 1")
    print("Quitter : 2 ")
    chose = input(">")
    if(chose=="1") :
        new_issue()
    else :
        quit=1
        
