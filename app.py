from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super Secret Unguessable Key'


# @app.before_request
# def before_request():
#     # db.connect()
#
#
# @app.teardown_request
# def teardown_request(exception):
#     # db.disconnect()


@app.route('/')
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)