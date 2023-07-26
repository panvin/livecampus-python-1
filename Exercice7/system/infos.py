import platform

def read_infos_sys():
    
    uname = platform.uname()._asdict()
    if platform.system() == "Linux":
        retDict = dict(uname, **(platform.freedesktop_os_release()))
        
    elif platform.system() == "Windows":
        retDict = dict(uname, **({"os_version":platform.win32_ver()}))
    else:
        retDict = uname

    return retDict