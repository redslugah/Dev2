'''1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?'''

def questao_1():
    print("Questão 1")
    INDICE = 13
    SOMA = 0
    K = 0
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    print(SOMA)

questao_1()
# O valor da variável SOMA será 91.


'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;'''

def questao_2():
    print("Questão 2")
    def fibonacci(n):
        fib = [0, 1]
        while fib[-1] < n:
            fib.append(fib[-1] + fib[-2])
        return fib

    numero = int(input("Informe um número: "))
    sequencia = fibonacci(numero)

    if numero in sequencia:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

questao_2()

'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;'''

import json

def questao_3():
    print("Questão 3")
    with open('dados.json', 'r') as file:
        dados = json.load(file)

    faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)

    media_mensal = sum(faturamentos) / len(faturamentos)

    dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

    print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
    print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

questao_3()

'''4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.'''

def questao_4():
    print("Questão 4")
    faturamento = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    total_faturamento = sum(faturamento.values())

    for estado, valor in faturamento.items():
        percentual = (valor / total_faturamento) * 100
        print(f"{estado}: {percentual:.2f}%")

questao_4()

'''5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;'''

def questao_5():
    print("Questão 5")
    string = input("Informe uma string: ")
    string_invertida = ""

    for char in string:
        string_invertida = char + string_invertida

    print(f"String invertida: {string_invertida}")

questao_5()