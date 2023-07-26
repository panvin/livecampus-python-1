import datetime
import shutil
import os

class exo4Class():

    def __init__(self, path: str):
        self.path = path

    def set_path(self, path):
        self.path = path

    def show_path(self):
        if self.path:
            print(self.path)
        else:
            print("Le path est vide")
    
    
    def get_files_list (self)-> list:
        fileList = []
        for item in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, item)):
                fileList.append(item)
        
        return fileList

    def copy_with_timestamp(self) -> None:
        now = datetime.datetime.now()
        formattedNow = now.strftime("%Y_%m_%d-%H_%M_%S")
        
        filePathNoExt, fileExt = os.path.splitext(self.path)
        newPath = f'{filePathNoExt}-{formattedNow}{fileExt}'
        
        try:
            shutil.copyfile(self.path, newPath)
        except shutil.SameFileError:
            print("Le fichier copié doit être différent du fichier à copier")
        except OSError as error:
            print(f"Une erreur est survenue lors de la copie du fichier: {error}")
        else:
            print("Le fichier a été copié sans incident.")