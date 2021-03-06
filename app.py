from flask import Flask, render_template, redirect, flash, url_for, session, request
import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super Secret Unguessable Key'


@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def teardown_request(exception):
    db.disconnect()


@app.route('/')
def index():
    users = db.test_pull()
    return render_template("index.html", users=users)



if __name__ == '__main__':
    app.run(debug=True)