class Vehicule:
    def __init__(self, marque, modele, annee, couleur):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleur = couleur

    def set_marque(self, marque):
        self.marque = marque

    def set_modele(self, modele):
        self.modele = modele

    def set_annee(self, annee):
        self.annee = annee

    def set_couleur(self, couleur):
        self.couleur = couleur

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee})"


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, couleur, nombre_portes):
        super().__init__(marque, modele, annee, couleur)
        self.nombre_portes = nombre_portes

    def set_nombre_portes(self, nombre_portes):
        self.nombre_portes = nombre_portes

    def __str__(self):
        return f"Voiture {super().__str__()}, {self.nombre_portes} portes"


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, couleur, cylindree):
        super().__init__(marque, modele, annee, couleur)
        self.cylindree = cylindree

    def set_cylindree(self, cylindree):
        self.cylindree = cylindree

    def __str__(self):
        return f"Moto {super().__str__()}, cylindrée : {self.cylindree}cc"


class Autobus(Vehicule):
    def __init__(self, marque, modele, annee, couleur, capacite_passagers):
        super().__init__(marque, modele, annee, couleur)
        self.capacite_passagers = capacite_passagers

    def set_capacite_passagers(self, capacite_passagers):
        self.capacite_passagers = capacite_passagers

    def __str__(self):
        return f"Autobus {super().__str__()}, capacité passagers : {self.capacite_passagers}"


class Metro(Vehicule):
    def __init__(self, marque, modele, annee, couleur, lignes):
        super().__init__(marque, modele, annee, couleur)
        self.lignes = lignes

    def set_lignes(self, lignes):
        self.lignes = lignes

    def __str__(self):
        return f"Métro {super().__str__()}, lignes : {', '.join(self.lignes)}"


