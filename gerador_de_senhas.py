import random
import string

# Pede o número desejado, de 1 a n 
tamanho = int(input("Digite o tamanho de senha que deseja: "))

# Coloca quais caracteres podem entrar na senha gerada
chars = string.ascii_letters + string.digits + '!@#$%&*()-+=,.;:/?[{<>}]qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'


# Algoritmo de aleatoriedade
rnd = random.SystemRandom() 

# Mostra a senha gerada
print("Senha gerada: ")

# Gera a senha a ser mostrada
print("".join(rnd.choice(chars) for i in range(tamanho)))
 
