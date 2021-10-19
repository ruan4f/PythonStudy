from flask import Flask, render_template, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.debug = True

from database import query


def lista_compras():
    return query('SELECT * FROM produtos')


def cadastrar_compra(form):
    nome = form['nome']
    quantidade = form['quantidade']
    valor_por_unidade = form['valor_por_unidade']

    queryString = """ 
        INSERT INTO produtos(nome, quantidade, valor_por_unidade)
        VALUES ('{0}', {1}, {2})
    """

    query(queryString.format(nome, quantidade, valor_por_unidade))


@app.route('/compra', methods=['GET', 'POST'])
def compra(nome=None):
    if request.method == "POST":
        cadastrar_compra(request.form)

    return render_template("compra.html", compras=lista_compras())


@app.route('/produtos', methods=['GET'])
def produtos(nome=None):
    return render_template("produtos.html")


@app.route('/login/', methods=['GET'])
def inicio(nome=None):
    return render_template("login.html")


# @app.route('/compraProdutos/', methods=['GET'])
# def compraProdutos(nome=None):
#    return render_template("compra.html")

if __name__ == '__main__':
    app.run()
