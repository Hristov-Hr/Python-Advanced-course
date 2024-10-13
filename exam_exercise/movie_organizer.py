def movie_organizer(*args):
    movies = {}

    for name, genre in args:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(name)

    sorted_movies = sorted(movies.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []

    for g, m in sorted_movies:
        result.append(f"{g} - {len(m)}")
        for movie in sorted(m):
            result.append(f"* {movie}")

    return '\n'.join(result)


print(movie_organizer(
    ("The Matrix", "Sci-fi")))
print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
