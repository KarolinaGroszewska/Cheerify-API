from flask import Flask, jsonify
import random 
from affirmations import affirmations

app = Flask(__name__)

@app.route('/')
def generate_random_affirmation():
    affirmation = random.choice(affirmations)
    return jsonify(affirmation)

@app.route('/acceptance')
def generate_random_acceptance_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Acceptance' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/love')
def generate_random_love_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Love' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/success')
def generate_random_success_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Success' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/happiness')
def generate_random_happiness_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Happiness' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/health')
def generate_random_health_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Health' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/wealth')
def generate_random_wealth_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Wealth' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/gratitude')
def generate_random_gratitude_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Gratitude' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/self-love')
def generate_random_self_love_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Self-love' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/friendship')
def generate_random_friendship_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Friendship' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/family')
def generate_random_family_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Family' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/work')
def generate_random_work_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Work' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/success')
def generate_random_success_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'Success' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)

@app.route('/school')
def generate_random_school_affirmation():
    love_affirmations = [affirmation for affirmation in affirmations if 'School' in affirmation['category']]
    affirmation = random.choice(love_affirmations)
    return jsonify(affirmation)