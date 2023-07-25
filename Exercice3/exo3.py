########################################
# Exercice 3 Semaine Python Livecampus #
#        Vincent PANOUILLERES          #
########################################

import requests
import csv
import os
import pathlib
import json

def call_api_dnd(url:str) -> dict:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def search_monster_api_dnd(name:str, limit: int = 5) -> dict:
    response = requests.get(f"https://api.open5e.com/monsters/?search={name}&ordering=challenge_rating&limit={str(limit)}")
    response.raise_for_status()
    return response.json()

def read_csv(path: str) -> list[str]:
    data = []
    try:
        with open(path, "r", newline="") as csv_file:
            reader = csv.reader(csv_file, delimiter =",")
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print (f"Une erreur est survenue, le fichier {path} est introuvable.")
    except OSError as error:
        print(f"Une erreur système est survenue lors du traitement du fichier: {error}.")
    except Exception as error:
        print (f"Une erreur est survenue: {error}.")
    else:
        print("La lecture du fichier s'est terminé sans problème")
    
    return data

def save_csv( data: list[str], new_csv_path: str) -> None:
    try:    
        with open(new_csv_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            writer.writerows(data)
    except OSError as error:
        print(f"Une erreur système est survenue lors du traitement du fichier: {error}.")
    except Exception as error:
        print (f"Une erreur est survenue: {error}.")
    else:
        print("L'écriture du fichier s'est terminé sans problème")

def alter_csv_data (data : list):
    # Données modifiées a titre d'exemple
    data [3][1] = 8.152
    data [4][0] = 155
    return data

def format_textfile_as_dict(path :str):
    ret_dict = {}
    try:
        with open(path, 'r+') as file:
            content = file.readlines()
            ret_dict = {str(i+1): content[i].replace("\n","") for i in range(len(content))}
            
    except FileNotFoundError:
        print (f"Une erreur est survenue, le fichier {path} est introuvable.")
    except OSError as error:
        print(f"Une erreur système est survenue lors du traitement du fichier: {error}.")
    except Exception as error:
        print (f"Une erreur est survenue: {error}.")
    else:
        print("La lecture du fichier s'est terminé sans problème") 
    return ret_dict

def save_json( data: list[str], new_json_path: str) -> None:
    try:    
        with open(new_json_path, "w") as json_file:
            content = json.dump(data, json_file)
    except OSError as error:
        print(f"Une erreur système est survenue lors du traitement du fichier: {error}.")
    except Exception as error:
        print (f"Une erreur est survenue: {error}.")
    else:
        print("L'écriture du fichier s'est terminé sans problème")

def main():
    
    print ("-----Question 1 -------")
    dndDict = search_monster_api_dnd("dragon", 2)
    # La requête suivante ne fonctionne pas et leve une erreur
    try:
        call_api_dnd("https://api.open5e.com/v1/monsters/adult-blue-dragon123153154")
    except requests.exceptions.HTTPError as error:
        print(f"L'API a retourné une erreur: {error}")

    print ("-----------------")
    print(dndDict)
    print ("-----------------")

    print ("-----Question 2 -------")
    rootFile = pathlib.Path(__file__).parent.resolve()
    csvInPath = os.path.join(rootFile, "csv_files", "small.csv")
    csvOutPath = os.path.join(rootFile, "csv_files", "csvOutQ2.csv")
    dataCsv = read_csv(csvInPath)
    dataCsv = alter_csv_data(dataCsv)
    save_csv(dataCsv, csvOutPath)
    
    print ("-----Question 3 -------")
    txtInPath = os.path.join(rootFile, "fileToRead.txt")
    jsonOutPath = os.path.join(rootFile, "json_files", "jsonOut.json")
    dataAsDict = format_textfile_as_dict(txtInPath)
    save_json(dataAsDict, jsonOutPath)


    print ("-----Question 4 -------")
    secondCsvOutPath = os.path.join(rootFile, "csv_files", "csvOutQ4.csv")
    dataAsList = list(dataAsDict.items())
    dataAsList.insert(0, ["Ligne", "Libellé"])
    save_csv(dataAsList, secondCsvOutPath)


if __name__ == "__main__":
    main()
