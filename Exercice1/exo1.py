########################################
# Exercice 1 Semaine Python Livecampus #
#        Vincent PANOUILLERES          #
########################################

def ask_user():
    print('Entrez une adresse ipv4')
    address= input()
    return address

def is_ipv4(input: str):
    address_chunk = input.split(".")

    if len(address_chunk) != 4:
        return False
    
    try:
        for chunk in address_chunk:
            if not 0 <= int(chunk) <= 255:
                return False
            else:
                return True
    except ValueError:
        return False
        
def is_ipv6(userInput: str):
    address_chunk = userInput.split(":")

    if len(address_chunk) != 8:
        return False
    
    try:
        for chunk in address_chunk:
            if  not 0 <= int(chunk, 16) <= 65535:
                return False
            else:
                return True
    except ValueError:
        return False
        
def is_list_ipv4_or_ipv6(inputList: list):
    testedList = []
    for element in inputList:
        version = 0
        if is_ipv4(element):
            version = 4;
        elif is_ipv6(element):
            version =  6;
        addressData = [element, version]
        testedList.append(addressData)

    return testedList

def is_dict_ipv4_or_ipv6(inputDict: dict):
    testedDict = {}
    for key, value in inputDict.items():
        version = 0
        if is_ipv4(value):
            version = 4;
        elif is_ipv6(value):
            version =  6;
        testedDict[key] = [value, version]

    return testedDict


def main():
    # Promp utilisateur
    userInput = ask_user()
    if is_ipv4(userInput):
        print(f"L'adresse ipv4 {userInput} est correcte")
    else :
        print(f"L'adresse ipv4 {userInput} est incorrecte")
    if is_ipv6(userInput):
        print(f"L'adresse ipv6 {userInput} est correcte")
    else :
        print(f"L'adresse ipv6 {userInput} est incorrecte")

    # Manipulation de liste et dictionnaire
    listIP = ["1.1.1.1", "192.168.2.3", "3.3.3.999", "2001:0db8:0000:85a3:0000:0000:ac1f:8001"]
    testedList = is_list_ipv4_or_ipv6(listIP)
    print (testedList)

    dictIP = {"alex-laptop": "1.1.1.1", "serveur-23": "192.168.2.3", "PC-maman": "3.3.3.999", "PC-invite": "2001:0db8:0000:85a3:0000:0000:ac1f:8001"}
    testedDict = is_dict_ipv4_or_ipv6(dictIP)
    print (testedDict)
    

if __name__ == "__main__":
    main()
