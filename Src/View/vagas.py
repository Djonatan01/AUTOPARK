from flask import Blueprint, render_template,request,flash
from flask_login import login_required
from Src.Controller.Vagas import ControleVagas
from Src.Model.BancoDados import Vagas

vaga = Blueprint('vagas',__name__)

@vaga.route('/Cadastrar')
def Cadastrar():
  ultimaVaga = Vagas.query.order_by(Vagas.idVaga.desc()).first().nVaga
  if ultimaVaga is None:
    ultimaVaga = 0
  else:
    ultimaVaga = ultimaVaga.split("-")
    ultimaVaga = int(ultimaVaga[0])

  return render_template('cadastrarVagas.html',ultimaVaga = ultimaVaga + 1)

@vaga.route('/cadastro',methods = ['POST'])
def cadastro():
  if request.method == 'POST':
    _NumVaga = request.form.get('NumVaga')
    _TipoVaga = request.form.get('TipoVaga')
    if _NumVaga != "" and _TipoVaga != "" :
      ControleVagas.CadastroVaga(_NumVaga,_TipoVaga)
    else:
      flash("Todos os campos devem estar preenchidos",'error')

    ultimaVaga = Vagas.query.order_by(Vagas.idVaga.desc()).first().nVaga
    ultimaVaga = ultimaVaga.split("-")
    ultimaVaga = int(ultimaVaga[0])
    return render_template('cadastrarVagas.html',ultimaVaga = ultimaVaga + 1)

@vaga.route('/reserve')
@login_required
def reserve():

 CountVagas = ControleVagas.ConsultaTotalVagas()
 print(CountVagas)
 return render_template('reserve.html')