import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *                                                   # pour avoir les wigets nécessaire au lecteur
from zipfile import ZipFile                                                                   # pour décompresser les fichiers


def next_pushed():                                                              #affche l'image d'après si bouton appuyé
    global i
    if i==(len(L)-1):
        i=0
    else:
        i=i+1
    image_change(0)
    img.setPixmap(QPixmap(L[i]))

def preview_pushed():                                                           #affiche l'image d'avant si bouton appuyé
    global i
    if i==0:
        i=(len(L)-1)
    else:
        i=i-1
    image_change(0)
    img.setPixmap(QPixmap(L[i]))

def reserch_page():                                                             # va à la page sélectionnée
    i=int(input("saisissez la page"))
    while i<1 or i>(len(L)-1):
        i=int(input("le numéro de page saisi est incorrect, resaisissez le numéro de la page"))
    img.setPixmap(QPixmap(L[i-1]))
    img.resize(970,1490)
    assert img.resize(970,700),"l'image n'a pas été recadrée"

def image_change(y):
    if y>5:
        img.resize(970,700)
    else:
        img.resize(970,1490)

def openFileNameDialog():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName,_= QFileDialog.getOpenFileName(fen,"choisis ton comics","","All Files(*);;CBZ files(*.cbz)", options=options)
    if fileName:
        return fileName
    else:
        print("aucun comics sélectionné")


app = QApplication(sys.argv)                                                    #crée une application
fen = QWidget()                                                                 #crée la fenetre
i=0                                                                           #permettra de changer d'image
L=[]

with ZipFile(openFileNameDialog(),"r") as zipObj:                                   #dézippe le fichier nommé
    zipObj.extractall("unzip")
    for k in range(len(zipObj.namelist())):
      L.append("unzip/" + zipObj.namelist()[k])

img = QLabel(fen)
img.setPixmap(QPixmap(L[i]))                                                    #affiche l'image dans la fenêtre
img.resize(970,1490)

scrl = QScrollBar()                                                             #défiler l'image
scrl.setMaximum(10)                                                             #descendera jusqu'à la fin de l'image
scrl.setMinimum(0)
scrl.setPageStep(5)
scrl.valueChanged.connect(image_change)

Btnpreview = QPushButton("<preview")                                                  #bouton pour aller à la page d'avant
Btnpreview.clicked.connect(preview_pushed)

Btnnext = QPushButton("next>")                                                     #bouton pour aller à la page d'après
Btnnext.clicked.connect(next_pushed)

Btnreserch = QPushButton("looking for a specific page? click here")
Btnreserch.clicked.connect(reserch_page)
assert Btnreserch.clicked.connect(reserch_page),"méthode/fonction pas connectée"

layout = QVBoxLayout()                                                          #met en ordre les widgets
layout.addWidget(Btnreserch)                                                          #ajoute widget bouton recherche
layout.addWidget(scrl)                                                          #ajoute widget barre de défilement
layout.addWidget(Btnpreview)                                                          #ajoute widget bouton précédent
layout.addWidget(Btnnext)                                                          #ajoute widget bouton suivant

fen.setLayout(layout)
fen.setGeometry(200,0,970,750)                                                  #left,top,lenght,height
fen.setWindowTitle("ComicReader")                                               #donne titre de la fenêtre
fen.show()
sys.exit(app.exec_())                                                           #faire tourner le programme