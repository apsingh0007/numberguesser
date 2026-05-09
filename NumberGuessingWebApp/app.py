from flask import Flask, render_template, request, jsonify, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24) # For session management

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0
        session['game_over'] = False
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    data = request.get_json()
    if not data or 'guess' not in data:
        return jsonify({'error': 'Invalid request'}), 400
        
    try:
        user_guess = int(data['guess'])
    except ValueError:
        return jsonify({'error': 'Please enter a valid number.'}), 400

    if session.get('game_over', False):
        return jsonify({'error': 'Game over. Please reset to play again.'}), 400

    session['attempts'] = session.get('attempts', 0) + 1
    session.modified = True
    
    target = session.get('number')
    
    if user_guess < target:
        return jsonify({'status': 'low', 'message': 'Too low! Try again.', 'attempts': session['attempts']})
    elif user_guess > target:
        return jsonify({'status': 'high', 'message': 'Too high! Try again.', 'attempts': session['attempts']})
    else:
        session['game_over'] = True
        return jsonify({'status': 'correct', 'message': f'🎉 Congratulations! You guessed it in {session["attempts"]} attempts.', 'attempts': session['attempts']})

@app.route('/reset', methods=['POST'])
def reset():
    session['number'] = random.randint(1, 100)
    session['attempts'] = 0
    session['game_over'] = False
    return jsonify({'status': 'reset', 'message': 'Game reset. Good luck!'})

if __name__ == '__main__':
    app.run(debug=True)
