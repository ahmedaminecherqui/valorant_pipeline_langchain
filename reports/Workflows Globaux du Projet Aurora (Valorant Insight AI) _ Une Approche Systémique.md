# Workflows Globaux du Projet Aurora (Valorant Insight AI) : Une Approche Systémique

Ce document répond à la question de savoir si les workflows précédemment décrits représentent l'ensemble des processus et clarifie la définition d'un workflow comme un ensemble d'agents collaborant sur des tâches connectées. Le projet Valorant Insight AI est structuré autour de plusieurs workflows multi-agents, où chaque agent contribue à une étape spécifique pour atteindre un objectif global [1] [2].

## 1. Définition d'un Workflow Multi-Agent

Un workflow multi-agent, dans le contexte de Valorant Insight AI, est une séquence structurée de tâches où différents agents spécialisés collaborent de manière séquentielle ou parallèle pour transformer des données brutes en intelligence actionable. Chaque agent a un rôle défini et utilise des outils spécifiques, et leur interaction est orchestrée par un cadre comme CrewAI [1].

## 2. Les Workflows Globaux Identifiés

Les documents du projet identifient plusieurs workflows principaux, chacun étant une chaîne d'agents travaillant ensemble :

### A. Workflow d'Analyse de la Performance des Joueurs

Ce workflow vise à fournir une intelligence individuelle exploitable en transformant la télémétrie de performance brute en métriques normalisées pour les entraîneurs et les analystes [1] [3].

**Agents Impliqués et Séquence :**
1.  **CleanerBot** : Ingestion des données de télémétrie de l'API Riot, validation des schémas et mappage des données à un format unifié. Stocke les données nettoyées dans le Data Warehouse [1] [3].
2.  **AnalystBot** : Reçoit les données nettoyées du CleanerBot. Calcule les KPI tactiques (KDA, Aim, Économie) et génère le score OVR (Overall Rating) du joueur [1] [3].

### B. Workflow de Détection des Faiblesses Tactiques

Ce workflow a pour objectif d'identifier systématiquement les vulnérabilités tactiques d'une équipe ou d'un joueur [1] [3].

**Agents Impliqués et Séquence :**
1.  **CleanerBot** : Prépare la télémétrie de match agrégée pour l'analyse diagnostique [1] [3].
2.  **AnalystBot** : Identifie les échecs spécifiques (par exemple, un mauvais timing de reprise de site ou un ancrage de site inefficace) [1] [3].
3.  **CoachBot** : Synthétise l'analyse en rapports en langage naturel en utilisant un raisonnement méta-contextuel [1] [3].

### C. Workflow de Recommandation Stratégique (RAG-Enhanced)

Ce workflow fournit des conseils tactiques améliorés par la génération augmentée par la récupération (RAG) [1] [3].

**Agents Impliqués et Séquence :**
1.  **CleanerBot & AnalystBot** : Fournissent le contexte de performance de base (données nettoyées et KPI) [1].
2.  **CoachBot** : Utilise une base de données vectorielle (RAG) avec les notes de patch et les données de jeu professionnel pour formuler des recommandations [1] [3].
3.  **OracleBot** : Simule la probabilité de succès de la recommandation générée par le CoachBot [1] [3].

### D. Workflow de Prédiction du Résultat de Match

Ce workflow est dédié à l'analyse prédictive pour projeter le taux de victoire [1] [3].

**Agents Impliqués et Séquence :**
1.  **CleanerBot** : Récupère et prépare les données de performance de match [3].
2.  **AnalystBot** : Traite les données et extrait les caractéristiques prédictives [3].
3.  **OracleBot** : Reçoit les caractéristiques prédictives et les alimente dans des modèles d'apprentissage automatique spécialisés (comme XGBoost) pour prévoir l'évolution du match et la probabilité de victoire [1] [3].

### E. Workflow d'Optimisation des Requêtes SQL (QueryTunerBot)

Bien que le QueryTunerBot puisse opérer de manière autonome, il s'intègre dans les workflows analytiques pour optimiser les requêtes [1] [2].

**Agent Impliqué et Intégration :**
*   **QueryTunerBot** : Optimise de manière autonome les structures SQL pour les grands ensembles de données analytiques. Il est invoqué avant l'exécution des requêtes pour s'assurer que toutes les charges de travail analytiques sont automatiquement optimisées [1] [2]. Il peut être considéré comme un agent de support transversal aux workflows nécessitant des requêtes de base de données.

## 3. Orchestration Multi-Agent (CrewAI)

L'orchestration de ces workflows est gérée par **CrewAI**, qui coordonne les agents, définit les dépendances et assure une collaboration structurée. Cette approche permet une séparation des préoccupations, une explicabilité accrue et une robustesse académique, reflétant un environnement de coaching e-sport professionnel [1] [2].

## 4. Conclusion

Votre définition d'un workflow est tout à fait correcte et s'applique parfaitement à l'architecture de Valorant Insight AI. Les 
workflows ne sont pas de simples listes d'agents individuels, mais des chaînes d'agents spécialisés qui travaillent en synergie pour atteindre des objectifs spécifiques, de l'ingestion des données à la recommandation stratégique et à la prédiction des résultats. Cette approche modulaire et collaborative est au cœur de l'efficacité de la plateforme.

---

### Références

[1] [Agents_worflows_Valorant.pdf](/home/ubuntu/Aurora/Agents_worflows_Valorant.pdf) - Multi-Agent Strategic Workflow Documentation
[2] [valorant_insight_ai (1) (1).pdf](/home/ubuntu/Aurora/valorant_insight_ai (1) (1).pdf) - Multi-Agent Esports Performance & Strategy Intelligence Platform
[3] [Diagrammes conception Projet Valorant.docx](/home/ubuntu/Aurora/Diagrammes conception Projet Valorant.docx) - Diagrammes conception Projet Valorant (Use case, Sequence)
