from Src.Model.BancoDados import CartaoRFID
from confg import db
from sqlalchemy.exc import IntegrityError

class CartoesController:
  def createCartao(rfid,codCadUser):
    cartoes = CartaoRFID(0,rfid.upper(),codCadUser.upper(),'','')
    db.session.add(cartoes)
    try:
      db.session.commit()
      return True
    except IntegrityError:
      db.session.rollback()
      return False

    return {
      "regUser": query,
      "count": queryCount,
      "page": page,
      "per_page": per_page
    }
