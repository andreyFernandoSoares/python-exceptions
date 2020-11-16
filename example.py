if True:
    print("Ola mundo")

frase = "Ola mundo"

print(frase.split()[0])

def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError("Dividir só deve receber argumentos inteiros!")

    try:
        aux = dividendo / divisor
    except ZeroDivisionError as E:
        print(f"Não foi possivel dividir {dividendo} por divisor {divisor}")
        raise
    
    return aux

def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f"O resultado da divisao de 10 por {divisor} é {resultado}")

    
try:
    testa_divisao("2")
except ZeroDivisionError as E:
    print("Erro de divisao por 0")
except ValueError as E:
    print(E)

print("Programa encerrado")