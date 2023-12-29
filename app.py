from flask import Flask, jsonify, request
from model import recommend  # Ensure model.py is in the same directory

app = Flask(__name__)
users = {
    "username1": {
        "learning_styles": ["visual", "auditory"],
        "interests": ["math", "science"],
        "performance": {"math": 80, "science": 90}
    }
}

@app.route('/api/user/<username>', methods=['GET', 'POST'])
def user(username):
    if request.method == 'GET':
        return jsonify(users.get(username, "User not found"))
    elif request.method == 'POST':
        user_data = request.get_json()  # Parse JSON data from request
        users[username] = user_data
        return jsonify(users[username])

@app.route('/api/recommend/<username>', methods=['GET'])
def recommend_resources(username):
    user_profile = users.get(username)
    if user_profile:
        recommendations = recommend(user_profile)  # Get recommendations
        return jsonify(recommendations)
    return jsonify("User not found"), 404

@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
