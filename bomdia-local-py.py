#!/usr/bin/env python
# coding: utf-8


import tweepy as tw
import os
import time
import schedule as sd
#Tokens:
with open('api-key/bom-dia.txt', 'r') as tfile:
    consumer_key = tfile.readline().strip('\n')
    consumer_secret = tfile.readline().strip('\n')
    access_token = tfile.readline().strip('\n')
    access_token_secret = tfile.readline().strip('\n')

# #Validação da api.

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)



#funcao para pegar uma img da pasta selecionada, esta imagem será a imagem que voce seleciona no "n".

def i(n):
  try:
    #caminho da pasta:
    caminho = ("img/")
    #listando os itens na pasta
    lista_img = os.listdir(caminho)
    #auto-explicativo
    tamanho_lista = len(lista_img)
    #aqui se não tiver a imagem ele relatará erro pois está fora do alcance da lista
    if n < tamanho_lista:
        nome_img = lista_img[n]
        image = open(caminho+lista_img[n], 'rb')
        return nome_img, image, True, tamanho_lista
    else:
        print('ERRO, pois a foto esta fora de alcance!')
        return None, None, False
  except ValueError as e :
    print('Deu errado')
    return False
#quando tudo estiver pronto ele retornara a imagem em uma tupla que voce pode colocar um nome qulquer
#na função Post ela se chama 'retorno', perceba que nela está o nome da imagem 'retorno[0]' e a imagem que o python pode ler 'retorno[1]'


#função de postar, deve se ter a imagem
def post(n):
    try:
        #aqui esta a imagem
        retorno = i(n)
        
        
        if retorno[2] == True:
            try:
                #postar com a imagem, tem que ter o nome da imagem(filename) e ela "trasformada"
                postar = api.update_status_with_media(status='Bom dia Galerinha!!! #bomdia #frasesbomdia #goodmorning #shitpost', filename= retorno[0], file = retorno[1])
                postar
                n = n+1
                return print('Postou')
                
            
            except TypeError as t:
                
                print('Algo deu errado: ', t)
            
        else:
            print('não foi possivel postar!')
    except TypeError as t:
        print('Algo deu errado: ', t)
        return None

numero = 0

while 1: 
    #pega o tamanho da lista de imagens que tem lá. Fiz isso para poder colocar as imagens quando quiser. O problema é se
    #essas imagens novas ficarem na frente das mais velhas, pois pode postar imagens repetidas.
    retorno = i(0)
    if retorno[3] > numero:
        print('Criando Job...')
        job = sd.every().day.at('06:30').do(post, n = numero)
        n = sd.idle_seconds()
        if n is None:
            # não tem mais jobs
            break
        elif n > 0:
            # vai 'dormir' ate até o job ser executado, o n é o tempo que irá levar para ele ser executado
            print('Irá dormir por: ', n, ' Segundos!')
            time.sleep(n)
            print('Rodando job...')
            sd.run_pending()
        # Para funcionar o codigo, tem que cancelar o job, e crialo novamente
        time.sleep(60)
        print('Cancelando Job...')
        sd.cancel_job(job)
        numero = numero + 1
        
    else:
        sd.clear()
        print('saiu do escopo!')
        break
    
    
    
    

