from unittest import installHandler
from flask import Blueprint, render_template


views = Blueprint('views', __name__)

@views.route('/')
def home():
    
   
    return render_template("index.html")

# rotas #
# Esse arquivo define as rotas do Python, acredito que não teremos mais que um arquivo html, mas se for necessário, eu crio mais rotas #