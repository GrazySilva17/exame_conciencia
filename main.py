import arquivo as arq

#1. Página inicial 
#2. Quiz
#3. Criação do arquivo 

#Ler o arquivo 

arq.Copiar_Arquivo('base') #Copia os dados 
ler = arq.Ler_Arquivo(True) #Faz a leitura de dados 

for i in range(16): 
    arq.Ler_Arquivo(True, True)