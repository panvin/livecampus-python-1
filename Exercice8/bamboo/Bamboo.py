import pandas
import os

class Bamboo():

    def __init__(self, path: str):
        self.path = path
        self.data = None
        self.dataFiltered = None
        self.fileExt = ""
        self.readFunction = {
            ".json":  pandas.read_json,
            ".html":  pandas.read_html,
            ".csv":   pandas.read_csv,
            ".xlsx":  pandas.read_excel
        }
        self.isFileValid = False

    def __get_file_extension(self):
        self.fileExt = os.path.splitext(self.path)[1]
        self.check_extension()
        
    def check_extension(self):
        if not self.fileExt:
            print("Le chemin vers le fichier n'est pas correct ou le nom du fichier ne contient pas d'extension")
        
        elif self.fileExt not in self.readFunction :           
            extensions = ""
            for key in self.readFunction:
                extensions = f"{extensions}\"{key}\" "

            print(f"L'extension {self.fileExt} ne fait pas partie des extensiosn attendues: {extensions}")
        
        else:    
            self.isFileValid = True

    def read_file(self):
        self.__get_file_extension()      
        if self.isFileValid:
            self.data = self.readFunction[self.fileExt](self.path)
        else:
            print("Impossible de lire le fichier, le fichier en entrée n'est pas valide")
        return self.data
    
    def filter_dataframe(self, columnName : str, value: bool | str):

        try:
            if isinstance(value, str):
                self.dataFiltered =  self.data[self.data[columnName].str.contains(value)]
            elif isinstance(value, bool):
                self.dataFiltered =  self.data[self.data[columnName] == value]
            else:
                self.dataFiltered = self.data
                print("Le format de donnée filtrée n'est pas supporté ou le filtre est vide, les données n'ont pas été filtrée")

            percentage = 100 * self.dataFiltered.size / self.data.size
            print(f"Les données dont la colonne {columnName} contient {value} correspond à {percentage}% des données totales")
            return(self.dataFiltered)
        except KeyError:
            print("Le nom de colonne est erroné")

    def save_data_as_csv(self, path:str) -> None:
        try:
            self.data.to_csv(path)
        except OSError as error:
            print(f"Une erreur système est survenue lors du traitement du fichier: {error}.")
        except Exception as error:
            print (f"Une erreur est survenue: {error}.")
        else:
            print("L'écriture du fichier s'est terminé sans problème")

    def save_data_filtered_as_csv(self, path:str) -> None:
        try:
            self.dataFiltered.to_csv(path)
        except OSError as error:
            print(f"Une erreur système est survenue lors du traitement du fichier: {error}.")
        except Exception as error:
            print (f"Une erreur est survenue: {error}.")
        else:
            print("L'écriture du fichier s'est terminé sans problème")

    

         

            
        

        

    

