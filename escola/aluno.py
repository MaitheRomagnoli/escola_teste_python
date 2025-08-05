def calcular_media(entrada:list[float]) -> float:
    # # verifica se é uma lista
    # if not isinstance(notas,list[float]):

        


    # validando se a lista é vazia
    if len(entrada) == 0:
        raise ValueError("não é permitida uma lista vazia")

    media = sum(entrada)/len(entrada)
    return round(media, 1)
            
        