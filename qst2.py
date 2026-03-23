timesbrasileiraoserieA = ("Botafogo", "Palmeiras", "Flamengo", "Internacional", "Fortaleza", "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco", "EC Vitória", "Grêmio", "Juventude", "Atlético-MG", "Fluminense", "Athletico-PR", "Bragantino", "Criciúma", "Atlético-GO", "Cuiabá")
escolha = int(input("Digite a posição da tabela que deseja consultar: "))
while escolha < 1 or escolha > 20:
    escolha = int(input("Posição inválida! Digite um número de 1 a 20."))
print(f"{timesbrasileiraoserieA[escolha-1]} está na {escolha}º posição.")