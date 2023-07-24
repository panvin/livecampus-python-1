########################################
# Exercice 2 Semaine Python Livecampus #
#        Vincent PANOUILLERES          #
########################################

import os

# Code fourni par l'intervenant
def check_IPv4_address(ip: str) -> bool:
        for i in ip.split('.'):
            try:
                if not 0 <= int(i) <= 255:
                    return False
                # Ajout d'une erreur volontaire dans le code pour tester le raise
                raise ValueError
            except ValueError:
                 return False    
        return True

import fileinput

def check_address (ip: str) -> None:
    if check_IPv4_address(ip):
        print(f"L'adresse ip {ip} est valide!")
    else:
        print(f"L'adresse ip {ip} est invalide ou alors il y a un raise dans le code!")

def replace_letters_in_lines(content: list[str], listLetters: list[str]):
    newContent = []
    for line in content:
        new_line = line
        for letter in listLetters:
            newLine = new_line.replace(letter, "x")
        newContent.append(newLine)
    return newContent

def anonymize (path: str, listLetters: list):
    try:
        with open(path, 'r+') as file:
            content = file.readlines()
            newContent = replace_letters_in_lines(content, listLetters)
            file.seek(0)
            file.writelines(newContent)
            
    except OSError as error:
        print(f"Une erreur système est survenue lors du traitement du fichier: {error}.")
    except FileNotFoundError:
        print (f"Une erreur est survenue, le fichier {path} est introuvable.")
    except Exception as error:
        print (f"Une erreur est survenue: {error}.")
    else:
        print("La modification du fichier s'est terminé sans problème")

def format_textfile_as_dict(path):
    ret_dict = {}
    try:
        with open(path, 'r+') as file:
            content = file.readlines()
            ret_dict = {str(i+1): content[i] for i in range(len(content))}
            
    except OSError as error:
        print(f"Une erreur système est survenue lors du traitement du fichier: {error}.")
    except FileNotFoundError:
        print (f"Une erreur est survenue, le fichier {path} est introuvable.")
    except Exception as error:
        print (f"Une erreur est survenue: {error}.")
    else:
        print("La lecture du fichier s'est terminé sans problème") 
    return ret_dict

def print_formatted_dict(inputDict: dict):
    for line, value in inputDict.items():
        print(f"Ligne numéro {line} : {len(value)} caractères → {value}", end ='')
    

def main():
    
    print ("-----Question 1 -------")
    wrongAddress = "This should not work"
    rightAddress = "192.168.1.1"

    check_address(wrongAddress)
    check_address(rightAddress)

    
    print ("-----Question 2 -------")
    path = f'{ os.path.dirname(os.path.abspath(__file__))}/fileToRead.txt'
    listLetter = ['a', 'd', 'h', 'j', 'o', 't']

    print ("-----Question 3 -------")
    anonymize(path, listLetter)

    print ("-----Question 4 -------")
    formattedDict = format_textfile_as_dict(path)

    print ("-----Question 5 -------")
    print_formatted_dict(formattedDict)
    print ("\n")

if __name__ == "__main__":
    main()
