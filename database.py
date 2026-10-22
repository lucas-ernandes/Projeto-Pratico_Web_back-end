import sqlite3

def conectar():
    return sqlite3.connect("operacoes.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS operacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL, 
            ativo TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            valor_unitario REAL NOT NULL,
            tipo_operacao TEXT NOT NULL,
            valor_bruto REAL NOT NULL,
            taxas REAL NOT NULL,
            valor_liquido REAL NOT NULL
        )
''')
    
    conexao.commit() #confirma as alterações feito no banco
    conexao.close() #encerra a conexão
    
# recebe um objeto da classe Operacao pelo parâmetro operacao. 
def cadastrar_operacao(operacao):  # Esse objeto é criado antes, e seus atributos são utilizados para inserir os dados no banco.”
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO operacoes (
            data, ativo, quantidade, valor_unitario, tipo_operacao, valor_bruto, taxas, valor_liquido
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', (
    operacao.data,
    operacao.ativo,
    operacao.quantidade,
    operacao.valor_unitario,
    operacao.tipo_operacao,
    operacao.valor_bruto,
    operacao.taxas,
    operacao.valor_liquido
))
    conexao.commit()
    conexao.close()

def listar_operacoes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM operacoes')

    operacoes = cursor.fetchall()

    conexao.close()
    return operacoes

def buscar_operecoes(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        'SELECT * FROM operacoes WHERE id = ?',
        (id,)
    )
    
    operacao = cursor.fetchone()

    conexao.close()
    return operacao