import random as rd

movies = { "Action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
           "Comedy": ["Superbad", "Step Brothers", "The Big Lebowski", "Dumb and Dumber"],
            "Drama": ["Forrest Gump", "The Shawshank Redemption", "Titanic", "The Green Mile"], 
            "Sci-Fi": ["Interstellar", "Inception", "The Matrix", "Blade Runner 2049"], 
            "Horror": ["The Conjuring", "A Nightmare on Elm Street", "Get Out", "The Exorcist"] 
        }

print(" Welcome to the movie night recommender!🎬")
print("Available genres : Action, Comedy, Drama, Sci-fi, Horror")
print("Enter a genre: ", end=" ")
while True:
    try:
        genre = input("")
        if genre not in movies.keys():
            raise Exception
        else:
            break
    except Exception:
        print("Sorry, that genre is not available. Try again!")
print(f"You should watch: {movies[genre][0]}") 

# next step: put this program in a gui :)