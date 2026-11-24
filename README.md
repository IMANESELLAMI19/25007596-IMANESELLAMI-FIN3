# F1 : Risque de crédit en Allemagne

Projet de science des données appliqué à la finance : **classification binaire à coûts asymétriques** (régression logistique).

- **Étudiante :** Imane Sellami
- **Code Apogée :** 25007596
- **Groupe / filière :** FIN 3, S7 FIN
- **Établissement :** ENCG Settat, Université Hassan 1er
- **Cours :** BD & DS, examen individuel (Partie B) · Enseignant : Mr Larhimi
- **Algorithme principal :** n° 8, régression logistique

## Problématique
Quels attributs du client et du prêt permettent d'identifier les mauvais risques, et quel seuil de décision minimise le coût total des erreurs quand accepter un mauvais risque coûte **5 fois plus** que refuser un bon client ?

## Objectifs mesurables (fixés avant les résultats)
- Coût total sur le test **au moins 20 % sous** la meilleure règle naïve (tout accepter / tout refuser)
- **AUC ≥ 0,70** sur le test

## Données
Statlog (German Credit Data), UCI n° 144, H. Hofmann (1994), licence CC BY 4.0. 1 000 dossiers, 20 variables explicatives, cible `mauvais_risque` (30 % de mauvais risques). Fichier utilisé : `data/raw/base_credit_allemagne.xlsx` (version francisée). Date d'extraction : 12/11/2026.

## Résultats principaux
| | Coût test | AUC test |
|---|---|---|
| Tout accepter | 375 | 0,50 |
| Tout refuser (meilleure référence) | 175 | 0,50 |
| **Régression logistique** (C = 0,03, seuil = 0,20) | **139** | **0,811** |

Gain de **20,6 %** face à « tout refuser » : objectif atteint de justesse. Sur 10 découpages différents, le gain moyen est de 18,2 % ± 8,4 points (l'objectif n'est atteint que 5 fois sur 10), alors que l'AUC reste ≥ 0,70 dans les 10 cas.

## Structure du dépôt
```
25007596-IMANESELLAMI-FIN3/
├── README.md
├── requirements.txt
├── .gitignore
├── DECLARATION_IA.md
├── data/
│   ├── raw/                    # données brutes
│   └── processed/              # données préparées par le notebook
├── docs/
│   ├── fiche_sujet_F1.md       # fiche du sujet
│   └── references.md           # sources consultées
├── notebooks/
│   └── projet_F1.ipynb         # notebook final, exécuté, avec ses sorties
├── src/
│   └── telecharger_donnees.py  # téléchargement de la source UCI (facultatif)
├── figures/                    # graphiques du rapport et de la présentation
├── rapport/
│   └── rapport.pdf             # export PDF du notebook (compte rendu)
└── presentation/
    ├── presentation.pdf        # les six diapositives
    └── presentation.pptx
```

## Reproduction
1. Cloner le dépôt : `git clone https://github.com/IMANESELLAMI19/25007596-IMANESELLAMI-FIN3.git`
2. Installer les dépendances (Python 3.10 ou plus récent) : `pip install -r requirements.txt`
3. Ouvrir `notebooks/projet_F1.ipynb` et choisir **Redémarrer et tout exécuter**. Le notebook fonctionne en local (lancé depuis `notebooks/` ou la racine) et dans Google Colab. Toutes les graines sont fixées à 42 ; la section 7 utilise aussi les graines 0 à 8 pour mesurer la stabilité.

## Limites
Jeu ancien (1994) et petit (1 000 dossiers) ; matrice de coûts 5/1 supposée ; biais de sélection ; variables sensibles (âge, statut personnel, travailleur étranger) ; politique peu réaliste (66 % de refus au seuil 0,20). Le gain de coût est modeste et incertain.

## Déclaration d'IA
Voir [`DECLARATION_IA.md`](DECLARATION_IA.md).
