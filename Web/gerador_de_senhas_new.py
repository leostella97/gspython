import argparse
import secrets
import string


def main():
    parser = argparse.ArgumentParser(description="Gerador de senhas (CLI)")
    parser.add_argument("-n", "--length", type=int, default=12, help="Tamanho da senha (padrão: 12)")
    args = parser.parse_args()

    tamanho = args.length
    if tamanho <= 0:
        parser.error("O tamanho da senha deve ser maior que zero")
    if tamanho > 256:
        # clamp to a reasonable maximum
        tamanho = 256

    chars = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(secrets.choice(chars) for _ in range(tamanho))
    print(senha)


if __name__ == "__main__":
    main()
