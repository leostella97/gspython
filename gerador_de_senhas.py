import random
import string

tamanho = int(input("Digite o tamanho de senha que deseja: "))

chars = string.ascii_letters + string.digits + '!@#$%&*()-+=,.;:/?[{<>}]'

rnd = random.SystemRandom() 

print("Senha gerada: ")
print("".join(rnd.choice(chars) for i in range(tamanho)))
