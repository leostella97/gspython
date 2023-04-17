import random
import string
import sys

tamanho = int(sys.argv[1])
chars = string.ascii_letters + string.digits + '!@#$%&*()-+=,.;:/?[{<>}]qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
rnd = random.SystemRandom()
senha = "".join(rnd.choice(chars) for i in range(tamanho))

print(senha)
