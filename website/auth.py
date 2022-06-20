from xmlrpc.client import boolean
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logout():
    return "saiu"

@auth.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')


# vou dar uma lida melhodor de como utilizar o blueprint (ferramenta do flask para mecanismo de login) #