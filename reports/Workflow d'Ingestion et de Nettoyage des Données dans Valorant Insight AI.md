# Workflow d'Ingestion et de Nettoyage des Données dans Valorant Insight AI

Ce document décrit le processus d'ingestion et de nettoyage des données au sein de la plateforme Valorant Insight AI, en se concentrant sur le rôle de l'agent **CleanerBot**.

## 1. Vue d'ensemble du processus

Le workflow d'ingestion et de nettoyage des données est la première étape cruciale dans la chaîne de traitement de Valorant Insight AI. Il est principalement géré par le **CleanerBot**, un agent spécialisé dans l'ingénierie des données. Son objectif est de transformer les données brutes issues de l'API de Riot Games en un format propre, validé et unifié, prêt pour l'analyse par d'autres agents.

## 2. Rôle du CleanerBot

Le **CleanerBot** agit comme l'agent d'ingénierie des données. Ses responsabilités principales incluent [1] [2] :

*   **Ingestion des données** : Il récupère les données de télémétrie brutes directement depuis l'API de Riot Games.
*   **Validation des schémas** : Il s'assure que les données reçues respectent les schémas prédéfinis, garantissant ainsi la cohérence et l'intégrité des données.
*   **Normalisation et formatage** : Il mappe les données brutes à un format unifié, ce qui est essentiel pour une analyse cohérente à travers les différents agents du système.
*   **Préparation des données** : Il prépare les données de match agrégées pour l'analyse diagnostique ultérieure par l'AnalystBot.
*   **Stockage** : Après nettoyage, les données sont stockées dans l'entrepôt de données (Data Warehouse), prêtes à être interrogées par d'autres agents.

## 3. Flux de travail détaillé (basé sur le diagramme de séquence)

Le diagramme de séquence pour l'analyse des performances des joueurs [3] illustre clairement le rôle du CleanerBot :

1.  **Requête d'analyse** : Un utilisateur (Joueur/Analyste) envoie une requête d'analyse de performance au Système API.
2.  **Récupération et nettoyage** : Le Système API demande au CleanerBot de récupérer et nettoyer les données de match.
3.  **Accès à l'API Riot Games** : Le CleanerBot récupère les données de match brutes auprès de l'API de Riot Games.
4.  **Stockage des données nettoyées** : Le CleanerBot stocke les données nettoyées dans l'entrepôt de données (Data Warehouse).
5.  **Fourniture du jeu de données** : Le CleanerBot fournit le jeu de données nettoyé à l'AnalystBot pour traitement ultérieur.

## 4. Outils utilisés

Selon la documentation, le CleanerBot utilise des outils tels que **Pandas** pour la manipulation des données et **Great Expectations** pour la validation des schémas, assurant ainsi la qualité et la fiabilité des données [2].

## Références

[1] [Agents_worflows_Valorant.pdf](/home/ubuntu/Aurora/Agents_worflows_Valorant.pdf) - Multi-Agent Strategic Workflow Documentation
[2] [valorant_insight_ai (1) (1).pdf](/home/ubuntu/Aurora/valorant_insight_ai (1) (1).pdf) - Multi-Agent Esports Performance & Strategy Intelligence Platform
[3] [Diagrammes conception Projet Valorant.docx](/home/ubuntu/Aurora/Diagrammes conception Projet Valorant.docx) - Diagrammes conception Projet Valorant (Use case, Sequence)
