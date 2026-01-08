import sqlite3

def criarbando_de_dados():
    connt = sqlite3.connect('banco.db')
    connt.execute("PRAGMA foreign_keys = ON") 
    return connt

def criartabela():
    connt = criarbando_de_dados()
    connt.cursor()
    connt.execute("""CREATE TABLE IF NOT EXISTS ContaBancario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cpf TEXT,
        email TEXT,
        telefone TEXT,
        conta TEXT,
        agencia TEXT,
        login TEXT,
        senha TEXT,
        saldo REAL
            )""")

def inserir_dados(nome,cpf,email,telefone,conta,agencia,login,senha,saldo):
    try:
        criartabela()
        connt = criarbando_de_dados()
        connt.execute("INSERT INTO ContaBancario(nome,cpf,email,telefone,conta,agencia,login,senha,saldo) VALUES(?,?,?,?,?,?,?,?,?)", (nome,cpf,email,telefone,conta,agencia,login,senha,saldo))
        connt.commit()
        connt.close()
        print('Dados inseridos com sucesso')

    except Exception as e:
        print(e)


def update_dados(id, nome, cpf, email, telefone, conta, agencia, login, senha):
    connt = criarbando_de_dados()
    try:
        cursor = connt.cursor()
        cursor.execute("""
            UPDATE ContaBancario
            SET nome=?, cpf=?, email=?, telefone=?, conta=?, agencia=?, login=?, senha=?
            WHERE id=?
        """, (nome, cpf, email, telefone, conta, agencia, login, senha, id))
        connt.commit()
    finally:
        connt.close()

        

def consultar_dados():
    try:
        connt = criarbando_de_dados()
        curso = connt.cursor()
        curso.execute("SELECT * FROM ContaBancario")
        dados = curso.fetchall()
        return dados

    except Exception as e:
        print(e)

def criar_tabela_extrato():
    conn = sqlite3.connect("banco.db")
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Extrato(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        conta_id INTEGER NOT NULL,
        data_movimentacao DATETIME DEFAULT CURRENT_TIMESTAMP,
        descricao TEXT,
        valor REAL,
        saldo_apos REAL,
        FOREIGN KEY(conta_id) REFERENCES ContaBancario(id)
    )
    """)

    conn.commit()
    conn.close()
