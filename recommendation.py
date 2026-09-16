# ============================================================
# TASK 4: MOVIE RECOMMENDATION SYSTEM
# CodSoft AI Internship - Batch C19
# ============================================================
# WHAT THIS DOES:
# Recommends movies to a user based on:
#   Method 1 → Content-Based Filtering
#              (Find movies similar to ones you already liked)
#   Method 2 → Collaborative Filtering
#              (Find users like you, recommend what they liked)
#
# No external libraries needed! Pure Python. 🐍
# ============================================================

# ---------------------------------------------------------------
# STEP 1: Our Movie Database
# Each movie has a title and list of genres/tags
# ---------------------------------------------------------------

movies = {
    "Inception":          ["sci-fi", "thriller", "mind-bending", "action"],
    "The Dark Knight":    ["action", "thriller", "superhero", "crime"],
    "Interstellar":       ["sci-fi", "space", "emotional", "mind-bending"],
    "Avengers Endgame":   ["action", "superhero", "adventure", "emotional"],
    "The Matrix":         ["sci-fi", "action", "mind-bending", "thriller"],
    "Titanic":            ["romance", "drama", "emotional", "historical"],
    "The Notebook":       ["romance", "drama", "emotional"],
    "La La Land":         ["romance", "musical", "drama", "emotional"],
    "Toy Story":          ["animation", "adventure", "comedy", "family"],
    "Finding Nemo":       ["animation", "adventure", "family", "emotional"],
    "The Lion King":      ["animation", "drama", "family", "emotional"],
    "Parasite":           ["thriller", "drama", "crime", "social"],
    "Pulp Fiction":       ["crime", "thriller", "drama"],
    "The Godfather":      ["crime", "drama", "historical"],
    "Get Out":            ["thriller", "horror", "social"],
    "Iron Man":           ["action", "superhero", "adventure", "sci-fi"],
    "Doctor Strange":     ["action", "superhero", "sci-fi", "mind-bending"],
}

# ---------------------------------------------------------------
# STEP 2: User Ratings Database
# Each user has rated some movies (scale: 1 to 5 stars)
# ---------------------------------------------------------------

user_ratings = {
    "Alice":   {"Inception": 5, "The Matrix": 4, "Interstellar": 5, "Doctor Strange": 3},
    "Bob":     {"Titanic": 5, "The Notebook": 4, "La La Land": 5, "Finding Nemo": 3},
    "Charlie": {"The Dark Knight": 5, "Avengers Endgame": 4, "Iron Man": 5, "Pulp Fiction": 3},
    "Diana":   {"Inception": 4, "Interstellar": 5, "Doctor Strange": 4, "The Matrix": 5},
    "Eve":     {"Toy Story": 5, "Finding Nemo": 5, "The Lion King": 4, "La La Land": 3},
    "Frank":   {"Parasite": 5, "Pulp Fiction": 4, "The Godfather": 5, "Get Out": 4},
    "Grace":   {"The Dark Knight": 4, "Iron Man": 5, "Avengers Endgame": 5, "Inception": 3},
}

# ---------------------------------------------------------------
# METHOD 1: Content-Based Filtering
# "You liked Movie A? Here are movies with similar genres!"
# ---------------------------------------------------------------

def content_based_recommend(liked_movie, top_n=5):
    """
    Finds movies similar to 'liked_movie' based on shared genres/tags.
    
    HOW IT WORKS:
    - Count how many tags the liked movie shares with every other movie
    - Movies with MORE shared tags = more similar = recommended first
    """
    if liked_movie not in movies:
        print(f"Sorry, '{liked_movie}' is not in our database.")
        return []

    liked_tags = set(movies[liked_movie])  # Tags of the movie you liked
    similarity_scores = {}

    for movie, tags in movies.items():
        if movie == liked_movie:
            continue  # Skip the same movie

        # Count shared tags
        shared_tags = liked_tags.intersection(set(tags))
        similarity_scores[movie] = len(shared_tags)

    # Sort by most shared tags (highest similarity first)
    sorted_movies = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)

    # Return top N results (only movies with at least 1 shared tag)
    recommendations = [(m, s) for m, s in sorted_movies if s > 0][:top_n]
    return recommendations

# ---------------------------------------------------------------
# METHOD 2: Collaborative Filtering
# "Users similar to you loved these movies!"
# ---------------------------------------------------------------

