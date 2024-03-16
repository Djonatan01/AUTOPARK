from flask import Blueprint, render_template,request

vaga = Blueprint('vagas',__name__)

@vaga.route('/Cadastrar')
def Cadastrar():
  return render_template('cadastrarVagas.html')