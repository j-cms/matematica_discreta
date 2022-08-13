#Aluna Júlia Cristina Moreira da Silva
#O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) /n
# contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
#em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
#segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
#operações  que  estão  descritas  no  arquivo,  este  número  de  operações  será  um  inteiro;  as  linhas
#seguintes  seguirão  sempre  o  mesmo  padrão  de  três  linhas:  a  primeira  linha  apresenta  o  código  da
#operação  (U para união, I para interseção, D para diferença e C produto cartesiano),  a  segunda  e
#terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
#das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:

operacao = ''
conjunto1 = []
conjunto2=[]
cont_operacao = 1 #index na matriz
cont_conjunto1 = 2
cont_conjunto2 = 3
linhas = []
dados_formatados = []
resultado = 0
string_output = ''
print_operacao = ''

#ler o arquivo de texto
with open("teste1_conjuntos.txt") as entrada:
    dados = entrada.readlines()

#formatar a entrada do arquivo de texto (int e vetores)
for linha in dados:
    linha = linha.split(",")
    linhas = []
    for elemento in linha:
        try:
            elemento=int(elemento)
        except:
            elemento = elemento.replace("'", "")
            elemento = elemento.replace("\n", "")  #tirar os \n

        linhas.append(elemento)
    dados_formatados.append(linhas)

numero_operacoes = int(dados_formatados[0][0]) #primeiro dado da tabela, para sabermos o valor do laço de repeticao

#executar as operações
def resultado_matematico( conjunto1, conjunto2, operacao):
    print(" teste def resultado matematico", operacao,type(operacao), conjunto1,conjunto2)
    resultado = []
    if operacao == ('U'): #uniao
        print('entrei')
        resultado = conjunto2 + conjunto1

    elif operacao == 'I': #interseccao
        print("entrei")
        resultado = []
        for num in conjunto1:
            if num in conjunto2:
                resultado.append(num)

    elif operacao == 'D': #diferença
        resultado = []
        for num in conjunto1:
            if num not in conjunto2:
                resultado.append(num)

    elif operacao == ('C'): #produto cartesiano
        resultado = 1  # pra nao dar erro por ser matriz
        #o que fazer com as letras???
        for c1 in conjunto1:
            for c2 in conjunto2:
                resultado += c1 * c2

    print("o resultado é", resultado)
    return resultado

#formatar a saida dos dados
def formatar_saida(operacao, conjunto1, conjunto2, resultado, print_operacao):
    #exemplo: União: conjunto1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}.Resultado: {3, 5, 67, 7, 1, 2, 4}
    if operacao == ('U'):
        print_operacao = 'União'
    elif operacao == ('I'):
        print_operacao = 'Interseção'
    elif operacao == ( "C"):
        print_operacao = 'Cartesiano'
    elif operacao == ('D'):
        print_operacao = "Diferença"
    print("a operacao em string deve ser", print_operacao)

    string_output = f'{print_operacao}: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}.Resultado: {resultado}'
    string_output = string_output.replace("[", '{')
    string_output = string_output.replace(']', '}')
    string_output = string_output.replace("\n", '')
    string_output = string_output.replace(" '", '')
    string_output = string_output.replace("'", '')
    print(string_output)


def main(operacao, cont_operacao,cont_conjunto2, cont_conjunto1, conjunto1, conjunto2, numero_operacoes, resultado):

    #dividir o arquivo segundo as regras fixas
    for num in range(numero_operacoes):
        operacao = str(dados_formatados[cont_operacao])
        conjunto1 = dados_formatados[cont_conjunto1]
        conjunto2 = dados_formatados[cont_conjunto2]
        operacao = operacao.replace('\n', '')
        cont_operacao += 3 #todos adicionam mais 3 pois é o padrao ate achar valor para a mesma variavel no proximo conjunto
        cont_conjunto2+=3
        cont_conjunto1+=3
        print(operacao, conjunto1, conjunto2)

        resultado_matematico( conjunto1, conjunto2, operacao)
        formatar_saida(operacao, conjunto1, conjunto2, resultado, print_operacao)

main(operacao, cont_operacao,cont_conjunto2, cont_conjunto1, conjunto1, conjunto2, numero_operacoes, resultado)

#arrumar o resultado
#arrumar o print das operacoe


