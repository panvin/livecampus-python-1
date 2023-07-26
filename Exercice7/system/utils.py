import json
import pathlib
import os

def save_json( data: list[str], new_json_path: str) -> None:
    try:    
        with open(new_json_path, "w") as json_file:
            json.dump(data, json_file)
    except OSError as error:
        print(f"Une erreur système est survenue lors du traitement du fichier: {error}.")
    except Exception as error:
        print (f"Une erreur est survenue: {error}.")
    else:
        print("L'écriture du fichier s'est terminé sans problème")

def save_json_in_root_dir( data: list[str], jsonFilename: str) -> None:
    rootFile = pathlib.Path(__file__).parent.resolve()
    save_json(data, os.path.join(rootFile, "..", jsonFilename))