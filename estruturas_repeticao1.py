entrada_idade = None
while entrada_idade != 0:
    entrada_idade = input('Digite um numero qualquer ou 0 para sair: ')
    if entrada_idade.isdigit():
        entrada_idade = int(entrada_idade)
        print(f'Numero digitado: {entrada_idade}')
    else:
        print('Digite um numero valido!')

