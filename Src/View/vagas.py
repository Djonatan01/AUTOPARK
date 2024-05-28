from flask import Blueprint, render_template,request,flash,jsonify
from flask_login import login_required
from Src.Controller.Vagas import ControleVagas
from Src.Model.BancoDados import Vagas
import json
from pytz import timezone
from datetime import datetime, timedelta

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

@vaga.route('/consultaVagas')
@login_required
def consultaVagas():

  CountVagas, descricaoVagas,idVagas = ControleVagas.ConsultaTotalVagas()

  novaLista = json.dumps(descricaoVagas)

  statusVagas = ControleVagas.consultarStatusVaga()

  statusVagas = json.dumps(statusVagas)

  return render_template('reserve.html', CountVagas = CountVagas, descricaoVagas=novaLista,idVagas=idVagas, statusVagas=statusVagas)

@vaga.route('/reserva', methods=['POST'])
@login_required
#Data e hora da possivel
# atributo (idVaga,iduser,horaChegada,status)
def reserva():

  data = request.get_json()

  vaga_id = data.get('vagaId')
  user_id = data.get('userId')

  sao_paulo = timezone("America/Sao_Paulo")
  now = datetime.now(sao_paulo)
  # Adicionando 30 minutos
  new_time = now + timedelta(minutes=30)
  #hora = now.strftime("%H:%M:%S")
  # Formatando a data e a hora
  data_hora = new_time.strftime("%d/%m/%Y %H:%M:%S")

  # status da vaga L = Livre, O = Ocupada, R = Reservada
  teste = ControleVagas.atualizaStatusVaga(vaga_id,user_id,data_hora,'R')

  return render_template('index.html')