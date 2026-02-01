import sqlite3
from datetime import datetime

data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# ----------- função banco de dados -------------------
def criarbando_de_dados():
    connt = sqlite3.connect('banco.db')
    connt.execute("PRAGMA foreign_keys = ON") 
    return connt

# ------------ função criar tabela ---------------
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
# ------------------- função inserir dados -------------------------
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

# ---------------- função atualizar dados -----------------------------------
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
# ------------------ função atualizar dados -----------------------------

def atualizar_dados_bancario(id,saldo):
    connt = criarbando_de_dados()
    try:
        cursor = connt.cursor()
        cursor.execute("""
            UPDATE ContaBancario
            SET saldo=?
            WHERE id=?
        """, (saldo,id))
        connt.commit()
    finally:
        connt.close()

        
# ----------------- função consultar dados ------------------------------
def consultar_dados():
    try:
        connt = criarbando_de_dados()
        curso = connt.cursor()
        curso.execute("SELECT * FROM ContaBancario ORDER BY nome ASC")
        dados = curso.fetchall()
        return dados

    except Exception as e:
        print(e)
# ----------------- função criar tabela extrato --------------------------
def criar_tabela_extrato():
    try:
        conn = sqlite3.connect("banco.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Extrato(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titular_conta TEXT,
            conta_id INTEGER NOT NULL,
            data_movimentacao,
            descricao TEXT,
            valor REAL,
            saldo_apos REAL,
            FOREIGN KEY(conta_id) REFERENCES ContaBancario(id)
        )
        """)
    finally:
        conn.commit()
    

def inserir_no_extrato(contaid,titularconta,data,descricao, valor, saldo_apos):
    criar_tabela_extrato()
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO Extrato (conta_id, titular_conta,data_movimentacao,descricao, valor, saldo_apos)
            VALUES (?, ?, ?, ?, ?,?)
        """, (contaid,titularconta,data,descricao,valor,saldo_apos))

        conn.commit()
        

    except Exception as e:
        conn.rollback()
    finally:
        conn.close()



def set_extrato(valor):
    try:
        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM Extrato WHERE conta_id = ? """, (valor,))
        dados = cursor.fetchall()
        return dados
    finally:
        conn.close()



def transferir(conta_origem, conta_destino, valor):
    conn = sqlite3.connect("banco.db")
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    try:
       
        cursor.execute("SELECT nome,saldo FROM ContaBancario WHERE id = ?", (conta_origem,))
        resultado_origem = cursor.fetchone()
        titular_origem = resultado_origem[0]
        saldo_origem = resultado_origem[1]


        cursor.execute("SELECT nome,saldo FROM ContaBancario WHERE id = ?", (conta_destino,))
        resultado_destino = cursor.fetchone()
        titular_destino = resultado_destino[0]
        saldo_destino = resultado_destino[1]


        novo_saldo_origem = saldo_origem - valor
        novo_saldo_destino = saldo_destino + valor

        cursor.execute(
            "UPDATE ContaBancario SET saldo = ? WHERE id = ?",
            (novo_saldo_origem, conta_origem)
        )

        cursor.execute(
            "UPDATE ContaBancario SET saldo = ? WHERE id = ?",
            (novo_saldo_destino, conta_destino)
        )

            # extrato origem (saída)
        cursor.execute("""
            INSERT INTO Extrato
            (conta_id, titular_conta, data_movimentacao, descricao, valor, saldo_apos)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            conta_origem,
            titular_origem,
            data,
            f"Transferência para conta {conta_destino}",
            -valor,
            novo_saldo_origem
        ))

        # extrato destino (entrada)
        cursor.execute("""
            INSERT INTO Extrato
            (conta_id, titular_conta, data_movimentacao, descricao, valor, saldo_apos)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            conta_destino,
            titular_destino,
            data,
            f"Transferência recebida da conta {conta_origem}",
            valor,
            novo_saldo_destino
        ))



        conn.commit()

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.close()

