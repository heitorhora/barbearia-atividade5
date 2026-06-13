import os
from flask import Flask, render_template, request
import mysql.connector
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)

# Configuração da conexão usando variáveis de ambiente
def get_db():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT')
    )

@app.route('/')
def index():
    return render_template('index.html')

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
    app.run(host='0.0.0.0', port=5000, debug=True)