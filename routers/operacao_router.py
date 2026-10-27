from controllers.operacao_controller import inicio, cadastrar, listar, detalhes, editar, excluir, buscar

def adicionar_rotas(app): #registra os endereços no Flask.
    
    #INICIOOOOO
    app.add_url_rule('/', view_func = inicio, methods=['GET'])
    
    app.add_url_rule(
        '/operacoes/cadastrar',
        view_func=cadastrar,
        methods=['GET', 'POST']
    )
    
    app.add_url_rule(
        '/operacoes',
        view_func = listar,
        methods=['GET']
    )
    
    app.add_url_rule(
        '/operacoes/<int:id>', # - <int:id> permite acessar uma operação pelo ID
        view_func = detalhes,
        methods=['GET']
    )
    
    app.add_url_rule(
        '/operacoes/<int:id>/editar', # - <int:id> permite acessar uma operação pelo ID
        view_func = editar,
        methods=['GET', 'POST']
    )
    
    app.add_url_rule(
        '/operacoes/<int:id>/excluir', # - <int:id> permite acessar uma operação pelo ID
        view_func = excluir,
        methods=['POST']
    )
    
    app.add_url_rule(
        "/operacoes/buscar",
        view_func=buscar,
        methods=["GET"]
    )
    
