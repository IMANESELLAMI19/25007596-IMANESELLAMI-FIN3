### F1. Risque de crédit en Allemagne

- **Question :** quels attributs du client et du prêt permettent d'identifier les mauvais risques ?
- **Tâche :** classification binaire, avec coûts d'erreur asymétriques.
- **Données :** UCI 144, https://archive.ics.uci.edu/dataset/144. 1 000 dossiers, 20 variables, 300 mauvais risques.
- **Prétraitement :** encodage des variables catégorielles, standardisation des montants et des durées.
- **Modèles :** régression logistique (référence), arbre de décision, forêt aléatoire.
- **Métriques :** AUC et coût total. Fixer la matrice de coûts (par exemple : accepter un mauvais risque coûte cinq fois plus que refuser un bon) et la justifier.
- **Livrable :** notebook et courbe de coût selon le seuil de décision.
- **Risque :** le seuil optimal dépend des hypothèses de coût. Présenter une analyse de sensibilité.