class Application:
    def __init__(self):
        self.vehicle_list = []

    def start(self):
        print("Bienvenue dans l'application de gestion des véhicules !")
        self.menu()

    def menu(self):
        print("\nMenu:")
        print("1. Ajouter un véhicule")
        print("2. Supprimer un véhicule")
        print("3. Modifier un véhicule")
        print("4. Afficher des statistiques")
        print("5. Afficher la liste complète des véhicules")
        print("6. Rechercher un véhicule")
        print("7. Quitter l'application")
        choice = input("Veuillez sélectionner une option : ")

        if choice == "1":
            self.add_vehicle()
        elif choice == "2":
            self.remove_vehicle()
        elif choice == "3":
            self.modify_vehicle()
        elif choice == "4":
            self.display_statistics()
        elif choice == "5":
            self.display_vehicle_list()
        elif choice == "6":
            self.search_vehicle()
        elif choice == "7":
            self.quit()
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")
            self.menu()

    def add_vehicle(self):
        vehicle_type = input("Veuillez entrer le type de véhicule (voiture, moto, autobus, métro) : ")

        marque = input("Marque : ")
        modele = input("Modèle : ")
        annee = input("Année : ")
        couleur = input("Couleur : ")

        if vehicle_type == "voiture":
            nombre_portes = input("Nombre de portes : ")
            vehicle = Voiture(marque, modele, annee, couleur, nombre_portes)
        elif vehicle_type == "moto":
            cylindree = input("Cylindrée : ")
            vehicle = Moto(marque, modele, annee, couleur, cylindree)
        elif vehicle_type == "autobus":
            capacite_passagers = input("Capacité passagers : ")
            vehicle = Autobus(marque, modele, annee, couleur, capacite_passagers)
        elif vehicle_type == "métro":
            lignes = input("Lignes (séparées par des virgules) : ").split(",")
            vehicle = Metro(marque, modele, annee, couleur, lignes)
        else:
            print("Type de véhicule invalide.")
            self.menu()
            return

        self.vehicle_list.append(vehicle)
        print(f"Le véhicule {vehicle} a été ajouté avec succès !")
        self.menu()

    def remove_vehicle(self):
        self.display_vehicle_list()

        if len(self.vehicle_list) == 0:
            print("Aucun véhicule enregistré.")
            self.menu()
            return

        vehicle_number = int(input("Veuillez entrer le numéro du véhicule à supprimer : "))

        if vehicle_number < 1 or vehicle_number > len(self.vehicle_list):
            print("Numéro de véhicule invalide.")
            self.menu()
            return

        vehicle = self.vehicle_list.pop(vehicle_number - 1)
        print(f"Le véhicule {vehicle} a été supprimé avec succès !")
        self.menu()

    def modify_vehicle(self):
        self.display_vehicle_list()

        if len(self.vehicle_list) == 0:
            print("Aucun véhicule enregistré.")
            self.menu()
            return

        vehicle_number = int(input("Veuillez entrer le numéro du véhicule à modifier : "))

        if vehicle_number < 1 or vehicle_number > len(self.vehicle_list):
            print("Numéro de véhicule invalide.")
            self.menu()
            return

        vehicle = self.vehicle_list[vehicle_number - 1]
        print(f"Modifiez les attributs du véhicule {vehicle} :")

        marque = input("Nouvelle marque : ")
        modele = input("Nouveau modèle : ")
        annee = input("Nouvelle année : ")
        couleur = input("Nouvelle couleur : ")

        vehicle.set_marque(marque)
        vehicle.set_modele(modele)
        vehicle.set_annee(annee)
        vehicle.set_couleur(couleur)

        if isinstance(vehicle, Voiture):
            nombre_portes = input("Nouveau nombre de portes : ")
            vehicle.set_nombre_portes(nombre_portes)
        elif isinstance(vehicle, Moto):
            cylindree = input("Nouvelle cylindrée : ")
            vehicle.set_cylindree(cylindree)
        elif isinstance(vehicle, Autobus):
            capacite_passagers = input("Nouvelle capacité passagers : ")
            vehicle.set_capacite_passagers(capacite_passagers)
        elif isinstance(vehicle, Metro):
            lignes = input("Nouvelles lignes (séparées par des virgules) : ").split(",")
            vehicle.set_lignes(lignes)

        print(f"Le véhicule {vehicle} a été modifié avec succès !")
        self.menu()

    def display_statistics(self):
        print("\nStatistiques de circulation routière :")

        # Exemple de statistiques
        total_vehicules = len(self.vehicle_list)
        total_voitures = sum(isinstance(vehicle, Voiture) for vehicle in self.vehicle_list)
        total_motos = sum(isinstance(vehicle, Moto) for vehicle in self.vehicle_list)
        total_autobus = sum(isinstance(vehicle, Autobus) for vehicle in self.vehicle_list)
        total_metros = sum(isinstance(vehicle, Metro) for vehicle in self.vehicle_list)

        print(f"Total de véhicules enregistrés : {total_vehicules}")
        print(f"Total de voitures : {total_voitures}")
        print(f"Total de motos : {total_motos}")
        print(f"Total d'autobus : {total_autobus}")
        print(f"Total de métros : {total_metros}")

        self.menu()

        pass

    def display_vehicle_list(self):
        print("\nListe des véhicules enregistrés :")
        if len(self.vehicle_list) == 0:
            print("Aucun véhicule enregistré.")
        else:
            for i, vehicle in enumerate(self.vehicle_list, 1):
                print(f"{i}. {vehicle}")
        print()

    def search_vehicle(self):
        search_query = input("Veuillez entrer le critère de recherche (numéro d'immatriculation, marque, etc.) : ")
        search_results = []

        for vehicle in self.vehicle_list:
            if search_query.lower() in str(vehicle).lower():
                search_results.append(vehicle)

        if len(search_results) == 0:
            print("Aucun résultat trouvé.")
        else:
            print("\nRésultats de la recherche :")
            for i, result in enumerate(search_results, 1):
                print(f"{i}. {result}")

        self.menu()

    def quit(self):
        print("Merci d'avoir utilisé l'application. Au revoir !")


if __name__ == "__main__":
    app = Application()
    app.start()