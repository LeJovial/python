import psutil

def afficher_utilisation_memoire():
    memoire = psutil.virtual_memory()

    print("Utilisation de la mémoire du système:")
    print(f"   Total: {memoire.total} bytes")
    print(f"   Disponible: {memoire.available} bytes")
    print(f"   Utilisé: {memoire.used} bytes")
    print(f"   Pourcentage d'utilisation: {memoire.percent}%")

afficher_utilisation_memoire()
