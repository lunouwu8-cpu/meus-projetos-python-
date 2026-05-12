# Controle de Gastos Simples
# Criado por Mim(Lucas nobre)

gastos = []

print("--- Sistema de Controle de Custos ---")

while True:
    item = input("\nO que você comprou? (ou digite 'sair' para encerrar): ")
    
    if item.lower() == 'sair':
        break
        
    valor = float(input(f"Quanto custou o(a) {item}? R$ "))
    
    # Salvando os dados em um dicionário
    gasto_atual = {"item": item, "valor": valor}
    gastos.append(gasto_atual)

# Resumo Final
print("\n--- Resumo de Gastos ---")
total = 0
for g in gastos:
    print(f"- {g['item']}: R$ {g['valor']:.2f}")
    total += g['valor']

print(f"\nTOTAL GERAL: R$ {total:.2f}")
print("--- Fim do Relatório ---")
