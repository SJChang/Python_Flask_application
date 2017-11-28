from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/flaskmovie'
app.debug=True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
        nation = db.Column(db.String(80),unique=False)
        organization = db.Column(db.String(120),unique=False)
        name = db.Column(db.String(120),unique=False)
        title = db.Column(db.String(80),unique=False)
        phone = db.Column(db.String(100),unique=False)
        email = db.Column(db.String(120),unique=False)
        meet = db.Column(db.String(120),unique=False)
        
        def __init__(self, nation, organization, name, title, phone, email, meet):
            self.nation = nation
                self.organization = organization
                self.name = name
                self.title = title
                self.phone = phone
                self.email = email
                self.meet = meet
        def __repr__(self):
            return '<User %r>' % self.name



@app.route('/')
def index():
    myUser = User.query.all()
        oneItem = User.query.filter_by(nation="1").all()
        return render_template('add_user.html', myUser = myUser,oneItem=oneItem)


@app.route('/profile/<name>')
def profile(name):
    user = User.query.filter_by(name=name).first()
        return render_template('profile.html', user=user)

@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['nation'],request.form['organization'],request.form['name'],request.form['title'],request.form['phone'],request.form['email'],request.form['meet'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()