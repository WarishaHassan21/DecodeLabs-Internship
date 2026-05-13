movies = [
    {"title": "Interstellar", "genres": ["Sci-Fi", "Adventure"]},
    {"title": "The Dark Knight", "genres": ["Action", "Drama"]},
    {"title": "Titanic", "genres": ["Romance", "Drama"]},
    {"title": "Conjuring", "genres": ["Horror", "Thriller"]},
    {"title": "Avengers", "genres": ["Action", "Sci-Fi"]},
    {"title": "Hangover", "genres": ["Comedy"]},
    {"title": "John Wick", "genres": ["Action", "Thriller"]},
    {"title": "La La Land", "genres": ["Romance", "Music"]},
]

def recommend_movies(user_preferences):
    recommendations = []

    for movie in movies:
        score = len(set(user_preferences) & set(movie["genres"]))

        if score > 0:
            recommendations.append((movie["title"], score))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations