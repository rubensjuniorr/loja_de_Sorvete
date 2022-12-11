print("Bem vindo a Sorveteria do Rubens Junior")
print("-" * 45 + "Cardápio" + "-" * 43)
print("| Código | Descrição             | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (1500ml) |")
print("|   TR   | Sabores Tradicionais  |      R$ 6,00      |       R$10,00      |        R$18,00     |")
print("|   ES   | Sabores Especiais     |      R$ 7,00      |       R$12,00      |        R$21,00     |")
print("|   PR   | Sabores Premium       |      R$ 8,00      |       R$14,00      |        R$24,00     |")
print("-" * 48 + "-" * 48)
codigo_valido = True
tamanho_valido = True

tamanho_p = 6
tamanho_m = 10
tamanho_g = 18
conta_final = 0
while True:
    tamanho = input("Digite o TAMANHO do pote desejado (P/M/G)")
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print("Tamanho Inválido tente novamente")
        continue

    codigo = input("Digite o CÓDIGO do sorvete desejado (TR/ES/PR)")

    if tamanho == 'P':
        if codigo == 'TR':
            print("Você pediu um sorvete sabor TRADICIONAL P de R$ 6,00")
            conta_final += tamanho_p
        elif codigo == 'ES':
            conta_final += tamanho_p + 1
            print("Você pediu um sorvete sabor ESPECIAL P de R$ 7,00")
        elif codigo == 'PR':
            conta_final += tamanho_p + 2
            print("Você pediu um sorvete sabor PREMIUM P de R$ 8,00")
        else:
            print("Código inválido tente novamente!!")

    elif tamanho == 'M':

        if codigo == 'TR':
            conta_final += tamanho_m
            print("Você pediu um sorvete sabor TRADICIONAL M de R$ 10,00")
        if codigo == 'ES':
            conta_final += tamanho_m + 2
            print("Você pediu um sorvete sabor ESPECIAL M de R$ 12,00")
        if codigo == 'PR':
            conta_final += tamanho_m + 4
            print("Você pediu um sorvete sabor PREMIUM M de R$ 14,00")
        else:
            print("Código inválido tente novamente!!")

    elif tamanho == 'G':
        if codigo == 'TR':
            print("Você pediu um sorvete sabor TRADICIONAL G de R$ 18,00")
            conta_final += tamanho_g
        elif codigo == 'ES':
            conta_final += tamanho_g + 3
            print("Você pediu um sorvete sabor ESPECIAL G de R$ 21,00")
        elif codigo == 'PR':
            conta_final += tamanho_g + 6
            print("Você pediu um sorvete sabor PREMIUM G de R$ 24,00")
        else:
            print("Código inválido tente novamente!!")
    pedir_mais = input("Deseja pedir algum pote? se sim digite S ou N para fechar a conta.")
    if pedir_mais == 'S':
        continue
    if pedir_mais == 'N':
        print("O total da compra:R${}".format(conta_final))
        break













