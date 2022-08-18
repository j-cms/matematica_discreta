# Aluna Júlia Cristina Moreira da Silva
# O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) /n
# contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
# em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
# segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
# operações  que  estão  descritas  no  arquivo,  este  número  de  operações  será  um  inteiro;  as  linhas
# seguintes  seguirão  sempre  o  mesmo  padrão  de  três  linhas:  a  primeira  linha  apresenta  o  código  da
# operação  (U para união, I para interseção, D para diferença e C produto cartesiano),  a  segunda  e
# terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
# das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:

#definir as funcoes de calculos matematicos
def uniao(conjunto1, conjunto2):
    aux = conjunto2 + conjunto1
    resultado = []
    for elem in aux:
        if elem not in resultado:
            resultado.append(elem)

    return resultado


def intersecao(conjunto1, conjunto2):

    resultado = []

    if len(conjunto2) > len(conjunto1):
        conjunto_teste = conjunto2
        outro_conjunto =conjunto1
    else:
        conjunto_teste = conjunto1
        outro_conjunto= conjunto2

    for elem in conjunto_teste:
        if elem in outro_conjunto:
            resultado.append(elem)

    return resultado


def diferenca(conjunto1, conjunto2):

    resultado=[]

    for elem in conjunto1:
        if elem not in conjunto2:
            resultado.append(elem)

    return resultado


def produto_cartesiano(conjunto1, conjunto2):
    resultado = []
    for x in range(0, len(conjunto1)):
        for y in range(0, len(conjunto2)):
            par_ordenado = (conjunto1[x], conjunto2[y])
            resultado.append(par_ordenado)

    return resultado

#ler o arquivo
with open("teste_do_pdf.txt") as entrada:
    n_operacoes = int(entrada.readline())

    # realizar a operacao ao mesmo tempo em que le as diferentes linhas do arquiv
    for linha in range(0, n_operacoes):
        operacao = entrada.readline().strip("\n")          ## cada vez que chamar readline le uma linha diferente, por isso nao ha preocupacao com identacao
        conjunto1 = list(entrada.readline().split(", "))  #transforma em lista e separa com o split, antes era tudo uma unica string gigante
        conjunto2 = list(entrada.readline().split(", "))

        #fors para transformar string para inteiro e formatar as strings remanescentes
        for elemento in range(0, len(conjunto2)):
            resultado = conjunto2
            try:
                resultado[elemento] = int(conjunto2[elemento])
            except:
                resultado[elemento] = (conjunto2[elemento]).strip("'") # tira o '
                resultado[elemento] = (conjunto2[elemento]).strip("\n")  #tira o \n

        for elemento in range(0, len(conjunto1)):
            resultado = conjunto1
            try:
                resultado[elemento] = int(conjunto1[elemento])
            except:
                resultado[elemento] = (conjunto1[elemento]).strip("'")
                resultado[elemento] = (conjunto1[elemento]).strip("\n")

        # formatar a saida de dados conforme solicitado no modelo
        if operacao =='U':
            result = uniao(conjunto1, conjunto2)
            string_conjunto = 'União'

        elif operacao=='I':
            result = intersecao(conjunto1, conjunto2)
            string_conjunto = 'Interseção'

        elif operacao =='D':
            result = diferenca(conjunto1, conjunto2)
            string_conjunto = "Diferença"

        elif operacao =='C':
            result = produto_cartesiano(conjunto1, conjunto2)
            string_conjunto = 'Cartesiano'

        string_output = f'{string_conjunto}: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}.Resultado: {result}'
        string_output = string_output.replace("[", '{')
        string_output = string_output.replace(']', '}')
        string_output = string_output.replace("\n", '')
        string_output = string_output.replace(" '", '')
        string_output = string_output.replace("'", '')
        print(string_output)