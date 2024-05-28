from flask import request
from Src.Model.BancoDados import Usuarios, CartaoRFID
from config import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import aliased


class CartoesController:
    def createCartao(rfid, idUser):
        rfidCadastrado = db.session.query(
            CartaoRFID).filter_by(numRfid=rfid).first()
        if rfidCadastrado == None:
            cartoes = CartaoRFID(idUser, rfid.upper(),
                                 'Mendagem', 'Data Mensagem')
            db.session.add(cartoes)
            try:
                db.session.commit()
                return True
            except IntegrityError:
                db.session.rollback()
                return False
        else:
            return False

    def ListCartoes():
      usuarios_sem_cartao_rfid = db.session.query(Usuarios).outerjoin(CartaoRFID, Usuarios.id == CartaoRFID.id).\
          filter(CartaoRFID.idCard == None, Usuarios.status != "ADMIN").all()

      return usuarios_sem_cartao_rfid

    def FiltrarUsuarios(codUser):
        usuarios_sem_cartao_rfid = Usuarios.query.filter(Usuarios.codUser.like('%'+codUser+'%'))
        return usuarios_sem_cartao_rfid
