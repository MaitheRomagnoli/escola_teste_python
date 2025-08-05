from escola.aluno import calcular_media

def test_calcular_media_entrada_basica_sem_erro():
    #defino as entradas
    entrada = [10.0, 5.0, 6.0, 1.0]

    # executo o codigo
    resultado = calcular_media(entrada)

    # checo a saída
    assert resultado == 5.5