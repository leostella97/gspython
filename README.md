# Gerador de Senha
## Gerador de senhas em Python com escolha de caracteres

Esse <b>código em Python</b> <i>gera senhas aleatórias</i> com base em caracteres alfanuméricos e especiais onde é <i>escolhida a quantidade</i>. A seguir, um passo a passo explicando o código:

• A primeira linha importa o módulo <b>random</b>, que será usado para <i>gerar a senha aleatória</i>, e o módulo <b>string</b>, que contém caracteres <i>alfanuméricos e especiais</i> que podem ser usados na senha.

• A segunda linha <i>solicita ao usuário</i> o tamanho da senha que ele deseja.

• A terceira linha <b>concatena</b> os caracteres que serão usados na senha, incluindo letras <i>maiúsculas e minúsculas</i>, números e uma variedade de caracteres especiais.

• A quarta linha cria um objeto <b>random.SystemRandom()</b> que será usado para <i>gerar a senha aleatória de forma segura</i>.

• A quinta linha imprime a mensagem <b>"Senha gerada: "</b> para informar que a <i>senha será exibida</i>.

• A sexta linha usa um laço <b>for</b> para <i>gerar a senha aleatória</i>. A função <b>rnd.choice(chars)</b> escolhe um caractere aleatório da <b>string chars</b> e o laço é executado com o tamanho_escolhido vezes, gerando assim uma senha com o <i>tamanho especificado</i> pelo usuário.

• A última linha imprime a senha aleatória gerada pelo código com o comando <b>print</b>.