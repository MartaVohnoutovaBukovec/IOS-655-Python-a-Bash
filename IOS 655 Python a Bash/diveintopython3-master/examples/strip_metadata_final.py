# strip metadata from Passau newspapers to text 2
# 

# import urllib3
import os
import codecs
import inspect
import sys
import glob
# os.path.dirname(__file__) # relative directory path
# os.path.abspath(__file__) # absolute file path
# os.path.basename(__file__) # the file name only
    

sit = "//fprsw04.ad.jcu.cz/roda/KfN/kfn_volume_067_issue_001_001_19140102"
#  sit = "\\fprsw04.ad.jcu.cz\roda\KfN\kfn_volume_067_issue_001_001_19140102"

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return (s[start:end],end)
    except ValueError:
        return ("Text End",999999)

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

    
for root, dirs, files in os.walk("//fprsw04.ad.jcu.cz/roda/KfN"):
    for file in os.listdir(root):
        if file.endswith(".xml"):
            f_vstupni = codecs.open(root+"/"+file, 'r','utf-8')
            vystup=f_vstupni.name.replace("xml","txt")
            # print( os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

            soubor = f_vstupni.read()

            delka = len(soubor)

            f_vystupni=codecs.open(vystup, 'w+','utf-8')

            #  sys.stdout = f_vystupni


            retez=["",0]
            pozice=0
            while pozice < delka :
                retez = find_between( soubor[pozice:delka], "<Unicode>", "</Unicode>" )
                print( retez[0]," ", file = f_vystupni, end="")
                # print( retez[0]," ", end="")
                pozice = pozice + retez[1]

            f_vstupni.close()
            f_vystupni.close()
 


