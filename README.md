<h1 align="center"> ☀️ Projeto Bom Dia ☀️ </h1>

<hr>

<p align="center">
   <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge"/>
</p>

### Tópicos 

- [Descrição do projeto](#descrição-do-projeto)

- [Aplicação](#aplicação)

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
<div style="align-items: center;
                display: flex;
                flex-direction: row;
                justify-content: center;">
   <a href="https://www.python.org" target="_blank"> <img src="https://aws1.discourse-cdn.com/business6/uploads/python1/original/1X/fe459ce92996895410438d8efee327d394e419a0.png" alt="python" width="40" height="40"/> </a> 

  <a href="https://developer.twitter.com/en" target="_blank"> <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="Twitter" width="40" height="40"/> </a> 
  
  <a href="https://cloud.google.com" target="_blank"> <img src="https://lirp.cdn-website.com/aa0ef369/dms3rep/multi/opt/google-cloud-icon-400w.png" alt="google" width="40" height="40"/> </a>
</div>


<p align="center" width="100%">
    <a href="https://developer.twitter.com/en" target="_blank"> <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="Twitter" width="40" height="40"/> </a>
    <a href="https://developer.twitter.com/en" target="_blank"> <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="Twitter" width="40" height="40"/> </a> 
  
</p>
   
   
###

## Acesso ao projeto

Você pode [acessar o código fonte do projeto](https://github.com/RenanMour4/Projeto-Bom-Dia) ou [baixá-lo](https://github.com/RenanMour4/Projeto-Bom-Dia/archive/refs/heads/main.zip).

## Abrir e rodar o projeto

<p>Quando baixar a pasta inteira há dois arquivos praticamente iguais, que são: [bomdia_local.ipynb](https://github.com/RenanMour4/Projeto-Bom-Dia/blob/main/bomdia_local.ipynb) e [bomdia-local-py.py](https://github.com/RenanMour4/Projeto-Bom-Dia/blob/main/bomdia-local-py.py). A unica diferença deles é que são extensões diferentes, a primeira usa a extensão do jupyter e a segunda do python. Fiz isso pois acho o jupyter bem melhor para testar as alterações.</p>

<p>O codigo em si é bem auto explicativo, mas explicando no geral ele primeiro faz a validação da api por meio de um [documento de texto](https://github.com/RenanMour4/Projeto-Bom-Dia/blob/main/api-key/bom-dia.txt) colocado na pasta [api-key](https://github.com/RenanMour4/Projeto-Bom-Dia/tree/main/api-key) que estão todas as credenciais para utiliza-la em ORDEM, as quatro primeiras linhas são destinadas para respectivamente: api-key, api-key-secret, acess-token e o acess-token-secret!!! (isto é muito importante, pois se não tiver em ordem a validação falha). </p>

<p>Segundamente eu fiz uma função chamada i() que consegue pegar a imagem que está na pasta img e "transforma" ela.</p>

<p>Terceiramente a Função post faz a postagem da imagem que voce escolheu no parametro da função i().</p>

<p>Quartamente e finalizando fiz um while infinito que irá quebrar quando não tiver mais imagens para postar na pasta [IMG](https://github.com/RenanMour4/Projeto-Bom-Dia/tree/main/img).</p>

<p>OBS: O jeito que eu fiz esta ultima parte do projeto não acredito que seja muito usual, pois usando o time.sleep na ultima parte o programa não consegue parar de maneira usual assim dificultando o processo de testes. Se você quiser modificar esta ultima parte, fique a vontade ;)</p>



## Desenvolvedores

[<img src="https://avatars.githubusercontent.com/u/64485870?v=4" width=115><br><sub>Renan Moura</sub>](https://github.com/RenanMour4)

