from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.run(host='0.0.0.0', port=5000, debug=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(100), nullable=False)
    pilot = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)


@app.route("/index")
@app.route("/")
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        team = request.form['team']
        pilot = request.form['pilot']
        year = request.form['year']

        new_post = Post(team=team, pilot=pilot, year=year)

        try:
            db.session.add(new_post)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your post"
    return render_template('create.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
