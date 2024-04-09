from flask import Flask, jsonify
import random 
from affirmations import affirmations
from mock_users import users 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def generate_random_affirmation():
    affirmation = random.choice(affirmations)
    return jsonify(affirmation)

@app.route('/acceptance', methods=['GET'])
def generate_random_acceptance_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Acceptance' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/love', methods=['GET'])
def generate_random_love_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Love' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/success', methods=['GET'])
def generate_random_success_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Success' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/happiness', methods=['GET'])
def generate_random_happiness_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Happiness' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/health', methods=['GET'])
def generate_random_health_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Health' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/wealth', methods=['GET'])
def generate_random_wealth_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Wealth' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/gratitude', methods=['GET'])
def generate_random_gratitude_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Gratitude' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/self-love', methods=['GET'])
def generate_random_self_love_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Self-love' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/friendship', methods=['GET'])
def generate_random_friendship_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Friendship' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/family', methods=['GET'])
def generate_random_family_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Family' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/work', methods=['GET'])
def generate_random_work_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Work' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/school', methods=['GET'])
def generate_random_school_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'School' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

def get_users(id):
 return next((u for u in users if u['id'] == id), None)

@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id: int):
    user = get_users(id)
    if user is None:
        return jsonify({ 'error': 'User does not exist'}), 404
    return jsonify(user)

@app.route('/users/<int:id>/favorite', methods=['GET'])
def get_random_favorite_from_user_by_id(id: int):
    user = get_users(id)
    if user is None:
        return jsonify({ 'error': 'User does not exist'}), 404
    favorite = random.choice(user['favorites'])
    affirmation = [affirmation for affirmation in affirmations if affirmation['id'] == favorite]
    return jsonify(affirmation)

@app.route('/users/<int:id>/custom', methods=['GET'])
def get__random_custom_affirmations_from_user_by_id(id: int):
    user = get_users(id)
    if user is None:
        return jsonify({ 'error': 'User does not exist'}), 404
    custom = random.choice(user['custom'])
    return jsonify(custom)