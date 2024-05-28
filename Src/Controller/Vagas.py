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

        # Contar o número de vagas de acessibilidade
        tvagas = Vagas.query.filter(Vagas.tVaga == "A").count()

        return ContVaga , descricaoVagas, idVagas, tvagas

    def CadastroVaga(numVaga,tipoVaga):
        novaVaga = Vagas(numVaga,tipoVaga.upper())
        db.session.add(novaVaga)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            return False

    def consultarStatusVaga():
        # Filtra os registros onde o status não é "P"
        situacoes_validas = situacaoVagas.query.filter(situacaoVagas.status != "P").all()

        situacaoVaga = [stat.status for stat in situacoes_validas]
        IdVaga = [stat.idVaga for stat in situacoes_validas]

        return {"situacaoVaga": situacaoVaga,
                "IdVaga": IdVaga}

    def atualizaStatusVaga(idVaga, iduser, hEntrada, hSaida, horaChegada, status):
        status = status.upper()
        if hEntrada == "" and hSaida == "":
            vaga_reserva = db.session.query(situacaoVagas).filter_by(idUser=iduser).first()
            if vaga_reserva:
                vaga_reserva.idVaga = idVaga
                vaga_reserva.idUser = iduser
                vaga_reserva.hEntrada = hEntrada
                vaga_reserva.hSaida = hSaida
                vaga_reserva.hChegada = horaChegada
                vaga_reserva.status = status
                try:
                    db.session.commit()
                    return True
                except IntegrityError as e:
                    logging.error(f"Ocorreu um erro ao atualizar a reserva: {e}")
                    db.session.rollback()
                    return False
            if vaga_reserva == None:
                # Registrar nova situação de vaga
                situacaoVaga = situacaoVagas(idVaga, iduser, hEntrada, hSaida, horaChegada, status)
                db.session.add(situacaoVaga)
                try:
                    db.session.commit()
                    return True
                except IntegrityError as e:
                    logging.error(f"Ocorreu um erro ao registrar a nova situação de vaga: {e}")
                    db.session.rollback()
                    return False
        if hEntrada != "":
            # Atualizar a reserva com os novos valores de hEntrada e status
            vaga_reserva = db.session.query(situacaoVagas).filter_by(idSitVaga=idVaga, idUser=iduser).first()
            if vaga_reserva:
                vaga_reserva.hEntrada = hEntrada
                vaga_reserva.status = status
                try:
                    db.session.commit()
                    return True
                except IntegrityError as e:
                    logging.error(f"Ocorreu um erro ao atualizar a reserva: {e}")
                    db.session.rollback()
                    return False

        if hSaida != "":
            # Atualizar o campo hSaida
            vaga_reserva = db.session.query(situacaoVagas).filter_by(idSitVaga=idVaga, idUser=iduser).first()
            if vaga_reserva:
                vaga_reserva.hSaida = hSaida
                vaga_reserva.status = status
                try:
                    db.session.commit()
                    return True
                except IntegrityError as e:
                    logging.error(f"Ocorreu um erro ao atualizar o campo hSaida: {e}")
                    db.session.rollback()
                    return False
        # Registrar nova situação de vaga
        situacaoVaga = situacaoVagas(idVaga, iduser, hEntrada, hSaida, horaChegada, status)
        db.session.add(situacaoVaga)
        try:
            db.session.commit()
            return True
        except IntegrityError as e:
            logging.error(f"Ocorreu um erro ao registrar a nova situação de vaga: {e}")
            db.session.rollback()
            return False
