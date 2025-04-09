from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

questions = [
    {
        "prompt": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which of the following is a valid variable name in Python?",
        "options": ["A. 2name", "B. name_2", "C. name-2", "D. name.2"],
        "answer": "B"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    },
    {
        "prompt": "Who invented the Python programming language?",
        "options": ["A. Guido van Rossum", "B. James Gosling", "C. Dennis Ritchie", "D. Bjarne Stroustrup"],
        "answer": "A"
    },
    {
        "prompt": "Which company developed the Windows operating system?",
        "options": ["A. Apple", "B. Google", "C. IBM", "D. Microsoft"],
        "answer": "D"
    },
    {
        "prompt": "What does HTML stand for?",
        "options": ["A. Hyper Trainer Marking Language", "B. Hyper Text Markup Language", "C. Hyper Text Marketing Language", "D. Home Tool Markup Language"],
        "answer": "B"
    },
    {
        "prompt": "Which one is a version control system?",
        "options": ["A. Git", "B. Node.js", "C. Nginx", "D. MySQL"],
        "answer": "A"
    }
]

@app.route('/')
def index():
    session['score'] = 0
    session['current'] = 0
    session['feedback'] = ''
    return redirect(url_for('question'))

@app.route('/question', methods=['GET', 'POST'])
def question():
    current = session.get('current', 0)
    score = session.get('score', 0)

    if current >= len(questions):
        return redirect(url_for('result'))

    feedback = ''

    if request.method == 'POST':
        selected = request.form.get('answer')
        correct = questions[current]['answer']
        if selected == correct:
            session['score'] = score + 1
            feedback = "✅ Correct!"
        else:
            feedback = f"❌ Wrong! Correct answer was {correct}"

        session['feedback'] = feedback
        session['current'] = current + 1
        return redirect(url_for('question'))

    return render_template("question.html",
                           question=questions[current],
                           qno=current + 1,
                           total=len(questions),
                           score=score,
                           feedback=session.get('feedback', ''))

@app.route('/result')
def result():
    return render_template("result.html",
                           score=session.get('score', 0),
                           total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
