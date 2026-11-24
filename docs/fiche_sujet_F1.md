# Fiche sujet F1 : Risque de crédit en Allemagne

| | |
|---|---|
| **Étudiante** | Imane Sellami |
| **Code Apogée** | 25007596 |
| **Groupe / filière** | FIN 3, S7 FIN |
| **Enseignant** | Mr Larhimi |
| **Algorithme principal** | n° 8, régression logistique |

## Intérêt du sujet
Une banque doit décider d'accorder ou de refuser un crédit à partir du profil du client et du prêt. Accepter un mauvais payeur coûte beaucoup plus cher que refuser un bon client (coût de 5 contre 1 dans la matrice de coûts du jeu UCI). Un modèle qui estime le risque aide la banque à décider, à condition de choisir un seuil adapté à ces coûts.

## Problématique
Quels attributs du client et du prêt permettent d'identifier les mauvais risques, et quel seuil de décision minimise le coût total des erreurs quand accepter un mauvais risque coûte cinq fois plus que refuser un bon client ?

## Objectif mesurable (fixé avant les résultats)
- **Métrique principale :** coût total sur le jeu de test = 5 × (mauvais risques acceptés) + 1 × (bons clients refusés).
- **Métrique secondaire :** AUC.
- **Références naïves :** « tout accepter » et « tout refuser ».
- **Jeu de test :** 25 % des 1 000 dossiers, stratifié, graine 42, utilisé une seule fois.
- **Seuil de réussite :** coût total inférieur d'au moins **20 %** à celui de la meilleure référence naïve, et AUC d'au moins **0,70**.

## Nature du problème
Classification binaire (bon ou mauvais risque), classes déséquilibrées (environ 70 % / 30 %) et coûts d'erreur asymétriques : le seuil de décision fait partie de la solution.

## Données
Statlog (German Credit Data), UCI Machine Learning Repository, jeu n° 144, H. Hofmann (1994), licence CC BY 4.0. 1 000 dossiers, 20 variables explicatives (7 numériques, 13 catégorielles), aucune valeur manquante, aucun doublon.

## Algorithme
Régression logistique avec pénalité L2 (scikit-learn). Forêt aléatoire (n° 12) écartée : moins lisible, et trop de variables pour 1 000 lignes.

## Résultat principal
Coût test 139 contre 175 pour « tout refuser » (−20,6 %), AUC test 0,811. Objectif atteint de justesse ; sur 10 découpages différents, le gain moyen est de 18,2 % ± 8,4 points et l'objectif de 20 % n'est atteint que 5 fois sur 10.
