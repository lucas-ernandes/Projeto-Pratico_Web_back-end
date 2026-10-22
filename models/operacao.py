class Operacao:
    
    def __init__(self, data, ativo, quantidade, valor_unitario, tipo_operacao):
        self.data = data
        self.ativo = ativo
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.tipo_operacao = tipo_operacao
        
        #Calcula o valor bruto
        self.valor_bruto = quantidade * valor_unitario
        
        #Calcula as taxas de 0.03%
        self.taxas =  self.valor_bruto * 0.0003
        
        # Calucula o valor liquido de acordo com o tipo de operacao
        if tipo_operacao == 'compra':
            self.valor_liquido = self.valor_bruto + self.taxas
        else:
            self.valor_liquido = self.valor_bruto - self.taxas