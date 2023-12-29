def recommend(user_profile):
    # Mock logic for recommendations based on user interests
    interests = user_profile.get("interests", [])
    recommendations = {interest: f"Content for {interest}" for interest in interests}
    return recommendations
