import pytest
from escola.aluno import verificar_aprovacao

@pytest.mark.parametrize("entrada, situacao_esperada",
                         [
                         ([0.0, 0.0, 0.0, 0.0], "reprovado"),
                         ([10.0, 10.0, 10.0, 10.0], "aprovado"),
                         ([7.0], "aprovado"),
                         ([5.0, 8.8, 6.7, 2.0, 5.3, 8.8, 9.9], "recuperacao"),
                         ([5.8, 9.3], "aprovado"),
                         ([0.8, 0.0, 0.0], "reprovado"),
                         ([5, 6, 10], "aprovado")
                         ]               
)

def test_aprovacao_parametrizadas(entrada, situacao_esperada):
    resultado = verificar_aprovacao(entrada)

    assert resultado == situacao_esperada