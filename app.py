from flask import Flask, request, jsonify, render_template, session
import random

app = Flask(__name__)
app.secret_key = 'shadow'  # Set a secret key for session management

active_sessions = 0  # Global variable to track active sessions

@app.before_request
def check_new_session():
    global active_sessions
    if 'visited' not in session:
        session['visited'] = True
        active_sessions += 1
        print(f"New session started. Total active sessions: {active_sessions}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/math-question')
def math_question():
    questions = [
        {"question": "What is 2 + 3?", "answer": 5, "choices": [3, 4, 5, 6]},
        {"question": "What is 7 - 4?", "answer": 3, "choices": [2, 3, 4, 5]},
        {"question": "What part of speech is 'grumpy'?", "answer": "adjective", "choices": ["noun", "verb", "adjective", "adverb"]},
        {"question": "What is the capital of France?", "answer": "Paris", "choices": ["London", "Berlin", "Paris", "Madrid"]},
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter", "choices": ["Mars", "Jupiter", "Saturn", "Earth"]},
        {"question": "What part of speech is 'jumped'?", "answer": "verb", "choices": ["noun", "verb", "adjective", "adverb"]},
        {"question": "What is 12 + 11?", "answer": 23, "choices": [21, 22, 23, 24]},
        # Add more questions as needed
    ]
    question = random.choice(questions)
    
    # Store the current question and answer in the session
    session['question'] = question['question']
    session['answer'] = question['answer']

    return jsonify({
        "question": session['question'],
        "choices": question["choices"]
    })

@app.route('/submit-answer', methods=['POST'])
def submit_answer():
    user_answer = request.json.get("answer")
    #print(f"Expected answer: {session.get('answer')}, User answer: {user_answer}")
    correct = user_answer == session.get("answer")
    
    response = {
        "correct": correct,
        "message": "Correct!" if correct else "Try again!"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
