from flask import request
from Src.Model.BancoDados import Usuarios, CartaoRFID
from config import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import aliased
from datetime import datetime
from pytz import timezone

class CartoesController:
    def createCartao(rfid, idUser):
        rfidCadastrado = db.session.query(CartaoRFID).filter_by(numRfid=rfid).first()

        userCadastrado = db.session.query(CartaoRFID).filter_by(id=idUser).first()

        if rfidCadastrado is None and userCadastrado is None:
                # Caso onde o RFID e o usuário não estão cadastrados
                cartoes = CartaoRFID(idUser, rfid.upper(), 'Mendagem', 'Data Mensagem')
                db.session.add(cartoes)
                try:
                    db.session.commit()
                    return True
                except IntegrityError:
                    db.session.rollback()
                    return False

        if userCadastrado is not None and rfidCadastrado is None:
            sao_paulo = timezone("America/Sao_Paulo")
            now = datetime.now(sao_paulo)
            data = now.strftime("%d/%m/%Y")
            hora = now.strftime("%H:%M:%S")
            # Caso onde o usuário já possui um cartão cadastrado, atualize o cartão
            userCadastrado.numRfid = rfid.upper()
            userCadastrado.mensage = 'Alterado o cartão RFID'  # Atualize conforme necessário
            userCadastrado.dataMensagem = data + " | " + hora  # Atualize conforme necessário
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
          filter(Usuarios.status != "ADMIN").all()

      return usuarios_sem_cartao_rfid

    def FiltrarUsuarios(codUser):
        usuarios_sem_cartao_rfid = Usuarios.query.filter(Usuarios.codUser.like('%'+codUser+'%'))
        return usuarios_sem_cartao_rfid
