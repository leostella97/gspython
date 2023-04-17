# Gerador de Senha
## Gerador de senhas em Python com escolha de caracteres
Este é um código Python que utiliza a biblioteca tkinter para criar uma interface gráfica simples para gerar senhas aleatórias.

A primeira linha do código importa a biblioteca tkinter e a renomeia como "tk". A segunda linha importa a biblioteca random, que será usada para gerar caracteres aleatórios para a senha. A terceira linha importa a biblioteca string, que contém um conjunto de caracteres padrão que serão utilizados para a criação da senha. A quarta linha importa a biblioteca webbrowser, que será utilizada para abrir um link em um navegador web.

A função "gerar_senha" é definida na linha 5. Ela obtém o tamanho da senha a ser gerada a partir do valor inserido no widget "entrada_tamanho". Em seguida, a função cria uma string contendo todos os caracteres possíveis que podem ser utilizados na senha. A string é composta por letras maiúsculas e minúsculas, números e alguns caracteres especiais. A função utiliza o gerador de números aleatórios "SystemRandom" para escolher caracteres aleatórios da string e, por fim, insere a senha gerada no widget "senha_gerada".

A função "abrir_link" é definida na linha 9. Ela recebe um evento como parâmetro e abre um link em um navegador web utilizando a biblioteca webbrowser.

Na linha 11, a janela principal é criada utilizando a função "Tk" da biblioteca tkinter. Em seguida, o título da janela é definido como "Gerador de Senha".

Na linha 13, um widget "Label" é criado para exibir o texto "Tamanho da senha:" e é posicionado na primeira linha e primeira coluna da janela utilizando o método "grid".

Na linha 15, é criado um widget "Entry" para permitir que o usuário insira o tamanho da senha que deseja gerar. O widget é posicionado na primeira linha e segunda coluna da janela utilizando o método "grid".

Na linha 17, é criado um botão "Gerar senha" que, quando clicado, chama a função "gerar_senha". O botão é posicionado na segunda linha e primeira coluna da janela utilizando o método "grid".

Na linha 19, é criado um widget "Entry" para exibir a senha gerada. O widget é posicionado na terceira linha e primeira coluna da janela utilizando o método "grid".

Na linha 21, é criado um widget "Label" para exibir o texto "Desenvolvido por Leonardo Stella" em azul e com um cursor do tipo "hand2". O widget é posicionado na quarta linha e primeira coluna da janela utilizando o método "grid". Além disso, a linha 22 faz com que a função "abrir_link" seja chamada quando o widget é clicado, enquanto as linhas 23 e 24 fazem com que o widget seja sublinhado quando o cursor está sobre ele e desfazem o sublinhado quando o cursor sai.

Por fim, a linha 26 inicia o loop principal da interface gráfica, mantendo a janela aberta até que o usuário a feche.

<a href="https://github.com/leostella97/gspython/blob/main/Execut%C3%A1vel/gerador_de_senhas.exe">> Download</a>
<br>
<a href="http://senha.lesttech.com.br/">> Sistema Web</a>