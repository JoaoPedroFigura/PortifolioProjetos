import datetime
import json
import re

lista_favoritos = []  # Lista para salvar as séries.

lista_concluidas = [] # Apenas series que já foram concluidas

lista_andamento = [] # Apenas series que ainda não foram concluidas

def salvar_series(lista, lista_series_concluidas, lista_series_andamento):
    """
    Salva três listas, em arquivos json diferentes:
    :param lista: pega a lista com todas as séries favoritas, independente se já foi concluida ou não, e salva no arquivo 'series_favoritas.json'
    :param lista_series_concluidas: recebe a lista com apenas as séries que já foram concluidas e salva no arquivo 'series_concluidas.json'
    :param lista_series_andamento: recebe a lista com apenas séries que já foram concluidas e salva no arquivo 'series_andamento.json'
    :return: Não retorna nada, pois apenas salva arquivos json
    """
    with open("series_concluidas.json", "w", encoding="utf-8") as file:
        json.dump(lista_series_concluidas, file, indent=4)
    with open("series_andamento.json", "w", encoding="utf-8") as file:
        json.dump(lista_series_andamento, file, indent=4)
    with open("series_favoritas.json", "w", encoding="utf-8") as file:
        json.dump(lista, file, indent=4)

def recuperar_series(nome_arquivo):
    """
    Acessa o arquivo que estiver no argumento da função
    :return: retorna um dicionário com a lista que estiver dentro do arquivo
    """
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as file:
            dicionario = json.load(file)
            return dicionario
    except (FileNotFoundError, json.JSONDecodeError):
        lista_vazia = []
        return lista_vazia

def verificador_serie_concluida():
    """
    Função auxiliar: pergunta se a série já foi concluida e retorna True ou False
    :return: True ou False
    """
    while True:
        concluida = input("A série já foi concluida? (digite True para sim ou false para não): ").lower()

        if concluida == "true":
            return True
        elif concluida == "false":
            return False
        else:
            print("Valor inválido.")  #

def pesquisa_serie(nome_serie_procurar, lista):
    """
    Pega o nome de uma série e procura se ela está na lista
    :param nome_serie_procurar: nome da série
    :param lista: a lista em que vai procurar
    :return: retorna a série caso encontre
    """
    for serie in lista:
        if serie['nome'] == nome_serie_procurar:
            return serie
    return None

def adicionar_serie(quantidade_series):
    """
    Adiciona séries na lista que foi passada a função
    :param quantidade_series: quantidades de séries a ser adicionadas
    """
    for i in range(quantidade_series):
        nome_serie = input("Digite o nome da série: ")

        while True:
            try:
                qtd_eps = int(input("Digite a quantidade de capítulos da série: "))
                if qtd_eps <1:
                    print("Mesmo que uma série seja curta, é impossível ela ter menos que 1 capítulo!")
                    continue
                break
            except ValueError:
                print("Digite um número inteiro de capítulos, caso seja dividido em partes, cada parte deve ser considerada um capítulo")
        serie_concluida_boolean = verificador_serie_concluida()
        servico_usado = input("Digite o serviço que você viu a série (Streaming, tv, etc): ")
        cadastro_serie = {
            "nome": nome_serie,
            "qtd_capitulos": qtd_eps,
            "serie_concluida": serie_concluida_boolean,
            "servico_usado": servico_usado,
            "historico": []
        }
        if cadastro_serie['serie_concluida'] == False:
            lista_andamento.append(cadastro_serie)
        else:
            lista_concluidas.append(cadastro_serie)
        lista = recuperar_series("series_favoritas.json")
        if any(serie["nome"] == nome_serie for serie in lista):
            print("A série já estava na lista e não foi adicionada novamente!")
        else:
            lista.append(cadastro_serie)
            salvar_series(lista, lista_concluidas, lista_andamento)

def listar_series(lista):
    """
    Exibe uma lista formatada daos itens que esitiverem na lista do parâmetro
    :param lista:
    :return:
    """

    if lista:
        contador = 1  # contador para mostrar as séries de forma progressiva "1.ª 2.ª 3.ª".
        for i in range(len(lista)):
            print("=" * 30)
            print(
                f"{contador}ª {lista[i]['nome']}\nConcluída: {lista[i]['serie_concluida']}\nQuantidade de Capítulos: {lista[i]['qtd_capitulos']}\nServiço utilizado: {lista[i]['servico_usado']}\nHistórico de alterações:")
            for data, nome_antigo, qtd_antiga_capitulos, status_antigo, servico_antigo, nome, qtd_capitulos, concluida, servico_usado in lista[i]['historico']:
                print("=" * 20)
                print(f"Data de alteração: {data}")
                print(f"Nome anterior: {nome_antigo}")
                print(f"Quantidade anterior de capítulos: {qtd_antiga_capitulos} ")
                print(f"Status anterior: {status_antigo}")
                print(f"Serviço anterior: {servico_antigo}")
                print(f"Novo nome: {nome}")
                print(f"Nova quantidade de capitulos: {qtd_capitulos}")
                print(f"Novo Status: {concluida}")
                print(f"Novo serviço: {servico_usado}")
            contador += 1
    else:
        print("WoW Você não tem nenhuma série favorita! Tente adicionar algumas e depois volte aqui.")

