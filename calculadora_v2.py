saida = ''
def adicao(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b
def calculadora(a, b, op):
    if op == '+':
        return adicao(a, b)
    elif op == '-':
        return subtracao(a, b)
    elif op == '*':
        return multiplicacao(a, b)
    elif op == '/':
        return divisao(a, b)
while saida != 'n':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    op = input("Digite a operação (+, -, *, /): ")
    resultado = calculadora(num1, num2, op)
    print(f"Resultado da operação: {resultado}")
    saida = input("Deseja continuar? (S/N): ").lower()
