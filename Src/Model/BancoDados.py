from confg import db
from flask_login import UserMixin

#CADASTRO DE CARTOES RFID
class CartaoRFID(db.Model):
  __tablename__= "cartao_rfid"
  idCard = db.Column(db.Integer, primary_key=True, autoincrement=True)
  id = db.Column(db.Integer,db.ForeignKey('Usuarios.id'))
  numRfid = db.Column(db.String(8))
  mensage = db.Column(db.String(120))
  dataMensagem =db.Column(db.String(8))

  def __init__(self,_id,_numRfid,_mensagem,_dataMensagem):
    self.id = _id
    self.numRfid = _numRfid
    self.mensagem = _mensagem
    self.dataMensagem = _dataMensagem

class Registro(db.Model):
  idRegistro = db.Column(db.Integer, primary_key=True, autoincrement=True)
  id = db.Column(db.Integer,db.ForeignKey('Usuarios.id'))
  rfid = db.Column(db.String(8))
  dt = db.Column(db.String(15))
  hr = db.Column(db.String(15))
  statusReg = db.Column(db.String(150))

  def __init__(self,_id, _rfid, _dt,_hr, _statusReg):
    self.id = _id
    self.rfid = _rfid
    self.dt = _dt
    self.hr = _hr
    self.statusReg = _statusReg

class Usuarios(UserMixin,db.Model):
  __tablename__= "Usuarios"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  cpf = db.Column(db.Integer, unique=True)
  codUser = db.Column(db.Integer, unique=True)
  nome = db.Column(db.String(150))
  endereco = db.Column(db.String(150))
  contato = db.Column(db.String(150))
  email = db.Column(db.String(150))
  senha = db.Column(db.String(150))
  status = db.Column(db.String(3))

  def __init__(self, _cpf,_codUser, _nome, _endereco, _contato, _email, _senha,_status):
    self.cpf = _cpf
    self.codUser=_codUser
    self.nome = _nome
    self.endereco = _endereco
    self.contato = _contato
    self.email = _email
    self.senha = _senha
    self.status = _status
