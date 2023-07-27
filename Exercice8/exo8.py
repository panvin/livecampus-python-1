########################################
# Exercice 8 Semaine Python Livecampus #
#        Vincent PANOUILLERES          #
########################################

from bamboo.Bamboo import Bamboo
import pathlib
import os


def main():
    
    rootFile = pathlib.Path(__file__).parent.resolve()
    csvFileName = "dataSetTwo.csv"
    jsonFileName = "dataSetOne.json"
    
    print ("-----Question 1 -------")
    dataObjForJson = Bamboo(os.path.join(rootFile, jsonFileName))
    dfOne = dataObjForJson.read_file()
    print(dfOne)
   
    print ("-----Question 2 et 3 -------")
    dataObjForCsv = Bamboo(os.path.join(rootFile, csvFileName))
    dataObjForCsv.read_file()

    dataReddit = dataObjForCsv.filter_dataframe('url', 'reddit')
    print(dataReddit)
    dataObjForCsv.save_data_filtered_as_csv(os.path.join(rootFile, "reddit.csv"))
    
    dataTrue = dataObjForCsv.filter_dataframe('boolean', True)
    print(dataTrue)
    dataObjForCsv.save_data_filtered_as_csv(os.path.join(rootFile, "true.csv"))

if __name__ == "__main__":
    main()
