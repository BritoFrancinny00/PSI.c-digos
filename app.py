from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    #retornar response

@app.route('/cadastro', methods=['GET','POST'])
def register():
    if request.methods == 'GET':
        return render_template('cadastro.html')
    else:
        nome = request.form['nome']
        genero = request.form['genero']

        response = make_response(
            redirect(url_for('preferencia')))
        response.set_cookie('nome', nome, max_age=7*24*3600)

        return response

@app.route('/preferencia')
def preferencia():
    pass
@app.route('/recomendar')
def recomendar():
    pass
    