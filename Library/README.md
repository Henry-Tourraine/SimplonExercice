## Consignes

Développer une API pour une librairie : 
- un livre en un seul exemplaire
- un utilisateur peut emprunter un livre
- un utilisateur peut voir le nombre de livres qu'il a empruntés

Pour lancer l'application, créer un environnement virtuel, téléchargez les dépendances du requirements.txt et tapez :<br/>
```
uvicorn main:app --reload
```

Etapes : 

* Créer un utilisateur -> POST /users/create
* Authentifiez-vous
* Créer un livre -> POST /books/create -> POST /books/create
* Vérifier si le livre est disponible -> GET /borrows/book/available/{id}
* Emprunter le livre -> POST /borrows/{book_id} // L'emprunt dure deux minutes
* Vérifier les emprunts en cours -> GET /borrows/current/all
* Vérifier les emprunts -> GET /borrows/all