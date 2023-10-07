from flask import render_template, request, flash, redirect, url_for, Blueprint
from confg import db
from Src.Controller.Cartoes import CartoesController

bp_cadCartoes = Blueprint("cadCartao",__name__)

@bp_cadCartoes.route('/cadastroCartao',methods = ['GET','POST'])
def cadastroCartao():
    _CadRFID = request.form.get('rfid')
    _codUsuario = request.form.get('codUsuarioCadastro')

    if request.method == 'POST':
        if any((x is None or len(x)<1) for x in [_CadRFID, _codUsuario]):
            flash('Preencha todos os campos do formulário', 'error')
        else:
            if CartoesController.createCartao(_CadRFID,_codUsuario):
                return render_template('cadastroCartaoRFID.html')
            else:
                flash('Cartão RFID ou Usuário já cadastrado', 'error')
            return render_template('cadastroCartaoRFID.html')

@bp_cadCartoes.route('/ListCartao', methods=['GET'])
def ListCartao():
    # Chame a função CartoesController.ListCartoes() e passe o resultado para render_template
    usuarios = CartoesController.ListCartoes()
    return render_template('listaUsuariosSemcartao.html',usuarios=usuarios)
