from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'icc'


class Busca:
    def __init__(self, busca):
        self.busca = busca


lista = []


@app.route('/')
def novo():
    return render_template('novo.html', titulo='ICC - Trabalho Busca Twitter')


@app.route('/criar', methods=['POST', ])
def criar():
    busca = request.form['busca']
    procura = Busca(busca)
    lista.append(procura)
    return redirect('/pesquisa')


@app.route('/pesquisa')
def pesquisa():
    return render_template('lista.html', titulo='Busca no Twitter', procuras=lista)


app.run(debug=True)
