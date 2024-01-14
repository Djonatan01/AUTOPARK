from flask import Blueprint, render_template
from flask_login import login_required

Home = Blueprint('home', __name__)

@Home.route('/')
def index():
  return render_template('index.html')

@Home.route('/reserve')
@login_required
def reserve():
  # Processar a reserva da vaga aqui...
 return render_template('reserve.html')