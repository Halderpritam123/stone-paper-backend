from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/play', methods=['POST'])
def play_round():
    choices = ['rock', 'paper', 'scissors']
    data = request.get_json()

    if 'user_choice' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    user_choice = data['user_choice']
    computer_choice = random.choice(choices)

    winner = determine_winner(user_choice, computer_choice)
    result = {
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'winner': winner
    }

    return jsonify(result), 200

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

if __name__ == '__main__':
    app.run(debug=True)
