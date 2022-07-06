<h1 align="center"> ☀️ Projeto Bom Dia ☀️ </h1>

<hr>

<p align="center">
   <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge"/>
</p>

### Tópicos 

- [Descrição do projeto](#descrição-do-projeto)

- [Ferramentas utilizadas](#ferramentas-utilizadas)

- [Acesso ao projeto](#acesso-ao-projeto)

- [Abrir e rodar o projeto](#abrir-e-rodar-o-projeto)

- [Desenvolvedores](#desenvolvedores)

## Descrição do projeto 

<p align="justify">
  Neste projeto Estou usando a api do twitter para fazer um bot que consegue postar automaticamente uma imagem de bom dia no feed todos os dias as 06:30 da manhã. O meu objetivo com este projeto é aprender sobre APIs, implementar uma IA nele e evoluir o codigo. Neste dia que estou escrevendo este README, ele já consegue postar uma imagem e uma frase pré programada. 
</p>



###

## Ferramentas utilizadas


<p align="center" width="100%">
    <a href="https://developer.twitter.com/en" target="_blank"> <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="Twitter" width="30%"/></a>  
    <a href="https://www.python.org" target="_blank"> <img src="https://aws1.discourse-cdn.com/business6/uploads/python1/original/1X/fe459ce92996895410438d8efee327d394e419a0.png" alt="python" width="30%"/> </a> 
    <a href="https://cloud.google.com" target="_blank" > <img src="https://lirp.cdn-website.com/aa0ef369/dms3rep/multi/opt/google-cloud-icon-400w.png" alt="google" width="30%" /></a>
    
    
    
   
  
</p>
   
   
###

## Detalhes dos arquivos

Você pode [acessar o código fonte do projeto](https://github.com/RenanMour4/Projeto-Bom-Dia) ou [baixá-lo](https://github.com/RenanMour4/Projeto-Bom-Dia/archive/refs/heads/main.zip).

## Abrir e rodar o projeto

<p>Quando baixar a pasta inteira há dois arquivos praticamente iguais, que são: <a href='https://github.com/RenanMour4/Projeto-Bom-Dia/blob/main/bomdia_local.ipynb' target='_blank'>bomdia_local.ipynb</a> e <a href='https://github.com/RenanMour4/Projeto-Bom-Dia/blob/main/bomdia-local-py.py' target='_blank'>bomdia-local-py.py</a>. A unica diferença deles é que são extensões diferentes, a primeira usa a extensão do jupyter e a segunda do python. Fiz isso pois acho o jupyter bem melhor para testar as alterações.</p>

<p>O codigo em si é bem auto explicativo, mas explicando no geral ele primeiro faz a validação da api por meio de um <a href='https://github.com/RenanMour4/Projeto-Bom-Dia/blob/main/api-key/bom-dia.txt' target='_blank'>documento de texto</a> colocado na pasta <a href='https://github.com/RenanMour4/Projeto-Bom-Dia/tree/main/api-key' target='_blank'>api-key</a> que estão todas as credenciais para utiliza-la em ORDEM! As quatro primeiras linhas são destinadas para respectivamente: api-key, api-key-secret, acess-token e o acess-token-secret (isto é muito importante, pois se não tiver em ordem a validação falha). </p>

<p>Segundamente eu fiz um método chamado i(n) que consegue pegar a imagem que está na pasta <a href='https://github.com/RenanMour4/Projeto-Bom-Dia/tree/main/img' target='_blank'>img</a> e retorna o nome, a imagem transformada, um valor True e o tamanho da lista de imagens que a pasta tem. O 'n' um numero inteiro.</p>

<p>Terceiramente o método post faz a postagem da imagem que voce escolheu no parametro da método i(n).</p>

<p>Quartamente e finalizando fiz um while infinito que irá quebrar quando não tiver mais imagens para postar na pasta <a href='https://github.com/RenanMour4/Projeto-Bom-Dia/tree/main/img' target='_blank'>img</a>.</p>

<p>OBS: O jeito que eu fiz esta ultima parte do projeto não acredito que seja muito 'boa', pois usando o time.sleep na ultima parte o programa não consegue parar de maneira usual assim dificultando o processo de testes.Somente consegui pensar nesta solução para que o n (variavel do post) possa mudar e executar corretamente. Se quiser modificar esta ultima parte, ou o projeto inteiro, fique a vontade e entre em contato comigo por favor ;)</p>



## Desenvolvedores

[<img src="https://avatars.githubusercontent.com/u/64485870?v=4" width=115><br><sub>Renan Moura</sub>](https://github.com/RenanMour4)

