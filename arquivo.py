
#1. Criar o arquivo
def Escrever_Arquivo(nome, conteudo, estilo): #serve para adicionar uma nova informação
    '''

    :param nome: digitar o nome do arquivo
    :param conteudo: informação que deseja adicionar
    :param estilo: 0 para ';' e 1 para '\n'
    '''

    with open(f'{nome}.txt', 'a') as arquivo: 
        if estilo == 0: 
            arquivo.write(f'{conteudo};')
        elif estilo == 1:
            arquivo.write(f'{conteudo}\n')


lista_dados = [] #Recebe os dados
def Copiar_Arquivo(nome): #Vai adicionar cada item na lista_dados, de maneira organizada e formatada
    '''
    nome: nome do arquivo
    '''
    global lista_dados  # Garante que estamos alterando a variável global
    lista_dados.clear()
    with open(f'{nome}.txt', 'r') as arquivo:
        ler = arquivo.readlines()
        for termo in ler:
            termo = termo.replace('\n', '')
            termo = termo.split(';')
            lista_dados.append(termo)
            

#Copiar_Arquivo('teste') #Para copiar o que está no arquivo

Copiar_Arquivo('assunto')
#2. Ler o arquivo
def Ler_Arquivo(): #Vai ler o arquivo
    '''
    lista: lista que está registrada as informações
    '''
    for itens in lista_dados:
        cor = 31
        for item  in itens:    
            print(f'\033[{cor}m{item:7}', end='    ')
            cor += 1
        print()

def Simples_Arquivo():
    Copiar_Arquivo('assunto')
    return lista_dados


def Alterar_Arquivo(info, nome, linha, coluna): #Vai alterar a informação desejada
    '''
    nome: nome do arquivo
    linha: linha que deseja alterar
    coluna: coluna que deseja alterar
    '''
    #3.1 Alterar o item na lista

    lista_dados[linha-1][coluna-1] = str(info)

    #3.2 Reescrever toda a lista no arquivo novamente

    with open(f'{nome}.txt', 'w') as arquivo:
        for itens in lista_dados:
            for i, item in enumerate(itens):  # Loop com índice
                if i > 0:
                    arquivo.write(";")  # Adiciona ";" apenas entre os itens
                arquivo.write(item)
            arquivo.write("\n")




