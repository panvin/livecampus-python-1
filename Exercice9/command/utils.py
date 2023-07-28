from subprocess import (
    run,
    TimeoutExpired,
    CalledProcessError,
    SubprocessError
    )
from invoke.exceptions import (
    ThreadException,
    Failure,
    UnexpectedExit
    )
from fabric import Connection
from getpass import getpass
import re


def run_cmd_local(cmd: list[str]) -> str:
    
    try:
        output = run(cmd, capture_output=True)

    except CalledProcessError as ex:
        # An error occurs with the command to execute
        print(ex)
    except TimeoutExpired as ex:
        # Timeout issue
        print(f"Timeout was raised while executing command :{ex}")
    except SubprocessError as ex:
        # Any other Subprocess exception
        print(f"Subprocess exception : {ex}")
    except Exception as ex:
        # Any other exception
        print(ex)
    else:
        # Everything when fine !
        return output.stdout.decode(encoding="utf-8")
    
def run_cmd_dist(cmd : str, login: str, address: str) -> list:
    try:
        password = getpass(f"Please enter {login}@{address}'s password:\n")
        with Connection(f"{login}@{address}", connect_kwargs={"password": password}) as con:
            result = con.run(cmd, hide=True)
            return result.stdout

    except (UnexpectedExit, Failure, ThreadException) as error:
        print(f"Une erreur est survenue lors de l'éxécution de la commande sur l'hôte distant: {error}")
    except Exception as error:
        print(f"Une erruer est survenue: {error}")

        

def get_clean_interface_stdout(stdout: str) -> list[str]:
    # Regex pour trouver lister les noms d'interfaces (noms standards debian)
    network_list = re.findall(r'\d{1,2}: [a-z]{2,3}\d{0,2}', stdout)
    
    # Récupération uniquement des données nécessaires sous forme de liste
    network_clean_lsit = [ network_list[i].split(" ")[1] for i in range(0, len(network_list), 1)]
    return(network_clean_lsit)


def get_interface_as_list() -> list:
    stdout = run_cmd_local(["ip", "a"])
    if stdout:
        return get_clean_interface_stdout(stdout)
    else:
        print("L'éxécution de la commande n'a pas renvoyé de résultat")

def get_interface_dist_as_list(login: str, address: str) -> list:
    stdout = run_cmd_dist("ip a", login, address)
    if stdout:
        return get_clean_interface_stdout(stdout)
    else:
        print("L'éxécution de la commande n'a pas renvoyé de résultat")