def traiter_data(data):
    data_actifs = [t for t in data if t[2] == "actif"]
    data_tries = sorted(data_actifs, key=lambda x: x[1], reverse=True)
    resultat = [(identifiant, nombre) for identifiant, nombre, _ in data_tries]

    return resultat
data = [("id1", 10, "actif"), ("id2", 15, "inactif"), ("id3", 20, "actif")]
resultat = traiter_data(data)
print(resultat)