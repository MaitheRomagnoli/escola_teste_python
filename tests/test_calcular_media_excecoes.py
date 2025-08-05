import pytest
from escola.aluno import calcular_media

def test_calcular_media_lista_vazia():
    entrada = []
  
    with pytest.raises(ValueError, match="não é permitida uma lista vazia"):
        calcular_media(entrada)