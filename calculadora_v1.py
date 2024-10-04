def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a, b):
    return a ** (1/b)

def resto(a, b):
    return a % b

operacoes = {
    '+': soma,
    '-': subtracao,
    '*': multiplicacao,
    '/': divisao,
    '**': potencia,
    '//': raiz,
    '%': resto
}

while True:
    a = float(input('Digite um numero: '))
    op = input('Digite uma operacao (ou "sair" para sair): ')
    if op.lower() == 'sair':
        break
    b = float(input('Digite outro numero: '))

    if op not in operacoes:
        print('Operacao invalida!')
        continue

    resultado = operacoes[op](a, b)
    print(f'{a} {op} {b} = {resultado}')
