from datetime import date
from dateutil.relativedelta import relativedelta

def obter_intervalo(mes: int, ano: int = None):
    """
    Retorna o intervalo entre dia 26 do mês anterior e 25 do mês fornecido.
    
    :param MES: mês de referência (1 a 12), onde o período termina no dia 25
    :param ANO: opcional, se quiser forçar o ano (default = ano atual)
    :return: tupla (data_inicio, data_fim)
    """
    if not (1 <= mes <= 12):
        raise ValueError("O mês deve estar entre 1 e 12.")
    
    today = date.today()
    ano = ano or today.year

    # Se mês de fim for janeiro (1), o mês de início é dezembro do ano anterior
    if mes == 1:
        ano_inicio = ano - 1
        mes_inicio = 12
    else:
        ano_inicio = ano
        mes_inicio = mes - 1

    data_inicio = date(ano_inicio, mes_inicio, 26)
    data_fim = date(ano, mes, 26)  # exclusivo

    return data_inicio, data_fim