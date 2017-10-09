from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'aSecret'

@app.route('/')
def indexPage():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')
@app.route('/reset', methods=['POST'])
def resetCount():
    session['count'] = 0
    return redirect('/')
app.run(debug=True)