def calculate_similarity(user1_ratings, user2_ratings):
    """
    Calculates how similar two users are based on their ratings.
    
    HOW IT WORKS:
    - Find movies both users have rated
    - Compare their ratings for those movies
    - Users with similar ratings = similar taste
    """
    # Find movies both users rated
    common_movies = set(user1_ratings.keys()) & set(user2_ratings.keys())

    if not common_movies:
        return 0  # No common movies = no similarity

    # Calculate the difference in ratings for each common movie
    total_diff = sum(abs(user1_ratings[m] - user2_ratings[m]) for m in common_movies)

    # Similarity: smaller difference = more similar
    # Formula: 1 / (1 + average_difference)  →  always between 0 and 1
    similarity = 1 / (1 + total_diff / len(common_movies))
    return round(similarity, 3)

def collaborative_recommend(target_user, top_n=5):
    """
    Recommends movies by finding users similar to 'target_user'
    and suggesting movies they loved that target_user hasn't seen.
    """
    if target_user not in user_ratings:
        print(f"User '{target_user}' not found.")
        return []

    target_ratings = user_ratings[target_user]
    similarity_with_others = {}

    # Compare target_user with every other user
    for user, ratings in user_ratings.items():
        if user == target_user:
            continue
        similarity_with_others[user] = calculate_similarity(target_ratings, ratings)

    # Sort users by similarity (most similar first)
    similar_users = sorted(similarity_with_others.items(), key=lambda x: x[1], reverse=True)

    # Collect movie suggestions from similar users
    movie_scores = {}
    for similar_user, similarity in similar_users:
        for movie, rating in user_ratings[similar_user].items():
            if movie not in target_ratings:  # Only suggest unseen movies
                if movie not in movie_scores:
                    movie_scores[movie] = 0
                # Weight the rating by how similar that user is
                movie_scores[movie] += rating * similarity

    # Sort by weighted score
    sorted_recommendations = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations[:top_n]

# ---------------------------------------------------------------
# STEP 3: Display functions — make output pretty
# ---------------------------------------------------------------

def display_content_recommendations(liked_movie):
    print(f"\n🎬 Because you liked '{liked_movie}', you might also enjoy:")
    print("-" * 45)
    results = content_based_recommend(liked_movie)
    if not results:
        print("  No similar movies found.")
    for i, (movie, score) in enumerate(results, 1):
        shared = set(movies[liked_movie]) & set(movies[movie])
        print(f"  {i}. {movie}")
        print(f"     ↳ Shared themes: {', '.join(shared)}")

def display_collaborative_recommendations(user):
    print(f"\n👥 Movies recommended for '{user}' (based on similar users):")
    print("-" * 45)
    results = collaborative_recommend(user)
    if not results:
        print("  No recommendations found.")
    for i, (movie, score) in enumerate(results, 1):
        print(f"  {i}. {movie}  (match score: {score:.2f})")

# ---------------------------------------------------------------
# STEP 4: Interactive Menu
# ---------------------------------------------------------------

def show_menu():
    print("\n" + "=" * 50)
    print("      🎥 MOVIE RECOMMENDATION SYSTEM")
    print("=" * 50)
    print("1. Content-Based Recommendation (by genre)")
    print("2. Collaborative Recommendation (by similar users)")
    print("3. Show all movies")
    print("4. Show all users")
    print("5. Exit")
    print("=" * 50)

def run_recommender():
    print("\nWelcome to the CodSoft Movie Recommender! 🍿")

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\nAvailable movies:")
            for i, movie in enumerate(movies.keys(), 1):
                print(f"  {i}. {movie}")
            liked = input("\nEnter a movie you liked: ").strip()
            display_content_recommendations(liked)

        elif choice == "2":
            print("\nAvailable users:")
            for i, user in enumerate(user_ratings.keys(), 1):
                print(f"  {i}. {user}")
            user = input("\nEnter your name (from the list): ").strip()
            display_collaborative_recommendations(user)

        elif choice == "3":
            print("\n📚 All Movies in Database:")
            for movie, tags in movies.items():
                print(f"  • {movie}: {', '.join(tags)}")

        elif choice == "4":
            print("\n👤 All Users & Their Ratings:")
            for user, ratings in user_ratings.items():
                print(f"\n  {user}:")
                for movie, rating in ratings.items():
                    print(f"    ⭐ {rating}/5 — {movie}")

        elif choice == "5":
            print("\nGoodbye! Happy watching! 🎬")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

# ---------------------------------------------------------------
# Run the recommender
# ---------------------------------------------------------------
if __name__ == "__main__":
    run_recommender()
