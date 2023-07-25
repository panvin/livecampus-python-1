########################################
# Exercice 4 Semaine Python Livecampus #
#        Vincent PANOUILLERES          #
########################################

import datetime
import shutil
import pprint
import pathlib
import os
import sys

def get_files_list (path: str)-> list:
    fileList = []
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            fileList.append(item)
    
    return fileList

def copy_with_timestamp(path: str) -> None:
    now = datetime.datetime.now()
    formattedNow = now.strftime("%Y_%m_%d-%H_%M_%S")
    
    filePathNoExt, fileExt = os.path.splitext(path)
    newPath = f'{filePathNoExt}-{formattedNow}{fileExt}'
    
    try:
        shutil.copyfile(path, newPath)
    except shutil.SameFileError:
        print("Le fichier copié doit être différent du fichier à copier")
    except OSError as error:
        print(f"Une erreur est survenue lors de la copie du fichier: {error}")
    else:
        print("Le fichier a été copié sans incident.")

def main():
    
    # Sauvegarde de l'ancien répertoire de travail
    oldWorkingDirectory = os.getcwd()
    rootFile = pathlib.Path(__file__).parent.resolve()
    os.chdir(rootFile)
    
    print ("-----Question 1 -------")
    currentWorkingDirectory = os.getcwd()
    print(currentWorkingDirectory)
    
    fileList = get_files_list(currentWorkingDirectory)
    pprint.pprint(fileList)
    
    fileToCopy = os.path.join(currentWorkingDirectory, fileList[0])
    copy_with_timestamp(fileToCopy)

    print ("-----Question 2 -------")
    updatedFileList = get_files_list(currentWorkingDirectory)
    print (f"Nombre de fichiers présents dans le répertoire de travail: {len(updatedFileList)}")
    
    print ("-----Question 3 -------")
    for strParam in sys.argv[1:]:
        if os.path.isdir(strParam):
            try:
                print(f"Le path {strParam} contient {len(get_files_list(strParam))} fichiers")
            except PermissionError:
                print(f"Vous n'avez pas les droits d'accès au path {strParam}")
            except (OSError, Exception) as error:
                print(f"Une erreur est survenue lors de l'accès à {strParam}: {error}")
        else:
            print(f"L'argument {strParam} n'est pas un path de dossier correct") 

    # Restauration de l'espace de travail
    os.chdir(oldWorkingDirectory)

if __name__ == "__main__":
    main()
