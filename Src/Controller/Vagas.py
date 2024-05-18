from Src.Model.BancoDados import situacaoVagas,Vagas
from config import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import aliased
import logging

class ControleVagas():
    def ConsultaTotalVagas():
        ContVaga = Vagas.query.count()
        # Consulta todas as vagas
        descricaoVagas = [vaga.tVaga for vaga in Vagas.query.all()]

        idVagas = [vaga.idVaga for vaga in Vagas.query.all()]

        return ContVaga , descricaoVagas, idVagas

    def CadastroVaga(numVaga,tipoVaga):
        novaVaga = Vagas(numVaga,tipoVaga.upper())
        db.session.add(novaVaga)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            return False

    def consultarStatusVaga():

        situacaoVaga = [stat.status for stat in situacaoVagas.query.all()]

        IdVaga = [stat.idVaga for stat in situacaoVagas.query.all()]

        return {"situacaoVaga": situacaoVaga,
                "IdVaga" : IdVaga
                }

    def atualizaStatusVaga(idVaga,iduser,horaChegada,status):
        situacaoVaga = situacaoVagas(idVaga,iduser,"","",horaChegada,status.upper())
        db.session.add(situacaoVaga)
        try:
            db.session.commit()
            return True
        except IntegrityError as e:
            logging.error(f"Ocorreu um erro: {e}")
            db.session.rollback()
        return False