from flask import Flask
from database import criar_tabela

app = Flask(__name__)


criar_tabela()

if __name__ == "__main__":
    app.run(debug=True)