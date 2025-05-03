
#1. Criar o arquivo
def Escrever_Arquivo(nome, conteudo, estilo): #serve para adicionar uma nova informação
    '''

    :param nome: digitar o nome do arquivo
    :param conteudo: informação que deseja adicionar
    :param estilo: 0 para ';' e 1 para '\n'
    '''

    with open(f'{nome}.txt', 'a', encoding='utf-8') as arquivo: 
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
    with open(f'{nome}.txt', 'r', encoding='utf-8') as arquivo:
        ler = arquivo.readlines()
        for termo in ler:
            termo = termo.replace('\n', '')
            termo = termo.split(';')
            lista_dados.append(termo)
            

#Copiar_Arquivo('teste') #Para copiar o que está no arquivo


#2. Ler o arquivo
def Ler_Arquivo(): #Vai ler o arquivo
    for v, itens in enumerate(lista_dados):
        cor = 32
        print(f'\033[1;31m{v+1:2}', end=' -> ') #Vai mostrar o número da linha
        for item  in itens:    
            print(f'\033[{cor}m{item:7}', end='    ')
            cor += 1
        print() 

    
def Ler_Especifico_Arquivo(linha, coluna): #Vai ler o arquivo
    #print(lista_dados[linha-1][coluna-1]) #Vai ler o arquivo e mostrar a informação desejada
    if coluna == 0: 
        '''Explicação: 
        map(str, lista_dados[linha-1]) #Vai transformar cada item da lista em string
        '; '.join(map(str, lista_dados[linha-1])) #Vai juntar os itens da lista com "; "
        Pegue cada item da lista llinha_dados[linha-1] e transforme em string

        '''
        linha_lista = '; '.join(map(str, lista_dados[linha-1]))
        return linha_lista
    else: 
        coluna_lista = lista_dados[linha-1][coluna-1]
        return coluna_lista 




def Simples_Arquivo(nome):
    Copiar_Arquivo(f'{nome}')
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

    with open(f'{nome}.txt', 'w', encoding='utf-8') as arquivo:
        for itens in lista_dados:
            for i, item in enumerate(itens):  # Loop com índice
                if i > 0:
                    arquivo.write(";")  # Adiciona ";" apenas entre os itens
                arquivo.write(item)
            arquivo.write("\n")




