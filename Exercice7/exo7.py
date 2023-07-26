########################################
# Exercice 7 Semaine Python Livecampus #
#        Vincent PANOUILLERES          #
########################################

import system.infos as infos
import system.process as process
import system.utils as utils

def main():
    
    print ("-----Question 1 -------")
    infosDict = infos.read_infos_sys()
    utils.save_json_in_root_dir(infosDict, "infos.json")
    
    print ("-----Question 2 -------")
    procsDict = process.get_all_process()
    utils.save_json_in_root_dir(procsDict, "procs.json")

    print ("-----Question 3 -------")
    procsGtTwoPercentDict = process.get_process_gt_two_percent()
    utils.save_json_in_root_dir(procsGtTwoPercentDict, "procs2%.json")

    print ("-----Question 4 -------")

if __name__ == "__main__":
    main()
