movies = { "Action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
           "Comedy": ["Superbad", "Step Brothers", "The Big Lebowski", "Dumb and Dumber"],
            "Drama": ["Forrest Gump", "The Shawshank Redemption", "Titanic", "The Green Mile"], 
            "Sci-Fi": ["Interstellar", "Inception", "The Matrix", "Blade Runner 2049"], 
            "Horror": ["The Conjuring", "A Nightmare on Elm Street", "Get Out", "The Exorcist"] 
        }


# Retourne la liste entière des films d'action
films_action = movies["Action"]
print(films_action)  # ['Mad Max: Fury Road', 'John Wick', 'Die Hard', 'Gladiator']

# Premier film d'horreur (index 0) 
premier_film_horreur = movies["Horror"][0]
print(premier_film_horreur)  # 'The Conjuring'


# Afficher tous les films par genre
for genre, films in movies.items():
    print(f"Genre {genre} 🎬:")
    for film in films:
        print(f"- {film}")


genres = movies.keys()
print(genres)  # dict_keys(['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Horror'])


tous_les_films = movies.values()
print(tous_les_films)  # dict_values([['Mad Max: Fury Road', 'John Wick', ...], ...])

