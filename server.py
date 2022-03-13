from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "***********"

@app.route("/")
def counter_page():
    if 'count' not in session:
        session['count'] = 1 #first time at the page (session set to variable name)
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/clear')
def reset():
    session.clear()
    return redirect("/")


if __name__=="__main__":
        app.run(debug=True)