def atualizar_serie(nome_serie):
    """
    Atualiza as informações sobre uma série já presente em uma lista
    :param nome_serie: Nome da série que será modificada
    """
    lista = recuperar_series("series_favoritas.json")
    serie = pesquisa_serie(nome_serie, lista)
    if serie:
        nome_antigo = serie['nome']
        status_antigo = serie['serie_concluida']
        qtd_antiga_capitulos = serie['qtd_capitulos']
        servico_antigo = serie['servico_usado']

        serie['nome'] = input("Digite o novo nome da série: ")
        serie['qtd_capitulos'] = input("Digite a nova quantidade de capitulos: ")
        serie['serie_concluida'] = verificador_serie_concluida()
        serie['servico_usado'] = input("Digite o novo nome do serviço utilizado: ")

        if serie['serie_concluida'] != status_antigo:
            if serie['serie_concluida']:
                for s in lista_andamento:
                    if s == serie['nome']:
                        lista_andamento.remove(s)
                        lista_concluidas.append(s)
            else:
                for s in lista_concluidas:
                    if s == serie['nome']:
                        lista_concluidas.remove(s)
                        lista_andamento.append(s)

        data = datetime.datetime.now()

        atualizacao = (str(data), nome_antigo, qtd_antiga_capitulos, status_antigo, servico_antigo, serie["nome"], serie['qtd_capitulos'], serie["serie_concluida"], serie['servico_usado'])
        serie["historico"].append(atualizacao)

        salvar_series(lista, lista_concluidas, lista_andamento)
    else:
        print("A serie não foi encontrada")

def deletar_serie(nome_serie):
    """
    Deleta uma série da lista que foi passada a função
    :param nome_serie: nome da série para remover
    """
    lista = recuperar_series("series_favoritas.json")
    serie = pesquisa_serie(nome_serie, lista)
    if serie:
        lista.remove(serie)
        salvar_series(lista, lista_concluidas, lista_andamento)
        print(f"A serie {serie['nome']} foi removida ")
    else:
        print("Espere! como você quer remover uma série que nem adicionou?")

def estatisticas():
    """
    Exibe estatisticas do projeto
    :return:
    """
    print("Lista de séries concluidas: ")
    listar_series(recuperar_series("series_concluidas.json"))
    qtd_concluidas = len(recuperar_series("series_concluidas.json"))
    print(f"nossa quanta coisa! Você tem {qtd_concluidas} séries concluidas")
    print("=" * 30)
    print("Lista de Séries em Andamento: ")
    listar_series(recuperar_series("series_andamento.json"))
    qtd_andamento = len(recuperar_series("series_andamento.json"))
    print(f"Ainda falta tudo isso? Você tem {qtd_andamento} séries em andamento")
    print("=" * 30)
    print(f"UaU! Você tem um total de {len(recuperar_series("series_favoritas.json"))} favoritas, isso é muita coisa.")

def pesquisar_termo():
    """
    Solicita um termo e verifica as correspondencias do mesmo no arquivo json de séries favoritas

    """
    termo = input("Digite o termo que deseja ver as insidencias: ")
    compativeis = [s for s in recuperar_series("series_favoritas.json")
                   if re.search(re.escape(termo), s['nome'], re.IGNORECASE)]
    listar_series(compativeis)


while True:
    print("=" * 30)  # Imprime "=" 30 vezes
    comando = input("Digite alguma das opções abaixo: "
                    "\n-ADD para adicionar uma nova série."
                    "\n-LIST para listar suas séries favoritas."
                    "\n-UPDATE para atualizar alguma informação"
                    "\n-DELETE para remover alguma série de suas favoritas."
                    "\n-STATS para uma visão geral"
                    "\n SEARCH para buscar séries na lista a partir de termos"
                    "\n-ABOUT para informações sobre o projeto."
                    "\n-QUIT para encerrar o programa."
                    "\n-> ").upper()

    match comando:  # verifica qual ação o usuario deseja realizar.

        case "ABOUT":
            print("Este é projeto da diciplina de Raciocínio Computacional do aluno João Pedro Figura Burkot e tem como objetivo ser um gerenciador de séries favoritas! ")

        case "QUIT":
            print("Encerrando o programa!")
            salvar_series(recuperar_series("series_favoritas.json"), lista_concluidas, lista_andamento)
            break

        case "ADD":
            qtd_series = 0
            while True:
                try:
                    qtd_series = int(input("Quantas séries você gostaria de adicionar?\n-> "))
                    if qtd_series < 1:
                        print("WoW! Como você quer adicionar uma quantidade negativa de séries? (caso queria deletar alguma, utilize o comando delete)")
                        continue
                    break
                except ValueError:
                    print("Você inseriu algo inválido, tente novamente")

            adicionar_serie(qtd_series)

        case "LIST":
            listar_series(recuperar_series("series_favoritas.json"))

        case "UPDATE":
            nome_alterar = input("Digite o nome da série que deseja alterar: ")
            atualizar_serie(nome_alterar)

        case "DELETE":
            nome_deletar = input("Digite o nome da serie que deseja remover: ")
            deletar_serie(nome_deletar)

        case "STATS":
            estatisticas()

        case "SEARCH":
            pesquisar_termo()

        case _:  # caso o usuario digite algo inválido.
            print("ERRO: O comando não foi identificado, por favor digite alguma das opções listadas.")

