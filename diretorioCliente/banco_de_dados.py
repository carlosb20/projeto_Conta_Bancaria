import sqlite3

def criarbando_de_dados():
    connt = sqlite3.connect('banco.db')
    return connt

def criartabela():
    connt = criarbando_de_dados()
    connt.cursor()
    connt.execute("CREATE TABLE IF NOT EXISTS ContaBancario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT,cpf TEXT,email TEXT,telefone TEXT,conta TEXT,agencia TEXT,login TEXT,senha TEXT,saldo REAL)")

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
