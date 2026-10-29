from flask import Flask
from database.sqlitedb import SQLiteDB
from routers.operacao_router import adicionar_rotas

app = Flask(__name__)
#permite que o Flask proteja os dados usados nas mensagens temporárias da sessão
app.secret_key = 'chave-temporaria'

db = SQLiteDB()
db.conectar()
db.executar_script_sql("database/scripts/tabela_op.sql")
db.desconectar()

# Registra as rotas do sistema
adicionar_rotas(app)

if __name__ == "__main__":
    app.run(debug=True)