from flask import render_template, request, redirect, url_for, flash
from models.operacao import Operacao

def inicio():
    return render_template('index.html')

def cadastrar():
    if request.method == 'POST':
        operacao = Operacao(dados=request.form)
        operacao.validar()

        if operacao.erros:
            for erro in operacao.erros:
                flash(erro, 'danger')
            return render_template('cadastrar.html')
        
        if operacao.salvar():
            flash('Operação cadastrada com Sucesso!', 'success')
        else:
            flash('Não foi possivel se cadastrar a  operação.', 'danger')
        return redirect(url_for('listar'))
    
    return render_template('cadastrar.html')

def listar():
    operacoes = Operacao.listar_todas()
    return render_template('listar.html', operacoes=operacoes)

def detalhes(id):
    operacao = Operacao.buscar_id(id)

    if operacao is None:
        flash('Operaçãop não encontrada.', 'danger')
        return redirect(url_for('listar'))

    return render_template('detalhes.html', operacao=operacao)

def editar(id):
    operacao_atual = Operacao.buscar_id(id)

    if operacao_atual is None:
        flash('Operação não encontrada.', 'danger')
        return redirect(url_for('listar'))
    
    if request.method == 'POST':
       operacao = Operacao(request.form)
       operacao.validar()
       
       if operacao.erros:
            for erro in operacao.erros:
                flash(erro, 'danger')
            return render_template('editar.html', operacao=operacao_atual)
    
       if operacao.update(id):
            flash('Operação atualizada com sucesso!', 'success')
            return redirect(url_for('detalhes', id=id))
       else:
            flash('Não foi possível atualizar a operação.', 'danger')
        
    return render_template('editar.html', operacao=operacao_atual)
    
def excluir(id):
    operacao = Operacao.buscar_id(id)

    if operacao is None:
        flash('Operação não encontrada.', 'danger')
        return redirect(url_for('listar'))
    
    resultado = Operacao.excluir(id)

    if resultado:
        flash('Operação excluida com sucesso!', 'success')
    else:
        flash('Não foi possivel excluir a operação.', 'danger')
    return redirect(url_for('listar'))

def buscar():
    id = request.args.get('id')
    ativo = request.args.get('ativo')
    data_inicio = request.args.get('data_inicio')
    data_fim = request.args.get('data_fim')

    if id:
        try:
            id = int(id)
        except ValueError:
            flash('O ID deve ser um numero inteiro.', 'danger')
            return redirect(url_for('listar'))

    operacoes = Operacao.buscar(
        id=id,
        ativo=ativo,
        data_inicio=data_inicio,
        data_fim=data_fim
    )
    
    return render_template('listar.html', operacoes=operacoes)
    