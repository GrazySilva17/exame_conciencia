import arquivo as arq

#1. Página inicial 
#2. Quiz
#3. Criação do arquivo 

#Ler o arquivo 

arq.Copiar_Arquivo('base') #Copia os dados 
#ler = arq.Ler_Arquivo() #Faz a leitura de dados 


#Printar cada termo do arquivo base 
for i in range(16): 
    ler = arq.Ler_Especifico_Arquivo(i, 0)
    print(f'\033[7;35m{ler}\033[0m')
    definir = str(input('Digite [S/N]: ')).strip().upper()[0]
    if definir == 'S':
        arq.Escrever_Arquivo('exame_conciencia', ler, 1) #Escrever o pecado selecionado no exame de consdiencia definitivo
        print('Vá até o confessionário mais próximo!')
    else: 
        print('Amém')