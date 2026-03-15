from flask import Flask, request, session, redirect, url_for, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import pyotp
from datetime import timedelta
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(minutes=15)

limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day"], storage_uri="memory://")

usuarios_db = {} # Em produção, usaríamos SQLite/PostgreSQL

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in usuarios_db:
            flash("Erro: Usuário já cadastrado.")
            return redirect(url_for('registro'))
        
        hash_senha = generate_password_hash(password, method='pbkdf2:sha256:600000')
        segredo_2fa = pyotp.random_base32()
        usuarios_db[username] = {'senha_hash': hash_senha, 'segredo_2fa': segredo_2fa}
        
        flash(f"CONTA CRIADA! Salve sua chave 2FA no app: {segredo_2fa}")
        return redirect(url_for('login'))
    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuario = usuarios_db.get(username)
        if usuario and check_password_hash(usuario['senha_hash'], password):
            session['pending_user'] = username
            return redirect(url_for('validar_2fa'))
        flash("Credenciais inválidas.")
    return render_template('login.html')

@app.route('/2fa', methods=['GET', 'POST'])
def validar_2fa():
    if 'pending_user' not in session: return redirect(url_for('login'))
    if request.method == 'POST':
        codigo = request.form['codigo']
        username = session['pending_user']
        totp = pyotp.TOTP(usuarios_db[username]['segredo_2fa'])
        if totp.verify(codigo):
            session.permanent = True
            session['usuario'] = username
            session.pop('pending_user', None)
            return redirect(url_for('dashboard'))
        flash("Código 2FA incorreto.")
    return render_template('2fa.html')

@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session: return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
