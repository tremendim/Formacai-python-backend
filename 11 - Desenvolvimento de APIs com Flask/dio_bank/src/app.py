from flask import Flask, url_for, request

app = Flask(__name__)

@app.route("/olamundo/<usuario>/<int:idade>")
def hello_world(usuario, idade):
    print(idade)
    print(type(idade))
    return f"<p>Ola mundo! usuario:{usuario.upper()}!</p>"

@app.route("/bemvindo")
def bem_vindo():
    return "<p>Bem, vindo!</p>"


@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about', methods=['GET','POST'])
def about():
    if request.method == 'GET':
        return 'This is a GET'
    else:
        return 'This is a Post'

with app.test_request_context():
    print(url_for('bem_vindo'))
    print(url_for('projects'))
    print(url_for('about', next='/'))
    print(url_for('hello_world', usuario="guilherme", idade=29))