from flask import Flask, render_template, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.debug = True

from database import query

@app.route('/')
def produtos(nome=None):
    produtos = query('SELECT * FROM produtos')

    print(produtos)

    return render_template("produtos.html", data = produtos)

@app.route('/produtos/', methods=['POST'])
def handle_data():
    nome = request.form['nome']
    quantidade = request.form['quantidade']
    valor_por_unidade = request.form['valor_por_unidade']
    
    queryString = """ 
        INSERT INTO produtos(nome, quantidade, valor_por_unidade)
        VALUES ('{0}', {1}, {2})
    """

    query(queryString.format(nome, quantidade, valor_por_unidade))
    return render_template('produtos.html')
    
@app.route('/login/', methods=['GET'])
def inicio(nome=None):
     return render_template("login.html")


#@app.route('/compraProdutos/', methods=['GET'])
#def compraProdutos(nome=None):
 #    return render_template("compraProdutos.html")

if __name__ == '__main__':
    app.run()