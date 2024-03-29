from flask import Flask, render_template, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.debug = True

from database import query


def lista_compras():
    return query('SELECT * FROM compras')


def lista_produtos():
    return query('SELECT * FROM produtos')


def cadastrar_compra(form):
    nome = form['nome']
    quantidade = form['quantidade']
    valor_por_unidade = form['valor_por_unidade']

    preco_medio = 0
    if valor_por_unidade and quantidade and int(quantidade) != 0:
        quantidade = int(quantidade)
        valor_por_unidade = int(valor_por_unidade)

        preco_medio = valor_por_unidade / quantidade

    queryString = """ 
        INSERT INTO compras(nome, quantidade, valor_por_unidade, preco_medio)
        VALUES ('{0}', {1}, {2}, {3})
    """

    query(queryString.format(nome, quantidade, valor_por_unidade, preco_medio))


def cadastrar_produto(form):
    nome = form['nome']

    queryString = """ 
        INSERT INTO produtos(nome) VALUES ('{0}')
    """

    query(queryString.format(nome))


@app.route('/')
def login(nome=None):
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def logar(nome=None):
    return redirect("compra")


@app.route('/compra', methods=['GET', 'POST'])
def compra(nome=None):
    if request.method == "POST":
        cadastrar_compra(request.form)

    return render_template("compra.html", compras=lista_compras())


@app.route('/produtos', methods=['GET', 'POST'])
def produtos(nome=None):
    if request.method == "POST":
        cadastrar_produto(request.form)

    return render_template("produtos.html", produtos=lista_produtos())





# @app.route('/compraProdutos/', methods=['GET'])
# def compraProdutos(nome=None):
#    return render_template("compra.html")

if __name__ == '__main__':
    app.run()
