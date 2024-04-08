from flask import Flask, jsonify
import random 
from affirmations import affirmations

app = Flask(__name__)

@app.route('/')
def generate_random_affirmation():
    affirmation = random.choice(affirmations)
    return jsonify(affirmation)

@app.route('/love')
def generate_random_love_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Love' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/friendship')
def generate_random_friendship_affirmation():
    friendship_affirmations = [affirmation for affirmation in affirmations if 'Friendship' in affirmation['category']]
    affirmation = random.choice(friendship_affirmations)
    return jsonify(affirmation)