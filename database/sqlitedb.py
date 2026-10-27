import sqlite3


class SQLiteDB:
    DB_FILE = 'operacao.db'

    def __init__(self):
        self.conn = None
        self.cursor = None
        
    def conectar(self): #Abre a conexao com o BD
        self.conn = sqlite3.connect(self.DB_FILE)
        self.conn.row_factory =  sqlite3.Row #permite acessar os dados retornados pelo banco pelo nome da coluna
        self.cursor = self.conn.cursor()
        
    def desconectar(self): #fecha a conexao com o BD
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
    
    def executar(self, query, params=()): #Executa os comandos para o CRUD
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor.rowcount
        
        except sqlite3.Error as erro:
            self.conn.rollback()
            print("Erro ao executar: ", erro)
            return 0
        
    def consultar(self, query, params=()): #executa consultas como SELECT e devolve os registros.
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        
        except sqlite3.Error as erro:
            print('Erro ao consultar: ', erro)
            return None
        
    def executar_script_sql(self, arquivo): #Lê e executa o arquivo que cria a tabela.
        with open(arquivo, 'r', encoding='utf-8') as f:
            script = f.read()
        
        try:
            self.cursor.executescript(script)
            self.conn.commit()
        except sqlite3.Error as erro:
            self.conn.rollback()
            print("Erro ao criar tabela:", erro)
