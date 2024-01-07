"""
Uma empresa na área do varejo encomendou uma pesquisa a Agência Big Data A+ para saber a opinião das pessoas gostaram ou não de um determinado produto lançando no mercado. Para isso será necessário armazenar em vetores as seguintes informações:
• o sexo do entrevistado ("M" ou "F");
• a sua idade;
• e a resposta sobre o produto("S" ou "N").

Sabe-se que foram entrevistas um número X de pessoas, elabore um programa que informe: 
• O total de pessoas que participaram da pesquisa;
• O número de pessoas que responderam Sim;
• O número de pessoas que responderam Não;
• Quantas pessoas maiores de 18 anos gostaram do produto;
• Quantas pessoas menores de 18 anos não gostaram do produto;
• Quantas pessoas maiores de 18 anos, do sexo feminino, não gostaram do produto;
• Quantas pessoas menores de 18 anos, do sexo masculino, gostaram do produto.
"""

# Função para ler a resposta do usuário, garantindo que seja 'S' ou 'N'
def obter_resposta():
    while True:
        resposta = input("Digite 'S' para Sim ou 'N' para Não: ").upper()
        if resposta in ['S', 'N']:
            return resposta
        else:
            print("Resposta inválida. Por favor, digite 'S' ou 'N'.")


# Função para ler a idade do usuário, garantindo que seja um número inteiro
def obter_idade():
    while True:
        try:
            idade = int(input("Digite a idade: "))
            return idade
        except ValueError:
            print("Idade inválida. Por favor, digite um número inteiro.")


# Inicialização de variáveis
total_pessoas = 0
pessoas_sim = 0
pessoas_nao = 0
maiores_18_gostaram = 0
menores_18_nao_gostaram = 0
maiores_18_feminino_nao_gostaram = 0
menores_18_masculino_gostaram = 0


# Perguntar ao usuário o número de pessoas entrevistadas
while True:
    try:
        total_pessoas = int(input("Digite o número de pessoas entrevistadas: "))
        if total_pessoas > 0:
            break
        else:
            print("Por favor, digite um número válido maior que zero.")
    except ValueError:
        print("Número inválido. Por favor, digite um número inteiro.")

# Loop para coletar as respostas dos entrevistados
for r in range(total_pessoas):
    print(f"\nEntrevistado {r + 1}:")
    
    sexo = input("Digite o sexo (M ou F): ").upper()
    
    idade = obter_idade()
    
    resposta = obter_resposta()

    # Contagem das estatísticas
    if resposta == 'S':
        pessoas_sim += 1
        if idade > 18:
            maiores_18_gostaram += 1
        elif idade < 18 and sexo == 'M':
            menores_18_masculino_gostaram += 1
    elif resposta == 'N':
        pessoas_nao += 1
        if idade < 18:
            menores_18_nao_gostaram += 1
        elif idade > 18 and sexo == 'F':
            maiores_18_feminino_nao_gostaram += 1

# Exibir os resultados
print("\nResultados da pesquisa:")
print(f"Total de pessoas entrevistadas: {total_pessoas}")
print(f"Número de pessoas que responderam Sim: {pessoas_sim}")
print(f"Número de pessoas que responderam Não: {pessoas_nao}")
print(f"Pessoas maiores de 18 anos que gostaram do produto: {maiores_18_gostaram}")
print(f"Pessoas menores de 18 anos que não gostaram do produto: {menores_18_nao_gostaram}")
print(f"Pessoas maiores de 18 anos, do sexo feminino, que não gostaram do produto: {maiores_18_feminino_nao_gostaram}")
print(f"Pessoas menores de 18 anos, do sexo masculino, que gostaram do produto: {menores_18_masculino_gostaram}")
