CREATE TABLE IF NOT EXISTS  operacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL, 
    ativo TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    valor_unitario REAL NOT NULL,
    tipo_operacao TEXT NOT NULL,
    valor_bruto REAL NOT NULL,
    taxas REAL NOT NULL,
    valor_liquido REAL NOT NULL
);