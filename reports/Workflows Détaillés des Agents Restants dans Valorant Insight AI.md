# Workflows Détaillés des Agents Restants dans Valorant Insight AI

Ce document complète l'analyse précédente en détaillant les workflows des agents **AnalystBot**, **CoachBot**, **OracleBot** et **QueryTunerBot** au sein de la plateforme Valorant Insight AI.

## 1. Workflow de l'AnalystBot (Analyse Tactique)

L'**AnalystBot** est l'agent analyste tactique, intervenant après le **CleanerBot** pour transformer les données nettoyées en informations exploitables. Ses responsabilités principales sont les suivantes [1] [2] :

*   **Calcul des KPI (Key Performance Indicators)** : Il calcule des KPI tactiques tels que le KDA (Kills/Deaths/Assists), la précision du tir (Aim) et l'économie. Il génère également le score OVR (Overall Rating) pour les joueurs, similaire aux systèmes d'EA Sports.
*   **Détection des Faiblesses Tactiques** : En collaboration avec le CoachBot, il identifie les défaillances spécifiques dans le jeu (par exemple, un mauvais timing de reprise de site ou un ancrage de site inefficace).
*   **Analyse SQL** : Il effectue des analyses SQL sur les données pour extraire des caractéristiques de performance.

### Flux de travail de l'AnalystBot (Exemple : Analyse de Performance Joueur) [3]
1.  Le **CleanerBot** fournit un jeu de données nettoyé à l'AnalystBot.
2.  L'AnalystBot interroge l'entrepôt de données (Data Warehouse) pour obtenir les métriques de performance.
3.  Il calcule les KPI et les insights.
4.  Ces informations sont ensuite transmises à l'API du système pour être affichées à l'utilisateur.

## 2. Workflow du CoachBot (IA Stratégique et RAG)

Le **CoachBot** est l'agent d'IA stratégique, spécialisé dans la recommandation de tactiques et la synthèse d'analyses. Son rôle est crucial pour fournir des conseils exploitables [1] [2] :

*   **Synthèse d'Analyse** : Il synthétise les analyses de l'AnalystBot en rapports en langage naturel, en utilisant un raisonnement méta-contextuel.
*   **Recommandations Stratégiques** : Il recommande des tactiques optimales basées sur la méta-connaissance et les données de patch. Il explique également le raisonnement derrière ses suggestions.
*   **Utilisation de la Mémoire RAG** : Il exploite une base de données vectorielle (FAISS) enrichie de notes de patch et de données de jeu professionnel pour ses recommandations.

### Flux de travail du CoachBot (Exemple : Recommandation de Stratégie) [3]
1.  L'AnalystBot fournit les faiblesses et le contexte au CoachBot.
2.  Le CoachBot interroge la mémoire RAG (FAISS) pour récupérer les stratégies pertinentes.
3.  Il collabore avec l'OracleBot pour évaluer la probabilité de succès de la stratégie.
4.  Enfin, il envoie les recommandations stratégiques à l'API du système.

## 3. Workflow de l'OracleBot (Agent de Prédiction)

L'**OracleBot** est l'agent de prédiction, dont la fonction principale est de prévoir les résultats et d'évaluer les probabilités de succès des stratégies [1] [2] :

*   **Prédiction des Résultats de Match** : Il prévoit les probabilités de victoire pour les manches et les matchs en utilisant des modèles d'apprentissage automatique (par exemple, XGBoost).
*   **Évaluation de la Stratégie** : Il simule la probabilité de succès des recommandations stratégiques générées par le CoachBot.

### Flux de travail de l'OracleBot (Exemple : Prédiction du Résultat de Match) [3]
1.  L'AnalystBot extrait les caractéristiques prédictives et les envoie à l'OracleBot.
2.  L'OracleBot exécute son modèle de prédiction.
3.  Il renvoie le résultat prédit et la probabilité à l'API du système.

## 4. Workflow du QueryTunerBot (Agent d'Optimisation SQL)

Le **QueryTunerBot** est un agent d'optimisation autonome, conçu pour améliorer les performances des requêtes SQL analytiques [1] [2] :

*   **Analyse et Optimisation des Requêtes** : Il analyse, optimise et restructure automatiquement les charges de travail SQL analytiques pour garantir une exécution rapide sur de grands ensembles de données.
*   **Réécriture de Requêtes** : Il simplifie les jointures, les filtres et les agrégations.
*   **Recommandation d'Index** : Il suggère les meilleures stratégies d'indexation et propose des optimisations de modèle de données.

### Flux de travail du QueryTunerBot [2]
1.  Une requête SQL est envoyée au QueryTunerBot.
2.  Le QueryTunerBot analyse la requête, détecte les goulots d'étranglement (en utilisant `EXPLAIN ANALYZE` de DuckDB).
3.  Il réécrit la requête et recommande des index ou des vues matérialisées.
4.  La requête SQL optimisée est ensuite exécutée sur DuckDB.

## 5. Orchestration Globale (CrewAI)

L'ensemble de ces agents est orchestré par **CrewAI**, qui définit les workflows précis et les dépendances entre eux. Cette approche garantit une collaboration structurée et une séparation claire des préoccupations, où chaque agent apporte son expertise spécifique pour atteindre l'objectif global de la plateforme [1] [2].

---

### Références

[1] [Agents_worflows_Valorant.pdf](/home/ubuntu/Aurora/Agents_worflows_Valorant.pdf) - Multi-Agent Strategic Workflow Documentation
[2] [valorant_insight_ai (1) (1).pdf](/home/ubuntu/Aurora/valorant_insight_ai (1) (1).pdf) - Multi-Agent Esports Performance & Strategy Intelligence Platform
[3] [Diagrammes conception Projet Valorant.docx](/home/ubuntu/Aurora/Diagrammes conception Projet Valorant.docx) - Diagrammes conception Projet Valorant (Use case, Sequence)
