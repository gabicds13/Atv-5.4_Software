import pytest
from livros import filtrar_livros

@pytest.fixture
def catalogo():
    return [
        {"id": 1, "titulo": "Clean Code", "autor": "Robert C. Martin", "genero": "Tecnologia"},
        {"id": 2, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "genero": "Fantasia"},
        {"id": 3, "titulo": "Refatoração", "autor": "Martin Fowler", "genero": "Tecnologia"}
    ]

def test_deve_filtrar_livros_por_genero(catalogo):
    criterios = {"genero": "Tecnologia"}
    resultado = filtrar_livros(catalogo, criterios)
    assert len(resultado) == 2
    assert resultado[0]["titulo"] == "Clean Code"
    assert resultado[1]["titulo"] == "Refatoração"

def test_deve_filtrar_livros_por_autor(catalogo):
    criterios = {"autor": "J.R.R. Tolkien"}
    resultado = filtrar_livros(catalogo, criterios)
    assert len(resultado) == 1
    assert resultado[0]["titulo"] == "O Senhor dos Anéis"