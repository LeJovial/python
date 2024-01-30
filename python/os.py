import os

def lister_fichiers_avec_taille(chemin_dossier):
    print(f"Fichiers dans le répertoire {chemin_dossier} avec leurs tailles:")
    for nom_fichier in os.listdir(chemin_dossier):
        chemin_complet = os.path.join(chemin_dossier, nom_fichier)
        if os.path.isfile(chemin_complet):
            taille = os.path.getsize(chemin_complet)
            print(f"{nom_fichier}: {taille} bytes")

chemin_dossier_specifie = "/chemin/vers/le/repertoire"
lister_fichiers_avec_taille(chemin_dossier_specifie)
