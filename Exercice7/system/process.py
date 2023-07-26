import psutil


def get_all_process():
    procs = {}
    for p in psutil.process_iter() :
        procs[p.pid] = p.as_dict()
    print (f"Nombre de processus: {len(procs)}")
    return procs

def get_process_gt_two_percent():
    procs = {}
    for p in psutil.process_iter() :
        if p.memory_percent() > 2:
            procs[p.pid] = p.as_dict()
    print (f"Nombre de processus utilisant plus de 2% de RAM: {len(procs)}")
    return procs