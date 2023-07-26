########################################
# Exercice 5 Semaine Python Livecampus #
#        Vincent PANOUILLERES          #
########################################

import exercice1.methods as exo1
import exercice4.methods as exo4
from exercice4.exo4Class import exo4Class
import os
import pathlib


def main():
    
    oldWorkingDirectory = os.getcwd()
    rootFile = pathlib.Path(__file__).parent.resolve()
    os.chdir(rootFile)
    
    
    print ("-----Question 1 -------")
    ip = "192.168.1.1"
    if exo1.is_ipv4(ip):
        print(f"L'adresse {ip} est une adresse ipv4!")
    elif exo1.is_ipv6(ip):
        print(f"L'adresse {ip} est une adresse ipv6!")
    else:
        print(f"L'adresse {ip} n'est ni une adresse ipv4, ni une adresse ipv6")
    
    ip = "2001:db8:0:85a3:0:0:ac1f:8001"
    version = exo1.is_list_ipv4_or_ipv6([ip])
    print(f"Il s'agit d'une adresse ipv{version[0][1]}")
    
    print ("-----Question 2 -------")
    path = os.getcwd()
    print("Liste des fichiers présens dans {path}")
    print(exo4.get_files_list(path))

    print ("-----Question 3 -------")    
    object = exo4Class(path)
    print(f"Liste des fichiers présents dans le path {object.show_path()}")
    print(object.get_files_list())

    path = os.path.join(path, 'fileToRead.txt')
    objectToCopy = exo4Class(path)
    objectToCopy.copy_with_timestamp()

    # Restauration de l'espace de travail
    os.chdir(oldWorkingDirectory)

if __name__ == "__main__":
    main()
