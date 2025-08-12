def calcular_media(entrada:list[float]) -> float:
    """"
    calcula a média de uma lista de notas

    parâmetros:
    notas (list[float]): lista de notas a serem calculadas

    retorna:
    float: a media das notas arredondada para uma casa decimal
    """

    # # verifica se é uma lista
    # if not isinstance(notas,list[float]):

    # validando se a resposta é uma str
    if not isinstance(entrada, list):
        raise TypeError("nota inválida")
    

    # validando se é uma str e uma lista juntos
    for nota in entrada:
        if not isinstance(nota, (int, float)):
            raise TypeError("nota inválida")
        
    
    # validando se é negativo ou maior que dez
    for nota in entrada:
        if nota < 0 or nota > 10:
            raise ValueError("limite da nota [0, 10]")

    # validando se a lista é vazia

    if len(entrada) == 0:
        raise ValueError("não é permitida uma lista vazia")

    media = sum(entrada)/len(entrada)
    
    
    return round(media, 1)
            
    







        

def verificar_aprovacao(entrada:list[float]) -> float:
     # validando se foi aprovado ou reprovado
    for nota in entrada:
        if nota <5:
            raise ValueError("reprovado")
        elif nota > 5 or nota < 6.9:
            raise ValueError("recuperação")
        elif nota >= 7 or nota >= 10:
            print("aprovado")
