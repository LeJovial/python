import shutil

def verifier_espace_disque():
    espace_disque = shutil.disk_usage("/")

    print("Espace disque du disque principal:")
    print(f"   Total: {espace_disque.total} bytes")
    print(f"   Utilisé: {espace_disque.used} bytes")
    print(f"   Disponible: {espace_disque.free} bytes")
    print(f"   Pourcentage d'utilisation: {espace_disque.percent}%")

verifier_espace_disque()