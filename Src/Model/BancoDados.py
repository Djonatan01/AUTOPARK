from confg import db
from flask_login import UserMixin

#CADASTRO DE CARTOES RFID
class CartaoRFID(db.Model):
  __tablename__= "cartao_rfid"
  idCard = db.Column(db.Integer, primary_key=True, autoincrement=True)
  id = db.Column(db.Integer,db.ForeignKey('usuarios.id'))
  numRfid = db.Column(db.String(8))
  codCadUser = db.Column(db.String(120))
  mensage = db.Column(db.String(120))
  dataMensagem =db.Column(db.String(8))

  def __init__(self,_idUser,_numRfid,_codCadUser,_mensagem,_dataMensagem):
    self.idUser = 0
    self.numRfid = _numRfid
    self.codCadUser = _codCadUser
    self.mensagem = _mensagem
    self.dataMensagem = _dataMensagem

class Registro(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  rfid = db.Column(db.String(8))
  dt = db.Column(db.String(15))
  hr = db.Column(db.String(15))
  statusReg = db.Column(db.String(150))

  def __init__(self, _rfid, _dt,_hr, _statusReg):
    self.rfid = _rfid
    self.dt = _dt
    self.hr = _hr
    self.statusReg = _statusReg

class UserBd(db.Model):
  __tablename__= "usuarios"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  mat = db.Column(db.Integer, unique=True)
  rfid = db.Column(db.String(8), unique=True)
  nome = db.Column(db.String(150))
  endereco = db.Column(db.String(150))
  contato = db.Column(db.String(150))

  def __init__(self, _mat, _rfid, _nome, _endereco, _contato):
    self.mat = _mat
    self.rfid = _rfid
    self.nome = _nome
    self.endereco = _endereco
    self.contato = _contato

class FuncBd(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  mat = db.Column(db.Integer, unique=True)
  nome = db.Column(db.String(150))
  endereco = db.Column(db.String(150))
  contato = db.Column(db.String(150))
  email = db.Column(db.String(150))
  senha = db.Column(db.String(150))

  def __init__(self, _mat, _nome, _endereco, _contato, _email, _senha):
    self.mat = _mat
    self.nome = _nome
    self.endereco = _endereco
    self.contato = _contato
    self.email = _email
    self.senha = _senha
