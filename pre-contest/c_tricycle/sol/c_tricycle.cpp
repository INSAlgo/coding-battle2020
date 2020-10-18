// Solution by Emma Neiss

#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char **argv) {

    // initialisation (récupération des inputs)
    int L, N;
    cin >> L >> N;

    vector<int> items (N);      // vecteur de int de taille N pour stocker les N objets
    for (int i = 0; i < N; ++i) {
        cin >> items[i];
        ++items[i];     // ajout d'une personne fictive dans le groupe pour respecter les distances
    }

// --- Implémentation du sac à dos classique sans répétition
// RQ : on fait +1 à la taille du sac initiale (longueur de la section de route) pour prendre
// en compte les distances nécessaires :
// comme on fait +1 à la taille de chacun des N groupes, mais qu'il faut laisser
// seulement N-1 espaces entre les groupes, on fait également +1 sur la taille du sac
// pour compenser
//
// Pour plus d'infos sur l'algorithme utilisé, voir "0-1 Knapsack Problem"

    vector<bool> sac (L+2);     // "sac" de capacité L+1
    sac[0] = true;

    for (auto item: items){
        for (int taille = L+1; taille > -1 ; --taille) {
            if (sac[taille] > 0 && taille + item <= L+1){
                sac[taille + item] = true;
            }
        }

        if (sac[L+1]){
            break;
        }
    }

    if (sac[L+1]){
        cout << "OUI" << endl;
    }else{
        cout << "NON" << endl;
    }

    return 0;
}

