import re
from datetime import date
from daos.operacao_dao import OperacaoDAO


class Operacao:
    taxa = 0.0003
    
    def __init__(self, dados: dict):
        self.dados = dados  #só vai quardar os valores do form
        self.erros = []


# VALIDAÇÂO
    def validar(self):
        v = self.dados
        ativo = v.get('ativo', '').strip()
        tipo = v.get('tipo_operacao')

        # Verifica o formato do código do ativo
        if not re.fullmatch(r'[A-Z]{4}[0-9]{1,2}', ativo):
            self.erros.append(
                'O ativo deve ter 4 letras maiúsculas e 1 ou 2 números.'
            )

        # Verifica o tipo de operação
        if tipo not in ('compra', 'venda'):
            self.erros.append('O tipo deve ser compra ou venda.')
            
        # Verifica se a data é válida
        try:
            date.fromisoformat(v.get('data'))
        except (ValueError, TypeError):
            self.erros.append('Informe uma data válida.')
            
        # Verifica a quantidade
        try:
            quantidade = int(v.get('quantidade'))
            if quantidade <0:
                self.erros.append('A quantidade deve ser que maior 0!')
        except (ValueError, TypeError):
            self.erros.append("A quantidade tem que ser numero INTEIRO!")


        # Verifica se o valor unitário é positivo
        try:
            valor_unitario = float(v.get('valor_unitario'))
            if valor_unitario <=0:
                self.erros.append('O valor unitário deve ser maior que 0')
        except (ValueError, TypeError):
            self.erros.append('O valor unitário deve ser um número válido.')
            
        
        #só vai calcular agora se TUDO estiver certo(se Deus quiser)
        if not self.erros:
            bruto = quantidade * valor_unitario
            taxas = bruto * self.taxa
            liquido = bruto + taxas if tipo == 'compra' else bruto - taxas
            
            self.dados = {
                'data': v['data'], 'ativo': ativo,
                'quantidade': quantidade, 'valor_unitario': valor_unitario,
                'tipo_operacao': tipo, 'valor_bruto': bruto,
                'taxas': taxas, 'valor_liquido': liquido
            }
    
    def salvar(self): 
        return OperacaoDAO().cadastrar(self.dados) == 1

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
        return  OperacaoDAO().update(id, self.dados) == 1 #envia os dados ao DAO para salvar no banco.

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
    