from models.operacao import Operacao
from database import cadastrar_operacao, listar_operacoes, criar_tabela

criar_tabela()

op = Operacao(
    "2026-10-21",
    "PETR4",
    10,
    35.00,
    "compra"
)

cadastrar_operacao(op)

print("Operações cadastradas:")

for operacao in listar_operacoes():
    print(operacao)
