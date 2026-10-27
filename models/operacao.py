import re
from daos.operacao_dao import OperacaoDAO


class Operacao:

    def __init__(self, data, ativo, quantidade, valor_unitario, tipo_operacao):
        self.data = data
        self.ativo = ativo
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.tipo_operacao = tipo_operacao

        # Calcula o valor bruto
        self.valor_bruto = quantidade * valor_unitario

        # Calcula as taxas de 0.03%
        self.taxas = self.valor_bruto * 0.0003

        # Calcula o valor líquido
        if tipo_operacao == 'compra':
            self.valor_liquido = self.valor_bruto + self.taxas
        else:
            self.valor_liquido = self.valor_bruto - self.taxas

    # Cadastra uma operação
    @staticmethod
    def validar(data, ativo, quantidade, valor_unitario, tipo_operacao):
        erros = []

        # Verifica o formato do código do ativo
        if not re.fullmatch(r'[A-Z]{4}[0-9]{1,2}', ativo):
            erros.append(
                'O ativo deve ter 4 letras maiúsculas e 1 ou 2 números.'
            )

        # Verifica se a quantidade é positiva
        if quantidade <= 0:
            erros.append('A quantidade deve ser maior que zero.')

        # Verifica se o valor unitário é positivo
        if valor_unitario <= 0:
            erros.append('O valor unitário deve ser maior que zero.')

        # Verifica o tipo da operação
        if tipo_operacao not in ['compra', 'venda']:
            erros.append('O tipo deve ser compra ou venda.')

        # Verifica se a data é válida
        try:
            from datetime import date
            date.fromisoformat(data)
        except (ValueError, TypeError):
            erros.append('Informe uma data válida.')

        return erros
    
    def salvar(self): 
        dao = OperacaoDAO()
        return dao.cadastrar(self)

    # Lista todas as operações
    @staticmethod
    def listar_todas():
        dao = OperacaoDAO()
        return dao.listar()

    # Busca uma operação pelo ID
    @staticmethod
    def buscar_id(id):
        dao = OperacaoDAO()
        return dao.buscar_id(id)

    # Atualiza uma operação
    def update(self, id):
        dao = OperacaoDAO()
        return dao.update(id, self) #envia os dados ao DAO para salvar no banco.

    # Exclui uma operação
    @staticmethod
    def excluir(id):
        dao = OperacaoDAO()
        return dao.delete(id)

    # Busca operações usando filtros
    @staticmethod
    def buscar(id=None, ativo=None, data_inicio=None, data_fim=None):
        dao = OperacaoDAO()
        return dao.buscar(id, ativo, data_inicio, data_fim)
  
    #envia os dados ao DAO para salvar no banco.
    