from tkinter import *
import tkinter as tk
import json
import os

def search(index, word):
    for e in index :
        if e["word"] == word:
            return True
    return False


       
class SortTeam(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("5SortTeam")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(sticky="NSEW")
        self.create_widgets()


    def json_find(self,label,labels,freq) :
        for e in labels :
            if e == label :
                return freq
            return 0.0

    def ReplaceWord(self,index, word,labels,freq):
        for element in index:
            if element["word"] == word:
                element["F > bug"] = element["F > bug"] + self.json_find("F > bug",labels,freq)
                element["F > enhancement"] = element["F > enhancement"] + self.json_find("F > enhancement",labels,freq)
                element["F > ergonomy"] = element["F > ergonomy"] + self.json_find("F > ergonomy",labels,freq)
                element["F > performance"] = element["F > performance"] + self.json_find("F > performance",labels,freq)
                element["M > duplicate"] = element["M > duplicate"]+ self.json_find("M > duplicate",labels,freq)
                element["M > to discuss"] = element["M > to discuss"] + self.json_find("M > to discuss",labels,freq)
                element["P > must-have"] = element["P > must-have"] + self.json_find("P > must-have",labels,freq)
                element["P > nice-to-have"] = element["P > nice-to-have"] + self.json_find("P > nice-to-have",labels,freq)
                element["P > should-have"] = element["P > should-have"] + self.json_find("P > should-have",labels,freq)
                element["S > ADMIN"] = element["S > ADMIN"] + self.json_find("S > ADMIN",labels,freq)
                element["S > APPSCRIPT AP"] = element["S > APPSCRIPT AP"] + self.json_find("S > APPSCRIPT AP",labels,freq)
                element["S > BIG JURY"] = element["S > BIG JURY"] + self.json_find("S > BIG JURY",labels,freq)
                element["S > CODE REVERSER"] = element["S > CODE REVERSER"] + self.json_find("S > CODE REVERSER" ,labels,freq)
                element["S > DELIVERABLES"] = element["S > DELIVERABLES"] + self.json_find("S > DELIVERABLES",labels,freq)
                element["S > FDP"] = element["S > FDP"] + self.json_find("S > FDP",labels,freq)
                element["S > FEEDBACK"] = element["S > FEEDBACK"] + self.json_find("S > FEEDBACK",labels,freq)
                element["S > FORMS"] = element["S > FORMS"] + self.json_find("S > FORMS",labels,freq)
                element["S > GAME"] = element["S > GAME"] + self.json_find("S > GAME",labels,freq)
                element["S > MATCHING ENGINE"] = element["S > MATCHING ENGINE"] + self.json_find("S > MATCHING ENGINE",labels,freq)
                element["S > ONLINE IDE"] = element["S > ONLINE IDE"] + self.json_find("S > ONLINE IDE",labels,freq)
                element["S > PLANNING MGT"] = element["S > PLANNING MGT"] + self.json_find("S > PLANNING MGT",labels,freq)
                element["S > PROG CLOUD"] = element["S > PROG CLOUD"]+ self.json_find("S > PROG CLOUD",labels,freq)
                element["S > PROJECTS MGT"] = element["S > PROJECTS MGT"] +  self.json_find("S > PROJECTS MGT",labels,freq)
                element["S > QUIZZES"] = element["S > QUIZZES"]  + self.json_find("S > QUIZZES",labels,freq)
                element["S > TALLY SHEETS"] = element["S > TALLY SHEETS"] + self.json_find("S > TALLY SHEETS",labels,freq)
                element["S > VIEWS"] =  element["S > VIEWS"] + self.json_find("S > VIEWS",labels,freq)
                element["S > GDRIVE GSHEETS"] = element["S > GDRIVE GSHEETS"] + self.json_find("S > GDRIVE GSHEETS",labels,freq)
                element["S > GDRIVE TEMPLATES"] = element["S > GDRIVE TEMPLATES"] + self.json_find("S > GDRIVE TEMPLATES",labels,freq)
                element["U > help wanted"] = element["U > help wanted"] + self.json_find("U > help wanted",labels,freq)
                element["U > question"] = element["U > question"] + self.json_find("U > question",labels,freq)
                element["U > NEED DOC"] =  element["U > NEED DOC"] + self.json_find("U > NEED DOC",labels,freq)
                element["WONTFIX"] = element["WONTFIX"] + self.json_find("WONTFIX" ,labels,freq)
                element["NbOfAppearances"] = element["NbOfAppearances"] +1 
    
    def clavier2(self,event) :
        touche = event.keysym
        classes = event.widget
        if touche == "Return":
            f = open('feedbacks.json', 'r')
            file_content2 = f.read()
            feedbacks = json.loads(file_content2)
            infos=self.liste2.grid_info()
            row = infos["row"]
            element = feedbacks[row-3]
            labels = element["classes"].split(",")
            classe = classes.curselection()
            for index in classe[::-1] :
                to_add = classes.get(index)
                labels.append(to_add)
                self.liste2.insert(END,classes.get(index))
            element["classes"] = ""
            for i in range(0,len(labels)-1):
                element["classes"] = labels[i] +"," + element["classes"]  
            element["classes"] =element["classes"] + labels[len(labels)-1]

            f.close()
            os.remove('feedbacks.json')
            f = open('feedbacks.json', 'w')
            f.write(json.dumps(feedbacks, indent = 4))
            f.close()
        
    def clavier(self,event):

        touche = event.keysym
        self.liste2 = event.widget
        if touche == "Delete":
            f = open('feedbacks.json', 'r')
            file_content2 = f.read()
            feedbacks = json.loads(file_content2)
            sel = self.liste2.curselection()
            infos=self.liste2.grid_info()
            row = infos["row"]
            element = feedbacks[row-3]
            labels = element["classes"].split(",")
            for index in sel[::-1]:
                to_del = self.liste2.get(index)
                labels.remove(to_del)
                element["classes"] = "";
                for i in range(len(labels)-1):
                    element["classes"] = labels[i] +"," + element["classes"]
                if(len(labels) != 0):
                    element["classes"] = element["classes"] + labels[len(labels)-1]
                f.close()
                os.remove('feedbacks.json')
                f = open('feedbacks.json', 'w')
                f.write(json.dumps(feedbacks, indent = 4))
                f.close()
                self.liste2.delete(index)
                          
        if touche == "Return":
            popup = Tk()
            classes = Listbox(popup,selectmode="multiple",height=31)
            classes.insert(1,"F > bug")
            classes.insert(2,"F > enhancement")
            classes.insert(3,"F > ergonomy")
            classes.insert(4,"F > performance")
            classes.insert(5,"M > duplicate")
            classes.insert(6,"M > to discuss")
            classes.insert(7, "P > must-have")
            classes.insert(8,"P > nice-to-have")
            classes.insert(9,"P > should-have")
            classes.insert(10,"S > ADMIN")
            classes.insert(11,"S > APPSCRIPT AP")
            classes.insert(12,"S > BIG JURY")
            classes.insert(13,"S > CODE REVERSER")
            classes.insert(14,"S > DELIVERABLES")
            classes.insert(15,"S > FDP")
            classes.insert(16,"S > FEEDBACK")
            classes.insert(17,"S > FORMS")
            classes.insert(18,"S > GAME")
            classes.insert(19,"S > MATCHING ENGINE")
            classes.insert(20,"S > ONLINE IDE")
            classes.insert(21,"S > PLANNING MGT")
            classes.insert(22,"S > PROG CLOUD")
            classes.insert(23,"S > PROJECTS MGT")
            classes.insert(24,"S > QUIZZES")
            classes.insert(25,"S > TALLY SHEETS")
            classes.insert(26,"S > VIEWS")
            classes.insert(27,"S > GDRIVE GSHEETS")
            classes.insert(28,"S > GDRIVE TEMPLATES")
            classes.insert(29,"U > help wanted")
            classes.insert(30,"U > question")
            classes.insert(31,"U > NEED DOC")
            classes.insert(32,"WONTFIX")
            classes.grid(row=1,column=1)
            classes.bind("<Key>", self.clavier2)
            button = Button(popup,text="Quit",command=popup.destroy).grid(row=2,column=1)

    def clic(self,event) :
        button = event.widget
        infos = button.grid_info()
        file = open('feedbacks.json', 'r')
        file_content2 = file.read()
        feedbacks = json.loads(file_content2)
        f = open('bdd.json', 'r')
        file_content = f.read()
        index = json.loads(file_content)
        row = infos["row"]
        element=feedbacks[row-3]
        words = element["text"].split(' ')
        Missing_Words = []
        Present_Words = []
        lab = element["classes"]
        freq = element["freq"]
        labels=lab.split(",")
        for word in words:
            if(not search(index,word)) :
                Missing_Words.append(word)
            else :
                Present_Words.append(word)

        for word in Present_Words :
            self.ReplaceWord(index, word,labels,freq)
            f.close()
            os.remove('bdd.json')
            f = open('bdd.json', 'w')
            f.write(json.dumps(index, indent = 4))
            f.close()
            f = open('bdd.json', 'r')
            file_content = f.read()
            index = json.loads(file_content)
        for word in Missing_Words :
            index.append({
                            "word" : word,
                            "F > bug" : self.json_find("F > bug",labels,freq),
                            "F > enhancement" : self.json_find("F > enhancement",labels,freq),
                            "F > ergonomy" : self.json_find("F > ergonomy",labels,freq),
                            "F > performance" : self.json_find("F > performance",labels,freq),
                            "M > duplicate" : self.json_find("M > duplicate",labels,freq),
                            "M > to discuss" :self.json_find("M > to discuss",labels,freq),
                            "P > must-have" : self.json_find("P > must-have",labels,freq),
                            "P > nice-to-have" : self.json_find("P > nice-to-have",labels,freq),
                            "P > should-have" : self.json_find("P > should-have",labels,freq),
                            "S > ADMIN" : self.json_find("S > ADMIN",labels,freq),
                            "S > APPSCRIPT AP" : self.json_find("S > APPSCRIPT AP",labels,freq),
                            "S > BIG JURY" :self.json_find("S > BIG JURY",labels,freq),
                            "S > CODE REVERSER" : self.json_find("S > CODE REVERSER" ,labels,freq),
                            "S > DELIVERABLES" : self.json_find("S > DELIVERABLES",labels,freq),
                            "S > FDP" : self.json_find("S > FDP",labels,freq),
                            "S > FEEDBACK" : self.json_find("S > FEEDBACK",labels,freq),
                            "S > FORMS" : self.json_find("S > FORMS",labels,freq),
                            "S > GAME" : self.json_find("S > GAME",labels,freq),
                            "S > MATCHING ENGINE" : self.json_find("S > MATCHING ENGINE",labels,freq),
                            "S > ONLINE IDE" : self.json_find("S > ONLINE IDE",labels,freq),
                            "S > PLANNING MGT" : self.json_find("S > PLANNING MGT",labels,freq),
                            "S > PROG CLOUD" : self.json_find("S > PROG CLOUD",labels,freq),
                            "S > PROJECTS MGT" : self.json_find("S > PROJECTS MGT",labels,freq),
                            "S > QUIZZES" : self.json_find("S > QUIZZES",labels,freq),
                            "S > TALLY SHEETS" : self.json_find("S > TALLY SHEETS",labels,freq),
                            "S > VIEWS" : self.json_find("S > VIEWS",labels,freq),
                            "S > GDRIVE GSHEETS" : self.json_find("S > GDRIVE GSHEETS",labels,freq),
                            "S > GDRIVE TEMPLATES" : self.json_find("S > GDRIVE TEMPLATES",labels,freq),
                            "U > help wanted" : self.json_find("U > help wanted",labels,freq),
                            "U > question" : self.json_find("U > question",labels,freq),
                            "U > NEED DOC" : self.json_find("U > NEED DOC",labels,freq),
                            "WONTFIX" : self.json_find("WONTFIX" ,labels,freq),
                            "NbOfAppearances" : 1,
                    })
            f.close()
            os.remove('bdd.json')
            f = open('bdd.json', 'w')
            f.write(json.dumps(index, indent = 4))
            f.close()
            f = open('bdd.json', 'r')
            file_content = f.read()
            index = json.loads(file_content)
        feedbacks.pop(row-3)
        file.close()
        os.remove('feedbacks.json')
        file = open('feedbacks.json', 'w')
        file.write(json.dumps(feedbacks, indent = 4))
        file.close()
        self.destroy()
        self.__init__()
        self.create_widgets()

            
                
        
        
        
            


    
    def create_widgets(self):
        logo = PhotoImage(file="logo.png")
        logoFrame = tk.Frame(self, borderwidth=2)
        Label(logoFrame,image=logo)
        logoFrame.grid(column=0, row=0, sticky="NSEW")
        Label(self,bg="chartreuse1",width=10,height=4).grid(row=1,column=1)
        Label(self,bg="chartreuse1",width=10,height=4).grid(row=1,column=2)
        Label(self,bg="chartreuse1",width=30,height=4).grid(row=1,column=3)
        Label(self,bg="chartreuse1",width=30,height=4).grid(row=1,column=4)
        Label(self, text='Utilisateur', borderwidth=1 ).grid(row=2, column=1)
        Label(self, text='Date du Post', borderwidth=1).grid(row=2, column=2)
        Label(self, text='Post', borderwidth=1).grid(row=2, column=3)
        Label(self, text='Classes proposés', borderwidth=1).grid(row=2, column=4)
        Label(self, text='Validation', borderwidth=1).grid(row=2, column=5)
        f = open('feedbacks.json', 'r')
        file_content = f.read()
        index = json.loads(file_content)
        count_row = 3
        for element in index :
            Label(self, text= element["user"]).grid(row=count_row,column=1)
            Label(self, text= element["date"]).grid(row=count_row,column=2)
            Label(self, text= element["text"],wraplength=400).grid(row=count_row,column=3)
            labels = element["classes"]
            label = labels.split(",")
            liste = Listbox(self,selectmode="multiple",height=3)
            count_list = 1
            for lab in label :
                liste.insert(count_list, lab)
                count_list = count_list + 1
                
            liste.bind("<Key>", self.clavier)
            liste.grid(row=count_row,column=4)
            var2 = IntVar()
            check = Button(self, text="Valider")
            check.bind("<Button-1>",self.clic)
            check.grid(row=count_row,column=5)
            count_row = count_row + 1
        f.close()
    
SortTeam().mainloop()



