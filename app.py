# app.py
def login():
    username = "admin"
    # ERREUR DE SÉCURITÉ : Ne jamais laisser de mot de passe dans le code !
    password = "superSecretPassword123!" 
    
    print(f"Connexion de {username} avec le mot de passe {password}")

if __name__ == "__main__":
    login()