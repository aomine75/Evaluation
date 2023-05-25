#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char immatriculation[20];
    char marque[50];
    char modele[50];
    int annee;
    char couleur[20];
} Vehicule;


Vehicule vehicules[100];
int nbVehicules = 0;


void ajouterVehicule();
void supprimerVehicule();
void modifierVehicule();
void afficherStatistiques();
void afficherVehicules();
void rechercherVehicule();

int main() {
    int choix;

    do {
        printf("========== GESTION DE LA CIRCULATION ROUTIÈRE ==========\n");
        printf("1. Ajouter un véhicule\n");
        printf("2. Supprimer un véhicule\n");
        printf("3. Modifier un véhicule\n");
        printf("4. Afficher les statistiques\n");
        printf("5. Afficher tous les véhicules\n");
        printf("6. Rechercher un véhicule\n");
        printf("7. Quitter\n");
        printf("Choix : ");
        scanf("%d", &choix);

        switch (choix) {
            case 1:
                ajouterVehicule();
                break;
            case 2:
                supprimerVehicule();
                break;
            case 3:
                modifierVehicule();
                break;
            case 4:
                afficherStatistiques();
                break;
            case 5:
                afficherVehicules();
                break;
            case 6:
                rechercherVehicule();
                break;
            case 7:
                printf("Merci d'avoir utilisé l'application.\n");
                break;
            default:
                printf("Choix invalide. Veuillez réessayer.\n");
        }

        printf("\n");

    } while (choix != 7);

    return 0;
}

void ajouterVehicule() {
    Vehicule nouveauVehicule;

    printf("===== AJOUTER UN VÉHICULE =====\n");

    printf("Immatriculation : ");
    scanf(" %[^\n]s", nouveauVehicule.immatriculation);

    printf("Marque : ");
    scanf(" %[^\n]s", nouveauVehicule.marque);

    printf("Modèle : ");
    scanf(" %[^\n]s", nouveauVehicule.modele);

    printf("Année : ");
    scanf("%d", &nouveauVehicule.annee);

    printf("Couleur : ");
    scanf(" %[^\n]s", nouveauVehicule.couleur);

    vehicules[nbVehicules++] = nouveauVehicule;

    printf("Le véhicule a été ajouté avec succès.\n");
}

void supprimerVehicule() {
    int indice;

    printf("===== SUPPRIMER UN VÉHICULE =====\n");

    printf("Indice du véhicule à supprimer : ");
    scanf("%d", &indice);

    if (indice >= 0 && indice < nbVehicules) {
        for (int i = indice; i < nbVehicules - 1; i++) {
            vehicules[i] = vehicules[i + 1];
        }

        nbVehicules--;

        printf("Le véhicule a été supprimé avec succès.\n");
    } else {
        printf("Indice invalide.\n");
    }
}

void modifierVehicule() {
    int indice;

    printf("===== MODIFIER UN VÉHICULE =====\n");

    printf("Indice du véhicule à modifier : ");
    scanf("%d", &indice);

    if (indice >= 0 && indice < nbVehicules) {
        Vehicule *vehicule = &vehicules[indice];

        printf("Immatriculation : ");
        scanf(" %[^\n]s", vehicule->immatriculation);

        printf("Marque : ");
        scanf(" %[^\n]s", vehicule->marque);

        printf("Modèle : ");
        scanf(" %[^\n]s", vehicule->modele);

        printf("Année : ");
        scanf("%d", &vehicule->annee);

        printf("Couleur : ");
        scanf(" %[^\n]s", vehicule->couleur);

        printf("Le véhicule a été modifié avec succès.\n");
    } else {
        printf("Indice invalide.\n");
    }
}

void afficherStatistiques() {
    int nbVoituresRouges = 0;
    int nbMotos = 0;
    int nbAutobus = 0;
    int nbAutresVehicules = 0;

    printf("===== STATISTIQUES DE LA CIRCULATION =====\n");

    for (int i = 0; i < nbVehicules; i++) {
        if (strcmp(vehicules[i].couleur, "rouge") == 0 && strcmp(vehicules[i].marque, "voiture") == 0) {
            nbVoituresRouges++;
        }

        if (strcmp(vehicules[i].marque, "moto") == 0) {
            nbMotos++;
        }

        if (strcmp(vehicules[i].marque, "autobus") == 0) {
            nbAutobus++;
        }

        if (strcmp(vehicules[i].marque, "voiture") != 0 && strcmp(vehicules[i].marque, "moto") != 0 &&
            strcmp(vehicules[i].marque, "autobus") != 0) {
            nbAutresVehicules++;
        }
    }

    printf("Nombre de voitures rouges : %d\n", nbVoituresRouges);
    printf("Nombre de motos : %d\n", nbMotos);
    printf("Nombre d'autobus : %d\n", nbAutobus);
    printf("Nombre d'autres véhicules : %d\n", nbAutresVehicules);
}

void afficherVehicules() {
    printf("===== LISTE DES VÉHICULES =====\n");

    for (int i = 0; i < nbVehicules; i++) {
        printf("===== VÉHICULE %d =====\n", i + 1);
        printf("Immatriculation : %s\n", vehicules[i].immatriculation);
        printf("Marque : %s\n", vehicules[i].marque);
        printf("Modèle : %s\n", vehicules[i].modele);
        printf("Année : %d\n", vehicules[i].annee);
        printf("Couleur : %s\n", vehicules[i].couleur);
        printf("=======================\n");
    }
}

void rechercherVehicule() {
    char critere[50];
    int resultatTrouve = 0;

    printf("===== RECHERCHER UN VÉHICULE =====\n");
    printf("Critère de recherche : ");
    scanf(" %[^\n]s", critere);

    for (int i = 0; i < nbVehicules; i++) {
        if (strstr(vehicules[i].immatriculation, critere) != NULL ||
            strstr(vehicules[i].marque, critere) != NULL ||
            strstr(vehicules[i].modele, critere) != NULL) {
            printf("===== VÉHICULE %d =====\n", i + 1);
            printf("Immatriculation : %s\n", vehicules[i].immatriculation);
            printf("Marque : %s\n", vehicules[i].marque);
            printf("Modèle : %s\n", vehicules[i].modele);
            printf("Année : %d\n", vehicules[i].annee);
            printf("Couleur : %s\n", vehicules[i].couleur);
            printf("=======================\n");
            resultatTrouve = 1;
        }
    }

    if (!resultatTrouve) {
        printf("Aucun véhicule trouvé.\n");
    }
}
