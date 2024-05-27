from Src.Model.BancoDados import Usuarios, CartaoRFID
from config import db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash
import logging


class UserController:
  """ Controlador para operações relacionadas ao usuário """
  def createUser(codUser, cpf, nome, endereco, contato, email, senha, status):
    """ Cria um novo usuário """
    passwd = generate_password_hash(senha)
    user = Usuarios(cpf.upper(), codUser.upper(), nome.upper(
    ), endereco.upper(), contato.upper(), email, passwd, status.upper())
    db.session.add(user)
    try:
      db.session.commit()
      return True
    except IntegrityError as e:
      logging.error(f"Ocorreu um erro: {e}")
      db.session.rollback()
      return False

  def updateUser(id, _cpf, _codUser, _nome, _endereco, _contato, _email, _status):
    """ Atualiza um usuário existente """
    try:
      Usuarios.query.filter_by(id=id).update({'cpf': _cpf.upper(), 'codUser': _codUser.upper(), 'nome': _nome.upper(
      ), 'endereco': _endereco.upper(), 'contato': _contato.upper(), 'email': _email, 'status': _status.upper()})
      db.session.commit()
      return True
    except IntegrityError as e:
      logging.error(f"Ocorreu um erro: {e}")
      db.session.rollback()
      return False

  def removeUser(id):
    """ Remove um usuário """
    _user = Usuarios.query.filter_by(id=id).first()
    if _user:
      db.session.delete(_user)
      db.session.commit()
    else:
      logging.error(f"Usuário com id {id} não encontrado")
      return False

  def List(page, _userFilter, per_page=15):
    """ Lista os usuários """
    if len(_userFilter) < 1:
      query = Usuarios.query.paginate(page=page, per_page=per_page)
    else:
      query = Usuarios.query.filter(Usuarios.nome.like(
          '%'+_userFilter+'%')).paginate(page=page, per_page=per_page)

    queryCount = Usuarios.query.count()

    return {
        "regUser": query,
        "count": queryCount,
        "page": page,
        "per_page": per_page
    }

  def checkEmail(_email):
    """ Verifica se o email já existe """
    query = Usuarios.query.filter_by(email=_email).first()
    return False if query == None or query == 'None' else True
