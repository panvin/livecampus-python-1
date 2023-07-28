########################################
# Exercice 9 Semaine Python Livecampus #
#        Vincent PANOUILLERES          #
########################################

from command import utils

def main():
    
    print ("-----Question 1 -------")
    interfaces_local = utils.get_interface_as_list()
    print(f"Les interfaces de la machine locales sont {interfaces_local}")

    print ("-----Question 2 -------")
    # Login et adresse à adapter à la machine à atteindre
    interfaces_dist = utils.get_interface_dist_as_list("vincent","localhost")
    print(f"Les interfaces de la machine distante sont {interfaces_dist}")

if __name__ == "__main__":
    main()