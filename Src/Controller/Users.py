from Src.Model.BancoDados import Usuarios, CartaoRFID
from confg import db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

class UserController:
  def createUser(codUser,cpf,nome,endereco,contato,email,senha,status):
    passwd=generate_password_hash(senha)
    user = Usuarios(cpf.upper(),codUser.upper(),nome.upper(),endereco.upper(),contato.upper(),email,passwd,status.upper())
    db.session.add(user)
    try:
      db.session.commit()
      return True
    except IntegrityError:
      db.session.rollback()
      return False

  def updateUser(id, _cpf,_codUser, _nome, _endereco, _contato, _email, _senha,_status):
    try:
      passwd=generate_password_hash(_senha)
      Usuarios.query.filter_by(id=id).update({'cpf':_cpf.upper(),'codUser':_codUser.upper(),'nome':_nome.upper(), 'endereco':_endereco.upper(),'contato':_contato.upper(),'email':_email,'senha':passwd,'status':_status.upper()})
      db.session.commit()
      return True
    except IntegrityError:
      db.session.rollback()
      return False

  def removeUser(id):
    _user = Usuarios.query.filter_by(id=id).first()
    db.session.delete(_user)
    db.session.commit()

  def List(page,_userFilter, per_page=15):
    if len(_userFilter)<1 :
      query = Usuarios.query.paginate(page=page, per_page=per_page)
      queryCount = Usuarios.query.count()
    else:
      query = Usuarios.query.filter(Usuarios.nome.like('%'+_userFilter+'%')).paginate(page=page, per_page=per_page)
      queryCount = Usuarios.query.count()
    return {
      "regUser": query,
      "count": queryCount,
      "page": page,
      "per_page": per_page
    }

  def checkEmail(_email):
    query=Usuarios.query.filter_by(email=_email).first()
    return False if query==None or query=='None' else True
