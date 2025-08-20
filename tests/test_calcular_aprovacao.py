import pytest
from escola.aluno import verificar_aprovacao

@pytest.mark.parametrize("entrada, situacao_esperada",
                         [
                         ([0], "reprovado"),
                         ([10], "aprovado"),
                         ([6], "recuperacao"),
                         ]               
)

def test_aprovacao_parametrizadas(entrada, situacao_esperada):
    resultado = verificar_aprovacao(entrada)

    assert resultado == situacao_esperada