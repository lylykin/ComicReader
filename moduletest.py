import patoolib
from zipfile import ZipFile
from rarfile import RarFile
def unzip(comic):                                                              #servira si réussite a pouvoir convrtir n'importe quel fichier donné
    file=str(input("indiquez le nom du dossier: il correspondra au nom du comics"))
    with ZipFile(comic,"r") as zipObj:
     zipObj.extractall()

def checkFileExistance(comic):
    try:
        with open(comic, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
#comic=str(input("rentrez l'adresse du fichier"))
#if checkFileExistance(comic)== False:
   # unzip(comic)
"comic/Akira (01-38) (1988)/Akira (1988) #01.cbr"

#patoolib.extract_archive(u)
#rar=RarFile("comic/Akira (01-38) (1988)/Akira (1988) #01.cbr","r")
with RarFile("comic/Akira (01-38) (1988)/Akira (1988) #01.cbr","r") as zipObj:
   zipObj.extract(zipObj.namelist()[0])
