import os
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = 'chave_secreta_barbearia' # Necessário para criar a sessão do usuário

# Configuração da conexão usando variáveis de ambiente
def get_db():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME'),
        port=int(os.environ.get('DB_PORT', 3306)) 
    )

@app.route('/')
def index():
    return render_template('index.html')

# Rota de Login (NOVA)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        conn = get_db()
        cursor = conn.cursor()
        sql = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
        cursor.execute(sql, (email, senha))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if usuario:
            # Se achou o usuário, salva na sessão e manda pro agendamento
            session['usuario_logado'] = email
            return redirect(url_for('agendar'))
        else:
            # Se a senha estiver errada, recarrega a página de login com erro
            return render_template('login.html', erro="E-mail ou senha incorretos!")
            
    return render_template('login.html')

# Rota de Logout (NOVA)
@app.route('/logout')
def logout():
    session.pop('usuario_logado', None) # Remove o usuário da sessão
    return redirect(url_for('index'))

# Rota de Cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        conn = get_db()
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (email, senha) VALUES (%s, %s)"
        cursor.execute(sql, (email, senha))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('cadastro_sucesso.html')
    return render_template('cadastro.html')

# Rota de Agendamento
@app.route('/agendar', methods=['GET', 'POST'])
def agendar():
    # VERIFICAÇÃO DE SEGURANÇA: Se não estiver logado, manda pro login
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        servico = request.form['servico']
        data = request.form['data']
        hora = request.form['hora']
        
        conn = get_db()
        cursor = conn.cursor()
        sql = "INSERT INTO agendamentos (servico, data_agendamento, horario) VALUES (%s, %s, %s)"
        cursor.execute(sql, (servico, data, hora))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('confirmacao.html')
    return render_template('agendamento.html')

# Rota de Listagem (Requisito da Atividade 4)
@app.route('/listar')
def listar():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT servico, data_agendamento, horario FROM agendamentos")
    agendamentos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('listar.html', agendamentos=agendamentos)

if __name__ == '__main__':
    # Modificado para permitir conexões externas dentro do contêiner Docker
    app.run(host='0.0.0.0', port=5000, debug=True)