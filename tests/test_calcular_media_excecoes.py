import pytest
from escola.aluno import calcular_media

def test_calcular_media_lista_vazia():
    entrada = []
  
    with pytest.raises(ValueError, match="não é permitida uma lista vazia"):
        calcular_media(entrada)


def test_calcular_media_str():
    entrada = "ola"
  
    with pytest.raises(TypeError, match="nota inválida"):
        calcular_media(entrada)


def test_calcular_media_str_e_list():
    entrada = ['ola', 1]

    with pytest.raises(TypeError, match= "nota inválida"):
        calcular_media(entrada)



# conferindo se é negativo
def test_calcular_media_num_negativo():
    entrada = [-10.0]

    with pytest.raises(ValueError, match= "limite da nota \[0, 10\]"):
        calcular_media(entrada)

# conferindo se é maior que dez
def test_calcular_media_num_maior_que_dez():
    entrada = [8, 9, 11]

    with pytest.raises(ValueError, match= "limite da nota \[0, 10\]"):
        calcular_media(entrada)