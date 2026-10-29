## Esse arquivo contem os comandos SQL especificos das operações. 
# Ela que cuida da pesistencia dos dados e do CRUD

from database.sqlitedb import SQLiteDB

class OperacaoDAO:
    
    def cadastrar(self, dados: dict):
        db = SQLiteDB()
        db.conectar()

        query = '''
            INSERT INTO operacoes
            (data, ativo, quantidade, valor_unitario, 
            tipo_operacao, valor_bruto, taxas, valor_liquido)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        data = dados.get('data')
        ativo = dados.get('ativo')
        quantidade = dados.get('quantidade')
        valor_unitario = dados.get('valor_unitario')
        tipo_operacao = dados.get('tipo_operacao')
        bruto = dados.get('valor_bruto')
        taxas = dados.get('taxas')
        valor_liquido = dados.get('valor_liquido')
        
        resultado = db.executar(query=query, params=(data, ativo, quantidade, valor_unitario, tipo_operacao, bruto, taxas, valor_liquido ))
        db.desconectar()

        return resultado
    
    def _dados_dict(self, row):
        return{
            'id': row['id'],
            'data': row['data'],
            'ativo': row['ativo'],
            'quantidade': row['quantidade'],
            'valor_unitario': row['valor_unitario'],
            'tipo_operacao': row['tipo_operacao'],
            'valor_bruto': row['valor_bruto'],
            'taxas': row['taxas'],
            'valor_liquido': row['valor_liquido'],
        }
    
    def listar(self):
        db = SQLiteDB()
        db.conectar()

        query = 'SELECT * FROM operacoes ORDER BY id'
        
        resultado = db.consultar(query)
        db.desconectar()
        
        if resultado is None:
            return None
        return [self._dados_dict(row) for row in resultado]
    
    def buscar_id(self, id):
        db = SQLiteDB()
        db.conectar()

        query = 'SELECT * FROM operacoes WHERE id = ?'

        resultado = db.consultar(query, (id,)) #(id,) é uma tupla com um único elemento. 
        db.desconectar()

        if resultado:
            return self._dados_dict(resultado[0])
        #pegamos o primeiro registro encontrado. 
        # Se não houver resultado, retornamos None.
        return None
    
    
    def update(self, id, dados: dict):
        db = SQLiteDB()
        db.conectar()

        query = '''
            UPDATE operacoes
            SET data = ?, ativo = ?, quantidade = ?,
                valor_unitario = ?, tipo_operacao = ?,
                valor_bruto = ?, taxas = ?, valor_liquido = ?
            WHERE id = ?
        '''
        
        data = dados.get('data')
        ativo = dados.get('ativo')
        quantidade = dados.get('quantidade')
        valor_unitario = dados.get('valor_unitario')
        tipo_operacao = dados.get('tipo_operacao')
        bruto = dados.get('valor_bruto')
        taxas = dados.get('taxas')
        valor_liquido = dados.get('valor_liquido')
        
        resultado = db.executar(query=query, params=(data, ativo, quantidade, valor_unitario, tipo_operacao, bruto, taxas, valor_liquido, id))
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
        
        if resultado is None:
            return None
        return [self._dados_dict(row) for row in resultado]
    

        