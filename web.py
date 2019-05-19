from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/About/')
def about():
    return render_template("about.html")

@app.route('/Skills/')
def skills():
    return render_template("skills.html")

if __name__=="__main__":
    app.run(debug=True)
