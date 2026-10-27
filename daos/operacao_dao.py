## Essa pasta contem os comandos SQL especificos das operações. 
# Ela que cuida da pesistencia dos dados e do CRUD

from database.sqlitedb import SQLiteDB

class OperacaoDAO:
    def cadastrar(self, operacao):
        db = SQLiteDB()
        db.conectar()

        query = '''
            INSERT INTO operacoes
            (data, ativo, quantidade, valor_unitario, 
            tipo_operacao, valor_bruto, taxas, Valor_liquido)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        
        params = (
            operacao.data,
            operacao.ativo,
            operacao.quantidade,
            operacao.valor_unitario,
            operacao.tipo_operacao,
            operacao.valor_bruto,
            operacao.taxas,
            operacao.valor_liquido
        )
        
        resultado = db.executar(query, params)
        db.desconectar()

        return resultado
    
    def listar(self):
        db = SQLiteDB()
        db.conectar()

        query = 'SELECT * FROM operacoes ORDER BY id'
        
        resultado = db.consultar(query)
        db.desconectar()
        
        return resultado
    
    def buscar_id(self, id):
        db = SQLiteDB()
        db.conectar()

        query = 'SELECT * FROM operacoes WHERE id = ?'

        resultado = db.consultar(query, (id,)) #(id,) é uma tupla com um único elemento. 
        db.desconectar()

        if resultado:
            return resultado[0]
        #pegamos o primeiro registro encontrado. 
        # Se não houver resultado, retornamos None.

        return None
    
    
    def update(self, id, operacao):
        db = SQLiteDB()
        db.conectar()

        query = '''
            UPDATE operacoes
            SET data = ?, ativo = ?, quantidade = ?,
                valor_unitario = ?, tipo_operacao = ?,
                valor_bruto = ?, taxas = ?, valor_liquido = ?
            WHERE id = ?
        '''
        
        params = (
            operacao.data,
            operacao.ativo,
            operacao.quantidade,
            operacao.valor_unitario,
            operacao.tipo_operacao,
            operacao.valor_bruto,
            operacao.taxas,
            operacao.valor_liquido,
            id
        )
        
        resultado = db.executar(query, params)
        db.desconectar()

        return resultado
    
    def delete(self, id):
        db = SQLiteDB()
        db.conectar()

        query = "DELETE FROM operacoes WHERE id = ?"

        resultado = db.executar(query, (id,))
        
        db.desconectar()
        return resultado
    
    
    def buscar(self, id=None, ativo=None, data_inicio=None, data_fim=None):
        db = SQLiteDB()
        db.conectar()

        query = "SELECT * FROM operacoes WHERE 1=1" #facilita adicionar filtros à consulta.| uma condição que sempre é verdadeira.
        params = []

        
        if id:
            query += " AND id = ?"
            params.append(id)

        if ativo:
            query += " AND ativo LIKE ?"
            params.append('%' + ativo + '%')

        if data_inicio:
            query += " AND data >= ? "
            params.append(data_inicio)

        if data_fim:
            query += " AND data <= ? "
            params.append(data_fim)

        query += " ORDER BY data DESC"

        resultado = db.consultar(query, tuple(params))
        db.desconectar()

        return resultado

        