
# Script d'Envoi de Rapport Quotidien par Email

Ce script Python automatise l'envoi d'un rapport quotidien par email, en attachant spécifiquement le fichier de vente de pizzas daté du jour courant.

## Configuration

Avant de pouvoir utiliser ce script, vous devez effectuer quelques configurations préliminaires.

### Prérequis

- Python 3.x installé sur votre système.
- Accès à un serveur SMTP pour l'envoi d'emails (par exemple, Gmail).

### Paramètres SMTP

1. Ouvrez le fichier `daily_report.py` avec un éditeur de texte.
2. Modifiez les variables suivantes avec vos informations :

```python
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'votre_email@gmail.com'
smtp_password = 'votre_mot_de_passe'