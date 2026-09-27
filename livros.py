def filtrar_livros(livros, criterios):
    """Filtra uma lista de dicionários de livros com base nos critérios fornecidos."""
    livros_filtrados = []
    for livro in livros:
        atende_todos = True
        for chave, valor in criterios.items():
            if livro.get(chave) != valor:
                atende_todos = False
                break
        if atende_todos:
            livros_filtrados.append(livro)
    return livros_filtrados